#!/usr/bin/env python3
"""Download the pinned official AE2S development artifact and verify SHA-256."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--artifact", choices=["dev", "runtime"], default="dev")
args = parser.parse_args()
lock = json.loads((root / "dependency-lock.json").read_text())
artifact = lock["ae2s"][args.artifact]
target = root / "libs" / artifact["file"]
target.parent.mkdir(parents=True, exist_ok=True)

def valid(path):
    return path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == artifact["sha256"]

if not valid(target):
    # Optional local cache, never an unchecked substitute for the pinned official jar.
    cache = Path(os.environ.get("AE2S_CACHE", str(root.parents[1] / ".dev/ae2s-1.1.0"))) / artifact["file"]
    if valid(cache):
        shutil.copyfile(cache, target)
    else:
        temporary = target.with_suffix(".download")
        try:
            subprocess.run(["curl", "--fail", "--location", "--retry", "3", "--max-time", "180",
                            "--output", str(temporary), artifact["url"]], check=True)
            if not valid(temporary): raise SystemExit("AE2S SHA-256 mismatch: " + str(temporary))
            temporary.replace(target)
        finally:
            temporary.unlink(missing_ok=True)
print(f"Verified {target.name}: {artifact['sha256']}")
