#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成 data/i18n.json：简体（源）→ 繁体（本地 OpenCC 字表转换）+ 英文 + 日文，附音系表数据。

用法：python tools/build_i18n.py
源：tools/i18n.src.json（hans / en / ja 三套文案；繁体由 tools/opencc/STCharacters.txt 从简体转出）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "i18n.src.json"
OUT = ROOT / "data" / "i18n.json"
TS_CHARS = ROOT / "tools" / "opencc" / "STCharacters.txt"


class S2T:
    """逐字繁化：读 OpenCC 的 STCharacters 表（简→繁），取每条的第一个候选（与 OpenCC s2t 一致）。"""

    EXCEPTIONS = {
        "若干": "若干",
        "並入": "併入",
        "分布": "分佈",
    }

    def __init__(self, path):
        self.table = {}
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            src, dst = parts[0], parts[1].split()
            if src and dst:
                self.table[src] = dst[0]

    def convert(self, text):
        out = "".join(self.table.get(ch, ch) for ch in text)
        for a, b in self.EXCEPTIONS.items():
            out = out.replace(self.conv_word(a), b)
        return out

    def conv_word(self, word):
        return "".join(self.table.get(ch, ch) for ch in word)


# 声母：严格按 7 行（唇音 / 舌尖中 / 舌根 / 舌面前 / 舌尖后 / 舌尖前 / 零声母）排列
INITIALS = [
    [["b", "p", "巴", "ba1"], ["p", "pʰ", "朋", "peng2"], ["m", "m", "明", "ming2"],
     ["bf", "pf", "中", "bfeng4", 1], ["pf", "pfʰ", "窗", "pfang1", 1],
     ["f", "f", "夫", "fu1"], ["v", "v", "文", "ven2"]],
    [["d", "t", "的", "di1"], ["t", "tʰ", "他", "ta1"], ["n", "n¹", "南", "nan2"], ["l", "l", "立", "li1"]],
    [["g", "k", "狗", "gou3"], ["k", "kʰ", "口", "kou3"], ["h", "x", "花", "hua1"], ["ng", "ŋ", "安", "ngan1"]],
    [["j", "tɕ", "家", "jia1"], ["q", "tɕʰ", "妻", "qi1"], ["x", "ɕ", "西", "xi1"]],
    [["zh", "ʈʂ", "張", "zhang1"], ["ch", "ʈʂʰ", "吃", "chi1"], ["sh", "ʂ", "上", "shang4"], ["r", "ɻ", "人", "ren2"]],
    [["z", "ts", "字", "zi4"], ["c", "tsʰ", "茶", "ca2"], ["s", "s", "山", "san1"], ["rh", "z", "入", "vu1", 2]],
    [["Ø", "—", "衣", "yi1"]],
]

# 韵母：严格按四呼分组及指定排序（开 14 / 齐 10 / 合 9 / 撮 6）
FINALS = [
    [["a", "a", "巴", "ba1"], ["e", "ɤ", "鵝", "nge2"], ["uu", "ɯ", "胳", "guu1", 1],
     ["i", "ɿ¹", "字", "zi4"], ["i", "ʅ²", "吃", "chi1"], ["ae", "æ", "菜", "cae4"],
     ["ei", "ei", "水", "fei3"], ["ao", "au", "到", "dao4"], ["ou", "ɤu", "狗", "gou3"],
     ["an", "ã", "山", "san1"], ["en", "ẽ", "人", "ren2"], ["ang", "aŋ", "上", "shang4"],
     ["eng", "əŋ", "中", "bfeng4"], ["er", "ɚ", "兒", "er2"]],
    [["i", "i", "衣", "yi1"], ["ia", "ia", "家", "jia1"], ["ie", "iɛ", "姐", "jie3"],
     ["iae", "iæ", "皆", "jiae1", 1], ["iao", "iau", "小", "xiao3"], ["iou", "iɤu", "有", "you3"],
     ["ian", "iã", "煙", "yan1"], ["ien", "iɛ̃", "音", "yen1"], ["iang", "iaŋ", "央", "yang1"],
     ["ing", "iŋ", "英", "ying1"]],
    [["u", "u", "烏", "wu1"], ["ua", "ua", "花", "hua1"], ["uo", "uɤ", "窩", "wo1"],
     ["uae", "uæ", "快", "kuae4"], ["uei", "uei", "回", "huei2"], ["uan", "uã", "彎", "wan1"],
     ["uen", "uẽ", "溫", "wen1"], ["uang", "uaŋ", "汪", "wang1"], ["uong / ung", "uɤŋ/uŋ³", "東", "duong1"]],
    [["yu", "y", "魚", "yu2"], ["yuo", "yɤ", "樂", "yuo1"], ["yue", "yɛ", "月", "yue1"],
     ["yuan", "yã", "元", "yuan2"], ["yuen", "yɛ̃", "勻", "yuen2"], ["yung", "yŋ", "容", "yung2"]],
]

# 声调：调号 / 调值 / 例字 / 读音
TONES = [["1", "31", "天", "tian1"], ["2", "24", "年", "nian2"], ["3", "53", "小", "xiao3"], ["4", "55", "去", "qi4"]]


NJ_READ = {}
_nj = ROOT / "data" / "nanjiao.json"
if _nj.exists():
    for _rec in json.loads(_nj.read_text(encoding="utf-8")):
        NJ_READ[_rec["character"]] = [x["py"] for x in _rec["readings"]]


def nj_of(char, reading):
    """例字在南郊音里的读法；与城区音相同则返回空串。"""
    rs = NJ_READ.get(char)
    if not rs or reading in rs:
        return ""
    same_tone = [x for x in rs if x[-1] == reading[-1]]
    return (same_tone or rs)[0]


def with_nj(rows):
    out = []
    for item in rows:
        it = list(item)
        it = it[:4] + [it[4] if len(it) > 4 else 0, nj_of(it[2], it[3])]
        out.append(it)
    return out


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
    cc = S2T(TS_CHARS)
    out = {
        "langs": {
            "hans": src["hans"],
            "hant": convert(src["hans"], cc),
            "en": src["en"],
            "ja": src["ja"],
        },
        "tables": {
            "initials": [with_nj(row) for row in INITIALS],
            "finals": [with_nj(g) for g in FINALS],
            "tones": TONES,
        },
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    hant = out["langs"]["hant"]
    print("i18n.json 已生成：4 种语言；声母 %d（7 行，城区特有 bf、pf ＋ 南郊特有 rh）、韵母 %d（14/10/9/6，城区特有 uu、iae）、声调 %d" % (
        sum(len(r) for r in INITIALS), sum(len(g) for g in FINALS), len(TONES)))
    print("繁体样例：", hant["h1"], "|", hant["search"], "|", hant["phon"]["initialsTitle"])
    print("日文样例：", out["langs"]["ja"]["h1"], "|", out["langs"]["ja"]["search"])


if __name__ == "__main__":
    main()
