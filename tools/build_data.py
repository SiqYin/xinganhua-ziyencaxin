#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把西安话字音表（tools/xinganhua.詳注.tsv）与 OpenCC 简繁表打包成前端用的 JSON。

用法（在仓库根目录）：python tools/build_data.py
输出：data/xian.json、data/variants.json
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICT_TSV = ROOT / "data" / "source.tsv"   # 字 / 拼音 / IPA[调名] / 释注
OPENCC = ROOT / "tools" / "opencc"
ST_TXT = OPENCC / "STCharacters.txt"   # 简 → 繁（OpenCC）
TS_TXT = OPENCC / "TSCharacters.txt"   # 繁 → 简（OpenCC）
OUT = ROOT / "data"

OPENCC_BASE = "https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary/"


def ensure_opencc() -> None:
    """简繁表不入库，构建时按需下载。"""
    import urllib.request

    OPENCC.mkdir(parents=True, exist_ok=True)
    for path in (ST_TXT, TS_TXT):
        if not path.exists():
            print(f"下载 {path.name} …")
            urllib.request.urlretrieve(OPENCC_BASE + path.name, path)

TONE_NAME = {"陰平": "阴平", "陽平": "阳平", "上聲": "上声", "去聲": "去声"}
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
TONED = re.compile(r"^([a-z]+)([1-4])$")


def load_opencc(path):
    table = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        key, values = parts[0].strip(), parts[1].split()
        if len(key) == 1 and values:
            table[key] = values
    return table


def load_readings():
    records = {}
    order = []
    lines = Path(DICT_TSV).read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        char, reading, ipa_field = parts[0], parts[1], parts[2]
        note = parts[3].strip() if len(parts) > 3 else ""
        m = re.match(r"^(.*)\[(.*?)\]$", ipa_field)
        ipa, tone_label = (m.group(1), m.group(2)) if m else (ipa_field, "")
        tm = re.match(r"^(\D+?)([1-9][0-9]?)$", tone_label)
        tone, value = (tm.group(1), tm.group(2)) if tm else (tone_label, "")
        note = note.strip("{}").strip() if note.startswith("{") else note
        if char not in records:
            records[char] = []
            order.append(char)
        records[char].append(
            {
                "py": reading,
                "ipa": unicodedata.normalize("NFC", ipa),
                "tone": TONE_NAME.get(tone, tone),
                "val": value,
                "val_sup": value.translate(SUP),
                "note": note,
            }
        )
    tone_rank = {"阴平": 1, "阳平": 2, "上声": 3, "去声": 4}
    for char, items in records.items():
        items.sort(key=lambda r: (tone_rank.get(r["tone"], 9), r["py"]))
        for i, item in enumerate(items):
            item["first"] = i == 0
    return [{"id": i + 1, "character": c, "readings": records[c]} for i, c in enumerate(order)]


def build_variants(chars, st, ts):
    """s2t：简化字 → 本字典里对应的繁体字；t2s：繁体字 → 简体写法（用于并列显示）。"""
    t2s = {}
    s2t = {}
    for t in chars:
        simplified = ts.get(t, [t])[0]
        t2s[t] = simplified if simplified != t else ""
        if simplified != t:
            s2t.setdefault(simplified, [])
            if t not in s2t[simplified]:
                s2t[simplified].append(t)
        # 本字本身也是别人的简化形（如「干」之于「乾/幹」）时一并挂上
        for alt in st.get(t, []):
            if alt != t:
                s2t.setdefault(t, [])
                if alt not in s2t[t]:
                    s2t[t].append(alt)
    for key in list(s2t):
        s2t[key].sort()
    return {"s2t": s2t, "t2s": {k: v for k, v in t2s.items() if v}}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ensure_opencc()
    st = load_opencc(ST_TXT)
    ts = load_opencc(TS_TXT)
    records = load_readings()
    chars = [r["character"] for r in records]
    variants = build_variants(chars, st, ts)

    (OUT / "xian.json").write_text(
        json.dumps(records, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )
    (OUT / "variants.json").write_text(
        json.dumps(variants, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )

    readings = sum(len(r["readings"]) for r in records)
    noted = sum(1 for r in records for x in r["readings"] if x["note"])
    poly = sum(1 for r in records if len(r["readings"]) > 1)
    print(f"字頭 {len(records)} / 字音 {readings} / 多音字 {poly} / 带注释 {noted}")
    print(f"s2t {len(variants['s2t'])} 條、t2s {len(variants['t2s'])} 條")
    print(f"xian.json {len(records)} 條；variants.json 已寫入 {OUT}")


if __name__ == "__main__":
    main()
