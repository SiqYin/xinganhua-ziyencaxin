#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把南郊音字表折成站点用的 data/nanjiao.json（与 data/xian.json 同构）。

用法：python tools/build_nanjiao_json.py [南郊音字表.tsv]
默认从归档目录取 ../南郊音字表.tsv；字序沿用 data/xian.json，缺的补在后面。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "南郊音字表.tsv"
OUT = ROOT / "data" / "nanjiao.json"

VAL = {"1": "21", "2": "24", "3": "53", "4": "44", "0": "0"}
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
TONE = {"1": "阴平", "2": "阳平", "3": "上声", "4": "去声", "0": "轻声"}


def main() -> None:
    rows = {}
    for n, line in enumerate(SRC.read_text(encoding="utf-8").splitlines()):
        if not line.strip() or line.startswith("#"):
            continue
        ch, py, _t, tone_name, ipa, _ipa_tone, src, adj = line.split("\t")
        m = re.match(r"^(.*?)([0-9])$", py)
        if not m:
            continue
        body, tone = m.group(1), m.group(2)
        # 变体读音：来源列为「变体」，卡片上要标出来
        note = "变体" if src == "变体" else ""
        rows.setdefault(ch, []).append({
            "py": py, "ipa": ipa, "tone": tone_name,
            "val": VAL[tone], "val_sup": VAL[tone].translate(SUP),
            "note": note, "first": False,
        })

    order = []
    xian = ROOT / "data" / "xian.json"
    if xian.exists():
        order = [r["character"] for r in json.loads(xian.read_text(encoding="utf-8"))]

    out, seen = [], set()
    for ch in order:
        if ch in rows:
            rec = {"id": len(out) + 1, "character": ch, "readings": rows[ch]}
            rec["readings"][0]["first"] = True
            out.append(rec)
            seen.add(ch)
    for ch, rs in rows.items():
        if ch in seen:
            continue
        rec = {"id": len(out) + 1, "character": ch, "readings": rs}
        rec["readings"][0]["first"] = True
        out.append(rec)

    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"nanjiao.json：{len(out)} 字 / {sum(len(r['readings']) for r in out)} 条 → {OUT}")


if __name__ == "__main__":
    main()
