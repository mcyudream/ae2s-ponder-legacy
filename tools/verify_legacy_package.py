#!/usr/bin/env python3
"""Check release metadata; this does not replace runtime compatibility acceptance."""
import argparse
import json
import hashlib
from pathlib import Path
from zipfile import ZipFile
p = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--require-verified-hash', action='store_true',
                    help='Require this installation jar and all baseline reports to match runtime acceptance')
args = parser.parse_args()
identity = json.loads((p/'legacy-identity.json').read_text())
version = identity['release_tag'].removeprefix('v')
jars = list((p/'build/libs').glob(identity['modid']+'-'+version+'.jar'))
if len(jars) != 1:
    raise SystemExit('Expected exactly one production jar: '+repr(jars))
with ZipFile(jars[0]) as archive:
    metadata = json.loads(archive.read('mcmod.info'))[0]
    assert metadata['modid'] == identity['modid'], metadata
    assert metadata['name'] == identity['name'], metadata
    assert metadata['authorList'] == ['yudream'], metadata
    logo = metadata['logoFile']
    assert logo in archive.namelist(), 'Missing project icon: ' + logo
    assert archive.read(logo) == (p/'branding/icon.png').read_bytes(), 'Packaged icon differs from project artwork'
    assert '${' not in archive.read('mcmod.info').decode(), 'Unexpanded metadata'
    assert not any('/dev/' in name or 'Smoke.class' in name for name in archive.namelist() if name.endswith('.class')), 'Development harness in release'
    classes = [name for name in archive.namelist() if name.endswith('.class')]
    assert all(name.startswith('dev/yudream/ae2sponder/') for name in classes), 'Bundled dependency classes'
    assert identity['release_tag'] == 'v' + metadata['version'], 'Release tag differs from packaged version'
sha256 = hashlib.sha256(jars[0].read_bytes()).hexdigest()
if args.require_verified_hash:
    if sha256 != identity['verified_jar_sha256']:
        raise SystemExit('Runtime acceptance required for new jar SHA-256: ' + sha256
                         + '\nAccepted: ' + identity['verified_jar_sha256'])
    evidence = p / identity['verification_directory']
    lock = json.loads((p/'dependency-lock.json').read_text())
    for variant in ('client-with-ponder', 'client-without-ponder',
                    'server-with-ponder', 'server-without-ponder'):
        report = json.loads((evidence / variant / 'report.json').read_text())
        runtime = json.loads((evidence / variant / 'runtime.json').read_text())
        if (report.get('result') != 'PASS' or report.get('cleanroom') != '0.4.0'
                or report.get('scenario','full') != 'full' or runtime.get('scenario','full') != 'full'
                or runtime.get('cleanroom') != '0.4.0'
                or runtime['jars'].get(jars[0].name) != sha256
                or report.get('ponder') != ('-with-ponder' in variant)
                or (variant.startswith('client-') and report.get('addonVersion') != version)):
            raise SystemExit('Formal Cleanroom 0.4.0 acceptance mismatch: ' + variant)
        if '-with-ponder' not in variant:
            continue
        if (runtime['jars'].get(lock['ponder']['runtime']['file'])
                != identity['verified_ponder_release_sha256']
                or report.get('ponderVersion') != lock['ponder']['version']):
            raise SystemExit('Published Ponder release acceptance mismatch: ' + variant)
print('PASS:', jars[0].name, metadata['modid'], 'SHA-256:', sha256)
