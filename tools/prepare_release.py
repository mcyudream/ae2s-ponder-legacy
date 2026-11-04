#!/usr/bin/env python3
"""Stage versioned installation/source jars, checksums and release notes for CI."""
import hashlib
import json
import os
from pathlib import Path
import shutil
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    identity = json.loads((ROOT / 'legacy-identity.json').read_text())
    tag = identity['release_tag']
    version = tag.removeprefix('v')
    if os.environ.get('REF_TYPE') == 'tag' and os.environ.get('REF_NAME') != tag:
        raise SystemExit('Tag must match packaged version: ' + tag)
    names = [identity['modid'] + '-' + version + suffix + '.jar'
             for suffix in ('', '-sources')]
    installation = ROOT / 'build/libs' / names[0]
    with ZipFile(installation) as archive:
        metadata = json.loads(archive.read('mcmod.info'))[0]
    if metadata['version'] != version or metadata['modid'] != identity['modid']:
        raise SystemExit('Packaged version or loader identity differs from release tag')
    if hashlib.sha256(installation.read_bytes()).hexdigest() != identity['verified_jar_sha256']:
        raise SystemExit('Refusing to stage an installation jar without matching runtime acceptance')
    sources = [ROOT / 'build/libs' / name for name in names]
    notes = ROOT / 'docs/releases' / (version + '.md')
    for path in [*sources, notes]:
        if not path.is_file():
            raise SystemExit('Missing release input: ' + str(path))
    dist = ROOT / 'build/release'
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir(parents=True)
    for source in sources:
        shutil.copyfile(source, dist / source.name)
    checksums = ''.join(hashlib.sha256((dist / name).read_bytes()).hexdigest()
                        + '  ' + name + '\n' for name in names)
    (dist / 'SHA256SUMS').write_text(checksums)
    shutil.copyfile(notes, dist / 'RELEASE-NOTES.md')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write('### Packaged assets\n\n```text\n' + checksums + '```\n')
    print(checksums, end='')


if __name__ == '__main__':
    main()
