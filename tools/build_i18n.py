#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成 data/i18n.json：简体（源）→ 繁体（OpenCC 转换）+ 英文，附音系表数据。

用法：python tools/build_i18n.py
源：tools/i18n.src.json（hans / en 两套文案）
"""
import json
from pathlib import Path

import opencc

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "i18n.src.json"
OUT = ROOT / "data" / "i18n.json"

# 声母：写法 / IPA / 例字 / 例字读音（例字取字表的繁体字形）
INITIALS = [
    ["b", "p", "巴", "ba1"], ["p", "pʰ", "朋", "peng2"], ["m", "m", "明", "mieng2"],
    ["f", "f", "夫", "fu1"], ["v", "v", "文", "ven2"],
    ["bf", "pf", "中", "bfeng4"], ["pf", "pfʰ", "窗", "pfang1"],
    ["d", "t", "的", "di1"], ["t", "tʰ", "他", "ta1"], ["n", "n", "你", "ni3"], ["l", "l", "立", "li1"],
    ["z", "ʦ", "字", "zi4"], ["c", "ʦʰ", "茶", "ca2"], ["s", "s", "山", "san1"],
    ["j", "ʨ", "家", "jia1"], ["q", "ʨʰ", "妻", "qi1"], ["x", "ɕ", "西", "xi1"],
    ["zh", "tʂ", "站", "zan4"], ["ch", "tʂʰ", "吃", "chi1"], ["sh", "ʂ", "上", "shang4"], ["r", "ʐ", "人", "ren2"],
    ["g", "k", "狗", "gou3"], ["k", "kʰ", "口", "kou3"], ["h", "x", "花", "hua1"],
    ["ng", "ŋ", "安", "ngan1"], ["Ø", "—", "衣", "yi1"],
]

# 韵母：四呼分组，写法 / IPA / 例字 / 读音
FINALS = [
    [["a", "a", "巴", "ba1"], ["o", "o", "若", "vo1"], ["er", "ɚ", "兒", "er2"], ["e", "ɤ", "鵝", "nge2"],
     ["uu", "ɯ", "胳", "guu1"], ["i", "ɿ", "字", "zi4"], ["i", "ʅ", "吃", "chi1"], ["ai", "ai", "菜", "cai4"],
     ["ao", "au", "到", "dao4"], ["an", "ã", "山", "san1"], ["ei", "ei", "水", "fei3"], ["en", "ẽ", "人", "ren2"],
     ["ou", "ɤu", "狗", "gou3"], ["ang", "ɑɣ̃", "上", "shang4"], ["eng", "əɣ̃", "中", "bfeng4"]],
    [["i", "i", "衣", "yi1"], ["ia", "ia", "家", "jia1"], ["ie", "iɛ", "姐", "jie3"], ["iai", "iai", "皆", "jiai1"],
     ["iao", "iau", "小", "xiao3"], ["ian", "iã", "煙", "yan1"], ["ien", "iẽ", "音", "yen1"], ["ieng", "iɣ̃", "英", "yeng1"],
     ["iou", "iɤu", "有", "you3"], ["iang", "iɑɣ̃", "央", "yang1"]],
    [["u", "u", "烏", "wu1"], ["ua", "ua", "花", "hua1"], ["uo", "uɤ", "窩", "wo1"], ["uai", "uai", "快", "kuai4"],
     ["uan", "uã", "彎", "wan1"], ["uei", "uei", "回", "huei2"], ["uen", "uẽ", "溫", "wen1"],
     ["uong", "uoɣ̃", "翁", "wong1"], ["uang", "uɑɣ̃", "汪", "wang1"]],
    [["yu", "y", "魚", "yu2"], ["yue", "yɛ", "月", "yue1"], ["yuo", "yɤ", "樂", "yuo1"],
     ["yuan", "yã", "元", "yuan2"], ["yuen", "yẽ", "勻", "yuen2"], ["yuong", "yoɣ̃", "容", "yuong2"]],
]

# 声调：调号 / 调值 / 例字 / 读音
TONES = [["1", "21", "天", "tian1"], ["2", "24", "年", "nian2"], ["3", "53", "小", "xiao3"], ["4", "44", "去", "qi4"]]


def convert(obj, cc):
    if isinstance(obj, str):
        return cc.convert(obj)
    if isinstance(obj, list):
        return [convert(x, cc) for x in obj]
    if isinstance(obj, dict):
        return {k: convert(v, cc) for k, v in obj.items()}
    return obj


def main() -> None:
    src = json.loads(SRC.read_text(encoding="utf-8"))
    cc = opencc.OpenCC("s2t")
    out = {
        "langs": {
            "hans": src["hans"],
            "hant": convert(src["hans"], cc),
            "en": src["en"],
        },
        "tables": {
            "initials": INITIALS,
            "finals": FINALS,
            "tones": TONES,
        },
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    hant = out["langs"]["hant"]
    print("i18n.json 已生成：3 种语言；声母 %d、韵母 %d、声调 %d" % (
        len(INITIALS), sum(len(g) for g in FINALS), len(TONES)))
    print("繁体样例：", hant["h1"], "|", hant["search"], "|", hant["phon"]["initialsTitle"])


if __name__ == "__main__":
    main()
