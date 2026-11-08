#!/usr/bin/env python3
"""Check shipped structure reproducibility and every narration/translation reference."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / "tools/generate-structures.py"), "--check"], check=True)
subprocess.run([sys.executable, str(root / "tools/generate-guis.py"), "--check"], check=True)

def language(code):
    entries = {}
    for line in (root / f"src/main/resources/assets/ae2s_ponder/lang/{code}.lang").read_text().splitlines():
        if not line.strip() or line.startswith("#"): continue
        key, text = line.split("=", 1)
        assert key not in entries, f"Duplicate {code} key: {key}"
        assert text.strip(), f"Empty {code} translation: {key}"
        entries[key] = text
    return entries

en, zh = language("en_us"), language("zh_cn")
assert en.keys() == zh.keys(), f"Language keys differ: {en.keys() ^ zh.keys()}"
source = (root / "src/main/java/dev/yudream/ae2sponder/compat/AE2SScenes.java").read_text()
references = re.findall(r'explain\(scene, util, "([^"]+)"', source)
for key in references:
    assert f"ae2s_ponder.ponder.shared.{key}" in en, f"Missing narration: {key}"
scene_ids = re.findall(r'begin\(scene, "([^"]+)"', source)
for scene_id in scene_ids:
    assert f"ae2s_ponder.ponder.{scene_id}.header" in en, f"Missing title: {scene_id}"
    assert (root / f"src/main/resources/assets/ae2s_ponder/ponder/{scene_id}.nbt").is_file()
assert len(scene_ids) == len(set(scene_ids))
subprocess.run([sys.executable, str(root / "tools/generate-guides.py"), "--check"], check=True)
import json
index = json.loads((root / "src/main/resources/assets/ae2s_ponder/ponder/guides/index.json").read_text())["pages"]
assert len(index) == 25 and len(set(index)) == len(index)
for page in index:
    for code in ("en_us", "zh_cn"):
        assert (root / f"src/main/resources/assets/ae2s_ponder/ponder/guides/{code}/{page}.md").is_file()
    if page != "troubleshooting":
        assert (root / f"src/main/resources/assets/ae2s_ponder/ponder/{page}.nbt").is_file()
print(f"Verified {len(scene_ids)} scenes, {len(references)} narration steps, {len(en)} keys in each language")
