#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把霞鹜文楷 Regular 子集化成站点自托管字体（WOFF2）。

字形集 = 页面里出现过的所有字符（含 JS 文案、拼音、国际音标、注释）+ ASCII + 常用标点。
用法：python tools/make_font.py [字体路径]
默认字体路径取环境变量 LXGW_TTF，否则用下面 SRC 的默认值。
"""
import json
import os
import sys
from pathlib import Path

from fontTools import subset

ROOT = Path(__file__).resolve().parent.parent
SRC_DEFAULT = Path(r"D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf")
OUT = ROOT / "fonts" / "lxgw-wenkai.woff2"

EXTRA = (
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "　、。，．·；：？！…—～《》〈〉「」『』【】（）〔〕“”‘’"
    + "约量词个只们这那么什怎样吗呢吧啊呀哦嗯的了着过和与及或者在是有无不都很更最太又再还就才只"
    + "０１２３４５６７８９"
    + "[]{}<>|/\\-_=+*&^%$#@!?.,;:'\"()"
)


def collect_text() -> str:
    chunks = []
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    chunks.append(html)
    for name in ("xian.json", "variants.json"):
        p = ROOT / "data" / name
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8"))
    chunks.append(EXTRA)
    return "".join(chunks)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(os.environ.get("LXGW_TTF", SRC_DEFAULT))
    if not src.exists():
        raise SystemExit(f"找不到字体文件：{src}")
    text = "".join(sorted(set(collect_text())))
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.name_languages = ["*"]
    opts.notdef_outline = True
    opts.recommended_glyphs = True
    opts.drop_tables += ["DSIG"]

    font = subset.load_font(str(src), opts)
    subsetter = subset.Subsetter(options=opts)
    subsetter.populate(text=text)
    subsetter.subset(font)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    subset.save_font(font, str(OUT), opts)
    print(f"字形 {len(set(text))} 个 → {OUT.name}（{OUT.stat().st_size / 1024:.0f} KB）")


if __name__ == "__main__":
    main()
