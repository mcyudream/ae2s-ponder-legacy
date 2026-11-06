#!/usr/bin/env python3
"""Verify production jars on official Cleanroom 0.4.0, without a development resource pack (Linux x64)."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import urllib.request
from zipfile import ZipFile

PROJECT = Path(__file__).resolve().parent.parent
WORKSPACE = Path(os.environ.get("AE2S_PONDER_WORKSPACE", str(PROJECT.parent.parent)))
VERSION = "0.4.0"
CACHE = WORKSPACE / ".dev" / f"cleanroom-{VERSION}-runtime"
GRADLE = Path(os.environ.get("GRADLE_USER_HOME", Path.home() / ".gradle"))
PACK = WORKSPACE / ".dev" / f"cleanroom-{VERSION}-installer.jar"
PACK_SHA256 = "882435d851a51e14b802e0a9384e4a05cfbb3890fca435c40c494af75e5a166f"


def digest(path, algorithm="sha1"):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, algorithm).hexdigest()


def download(url, destination, expected, algorithm="sha1", candidates=()):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file() and digest(destination, algorithm) == expected:
        return destination
    for candidate in candidates:
        if candidate.is_file() and digest(candidate, algorithm) == expected:
            shutil.copyfile(candidate, destination)
            return destination
    urls = [url]
    if url.startswith("https://repo.cleanroommc.com/releases/"):
        urls.insert(0, url.replace("https://repo.cleanroommc.com/releases/", "https://maven.cleanroommc.com/"))
    last_error = None
    for attempt in range(2):
        for source in urls:
            try:
                request = urllib.request.Request(source, headers={"User-Agent": "HNN-Cleanroom-verification"})
                partial = destination.with_name(destination.name + ".part")
                with urllib.request.urlopen(request, timeout=30) as response, partial.open("wb") as output:
                    shutil.copyfileobj(response, output, 128 * 1024)
                if digest(partial, algorithm) != expected:
                    raise ValueError(f"Hash mismatch: {destination.name}")
                partial.replace(destination)
                print("Downloaded", destination.name, flush=True)
                return destination
            except (OSError, ValueError) as error:
                last_error = error
    raise RuntimeError(f"Could not download {url}: {last_error}")


def allowed(library):
    rules = library.get("rules", [])
    result = not rules
    for rule in rules:
        os_rule = rule.get("os", {})
        if os_rule.get("name", "linux") == "linux" and os_rule.get("arch", "x86_64") in ("x86_64", "amd64"):
            result = rule["action"] == "allow"
    # The historical MMC recipe also lists ARM natives with a plain Linux rule.
    classifier = library["name"].split(":")[3:]
    return result and (not classifier or not classifier[0].startswith("natives-") or classifier == ["natives-linux"])


def artifact(library):
    entry = library["downloads"]["artifact"]
    parts = library["name"].split(":")
    group, module, version = parts[:3]
    path = entry.get("path") or f"{group.replace('.', '/')}/{module}/{version}/{entry['url'].rsplit('/', 1)[1]}"
    candidates = (GRADLE / "caches/modules-2/files-2.1" / group / module / version).glob(f"*/{Path(path).name}")
    candidates = list(candidates)
    if module == "cleanroom":
        candidates.append(WORKSPACE / ".dev" / f"cleanroom-{VERSION}-universal.jar")
    # Reuse byte-identical libraries from the old verification cache only after SHA-1 validation.
    candidates += list((WORKSPACE / ".dev/cleanroom-0.4.0-alpha-runtime/libraries").glob("**/" + Path(path).name))
    if module == "cleanroom":
        entry = dict(entry, url=f"https://maven.cleanroommc.com/com/cleanroommc/cleanroom/{VERSION}/cleanroom-{VERSION}-universal.jar")
    return download(entry["url"], CACHE / "libraries" / path, entry["sha1"], candidates=candidates)


def prepare(side):
    download(f"https://maven.cleanroommc.com/com/cleanroommc/cleanroom/{VERSION}/{PACK.name}", PACK, PACK_SHA256, "sha256")
    with ZipFile(PACK) as archive:
        recipe = json.loads(archive.read("version.json"))
    if recipe["id"] != f"cleanroom-{VERSION}":
        raise ValueError("Unexpected Cleanroom version in the official installer")
    metadata = json.loads((GRADLE / "caches/cleanroom_gradle/versions/1.12.2/meta.json").read_text())
    # Cleanroom replaces vanilla's obsolete LWJGL, Netty, ICU, JNA, logging and utility libraries.
    # Retain only the vanilla audio, authentication and platform services used by the official recipe.
    retained = {"com.paulscode", "com.mojang:authlib", "com.mojang:realms", "com.mojang:text2speech", "ca.weblite:java-objc-bridge"}
    vanilla_libraries = [library for library in metadata["libraries"]
                        if library["name"].split(":")[0] in retained or ":".join(library["name"].split(":")[:2]) in retained]
    libraries = {}
    for group in (recipe["libraries"], vanilla_libraries):
        for library in group:
            if allowed(library):
                libraries.setdefault(library["name"], library)
                native = library.get("natives", {}).get("linux")
                if native:
                    libraries.setdefault(library["name"] + ":" + native, {
                        "name": library["name"] + ":" + native,
                        "downloads": {"artifact": library["downloads"]["classifiers"][native]},
                    })
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        classpath = list(pool.map(artifact, libraries.values()))
    main = metadata["downloads"][side]
    vanilla = GRADLE / f"caches/cleanroom_gradle/versions/1.12.2/{side}.jar"
    classpath.append(download(main["url"], CACHE / f"minecraft-{side}-1.12.2.jar", main["sha1"], candidates=[vanilla]))
    # Never let concurrent verifiers overwrite ELF files mapped by this JVM.
    natives = PROJECT / "build/verification-natives" / str(os.getpid())
    natives.mkdir(parents=True, exist_ok=True)
    for jar in classpath:
        if "natives-linux" in jar.name:
            with ZipFile(jar) as archive:
                for name in archive.namelist():
                    if name.endswith(".so"):
                        target = natives / Path(name).name
                        data = archive.read(name)
                        if not target.is_file() or target.read_bytes() != data:
                            partial = target.with_name(target.name + f".{os.getpid()}.part")
                            partial.write_bytes(data)
                            partial.replace(target)
    return classpath, natives



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("side", choices=["client", "server"])
    parser.add_argument("--with-ponder", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if platform.system() != "Linux" or platform.machine() not in ("x86_64", "amd64"):
        parser.error("This verification launcher supports Linux x64")
    classpath, natives = prepare(args.side)
    if args.prepare_only:
        return
    variant = f"{args.side}-{'with' if args.with_ponder else 'without'}-ponder"
    run = PROJECT / "run" / f"cleanroom-{VERSION}-legacy" / variant
    mods = run / "mods"
    if mods.exists():
        shutil.rmtree(mods)
    mods.mkdir(parents=True)
    identity = json.loads((PROJECT / "legacy-identity.json").read_text())
    addon_version = identity["release_tag"].removeprefix("v")
    jars = [PROJECT / "build/libs" / f"{identity['modid']}-{addon_version}.jar",
            PROJECT / "libs/AppliedEnergistics2-Supergiant-1.1.0.jar",
            PROJECT / "build/dev/ae2s-ponder-verification-srg.jar"]
    lock = json.loads((PROJECT / "dependency-lock.json").read_text())
    if digest(jars[1], "sha256") != lock["ae2s"]["runtime"]["sha256"]:
        raise ValueError("AE2S installation jar differs from the official pinned artifact")
    if args.with_ponder:
        ponder = Path(os.environ.get("LEGACY_PONDER_JAR", PROJECT.parent / "ponder/build/libs" / lock["ponder"]["runtime"]["file"]))
        if digest(ponder, "sha256") != lock["ponder"]["runtime"]["sha256"]:
            raise ValueError("Ponder differs from the pinned official installation jar")
        jars += [ponder]
    for jar in jars:
        if not jar.is_file():
            raise FileNotFoundError(f"Build the addon, Ponder and SRG harness first: {jar}")
        shutil.copyfile(jar, mods / jar.name)
    config = run / "config"
    config.mkdir(exist_ok=True)
    (config / "splash.properties").write_text("enabled=false\n")
    output = run / "ae2s-ponder-smoke"
    if output.exists():
        shutil.rmtree(output)
    local_jdk = WORKSPACE / ".dev/jdk-25.0.5+8"
    jdk = Path(os.environ.get("AE2S_PONDER_JAVA_HOME",
               str(local_jdk) if (local_jdk / "bin/java").is_file() else os.environ.get("JAVA_HOME", "")))
    command = [str(jdk / "bin/java"), "-Xmx3G", "-Dfile.encoding=UTF-8", "--enable-native-access=ALL-UNNAMED",
               f"-Djava.library.path={natives}", "-Dae2sponder.smoke=true", "-Dae2sponder.packaged=true",
               f"-Dae2sponder.expectedAddon={addon_version}",
               f"-Dae2sponder.expectedCleanroom={VERSION}", "-cp", os.pathsep.join(map(str, classpath))]
    if args.with_ponder:
        command.insert(1, f"-Dae2sponder.expectedPonder={lock['ponder']['version']}")
    if args.side == "client":
        command += ["top.outlands.foundation.boot.Foundation", "--tweakClass", "net.minecraftforge.fml.common.launcher.FMLTweaker",
                    "--username", "AE2SPonderDev", "--uuid", "8b543c6b-0aaf-3b93-bf4a-e15e899058c8", "--accessToken", "0",
                    "--version", f"Cleanroom-{VERSION}", "--gameDir", str(run),
                    "--assetsDir", str(GRADLE / "caches/cleanroom_gradle/assets"), "--assetIndex", "1.12",
                    "--width", "1280", "--height", "720"]
    else:
        eula = run / "eula.txt"
        # Reuse the owner's existing acceptance for this same local verification server.
        accepted = PROJECT / "run/server/eula.txt"
        if not eula.exists() and accepted.exists():
            shutil.copyfile(accepted, eula)
        if not eula.exists() or "eula=true" not in eula.read_text().splitlines():
            parser.error(f"The local test server owner must accept the Minecraft EULA in {eula}")
        (run / "server.properties").write_text("server-ip=127.0.0.1\nserver-port=0\nonline-mode=false\nview-distance=2\nlevel-type=FLAT\n")
        command += ["net.minecraftforge.fml.relauncher.ServerLaunchWrapper", "nogui"]
    runtime = {"cleanroom": VERSION, "side": args.side, "ponder": args.with_ponder,
               "installer_sha256": PACK_SHA256, "jars": {jar.name: digest(jar, "sha256") for jar in jars},
               "libraries": {str(jar.relative_to(CACHE)): digest(jar) for jar in classpath}}
    environment = os.environ.copy()
    if args.side == "client":
        # Visual verification does not need host audio. Avoid PipeWire native crashes
        # when Minecraft reloads the sound engine during language switching.
        environment["ALSOFT_DRIVERS"] = "null"
        runtime["audio_backend"] = "null"
    (run / "runtime.json").write_text(json.dumps(runtime, indent=2) + "\n")
    print(f"Starting official Cleanroom {VERSION}: {variant}; installation jars, no userdev remapping", flush=True)
    result = subprocess.run(command, cwd=run, env=environment, timeout=600)
    report = output / "report.json"
    if result.returncode or not report.exists() or json.loads(report.read_text())["result"] != "PASS":
        raise SystemExit(f"Verification failed (exit={result.returncode}): {report}")
    destination = PROJECT / "build/reports/verification" / variant
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(output, destination)
    shutil.copyfile(run / "runtime.json", destination / "runtime.json")
    print("PASS:", destination / "report.json", flush=True)


if __name__ == "__main__":
    main()
