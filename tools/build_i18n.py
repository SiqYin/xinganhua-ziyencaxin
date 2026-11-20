#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成 data/i18n.json：简体（源）→ 繁体（本地 OpenCC 字表转换）+ 英文 + 日文，附音系表数据。

用法：python tools/build_i18n.py
源：tools/i18n.src.json（hans / en / ja 三套文案；繁体由 tools/opencc/TSCharacters.txt 从简体转出）

繁体不引外挂 opencc 库：词表就用仓库里带的那份 OpenCC TSCharacters（Apache-2.0），
逐字查表即可——与输入法侧 Rime 内置的 opencc 数据同源，不额外装东西。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "i18n.src.json"
OUT = ROOT / "data" / "i18n.json"
TS_CHARS = ROOT / "tools" / "opencc" / "STCharacters.txt"


class S2T:
    """逐字繁化：读 OpenCC 的 STCharacters 表（简→繁），取每条的第一个候选（与 OpenCC s2t 一致）。

    注意别用 TSCharacters.txt：那是繁→简，方向相反。
    另外逐字转换会在少数词上出错（如「若干」被转成「若幹」），这类例外在 EXCEPTIONS 里回改。
    """

    # 逐字转换与 OpenCC 的差异只在少数词上，按词回改（左为逐字结果，右为 OpenCC s2t 结果）
    EXCEPTIONS = {
        "若干": "若干",     # 不取「若幹」
        "並入": "併入",     # 併入（合併），非「並」
        "分布": "分佈",     # 分佈
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

    def conv_word_rev(self, word):
        return "".join(self.table.get(ch, ch) for ch in word)


# 声母：写法 / IPA / 例字 / 例字读音（例字取字表的繁体字形）
INITIALS = [
    ["b", "p", "巴", "ba1"], ["p", "pʰ", "朋", "peng2"], ["m", "m", "明", "mieng2"],
    ["f", "f", "夫", "fu1"], ["v", "v", "文", "ven2"],
    ["bf", "pf", "中", "bfeng4", 1], ["pf", "pfʰ", "窗", "pfang1", 1],
    ["d", "t", "的", "di1"], ["t", "tʰ", "他", "ta1"], ["n", "n", "你", "ni3"], ["l", "l", "立", "li1"],
    ["z", "ʦ", "字", "zi4"], ["c", "ʦʰ", "茶", "ca2"], ["s", "s", "山", "san1"], ["rh", "z", "入", "vu1", 2],
    ["j", "ʨ", "家", "jia1"], ["q", "ʨʰ", "妻", "qi1"], ["x", "ɕ", "西", "xi1"],
    ["zh", "tʂ", "站", "zan4"], ["ch", "tʂʰ", "吃", "chi1"], ["sh", "ʂ", "上", "shang4"], ["r", "ʐ", "人", "ren2"],
    ["g", "k", "狗", "gou3"], ["k", "kʰ", "口", "kou3"], ["h", "x", "花", "hua1"],
    ["ng", "ŋ", "安", "ngan1"], ["Ø", "—", "衣", "yi1"],
]

# 韵母：四呼分组，写法 / IPA / 例字 / 读音
FINALS = [
    [["a", "a", "巴", "ba1"], ["o", "o", "若", "vo1"], ["er", "ɚ", "兒", "er2"], ["e", "ɤ", "鵝", "nge2"],
     ["uu", "ɯ", "胳", "guu1", 1], ["i", "ɿ", "字", "zi4"], ["i", "ʅ", "吃", "chi1"], ["ai", "ai", "菜", "cai4"],
     ["ao", "au", "到", "dao4"], ["an", "ã", "山", "san1"], ["ei", "ei", "水", "fei3"], ["en", "ẽ", "人", "ren2"],
     ["ou", "ɤu", "狗", "gou3"], ["ang", "ɑɣ̃", "上", "shang4"], ["eng", "əɣ̃", "中", "bfeng4"]],
    [["i", "i", "衣", "yi1"], ["ia", "ia", "家", "jia1"], ["ie", "iɛ", "姐", "jie3"], ["iai", "iai", "皆", "jiai1", 1],
     ["iao", "iau", "小", "xiao3"], ["ian", "iã", "煙", "yan1"], ["ien", "iẽ", "音", "yen1"], ["ieng", "iɣ̃", "英", "yeng1"],
     ["iou", "iɤu", "有", "you3"], ["iang", "iɑɣ̃", "央", "yang1"]],
    [["u", "u", "烏", "wu1"], ["ua", "ua", "花", "hua1"], ["uo", "uɤ", "窩", "wo1"], ["uai", "uai", "快", "kuai4"],
     ["uan", "uã", "彎", "wan1"], ["uei", "uei", "回", "huei2"], ["uen", "uẽ", "溫", "wen1"],
     ["uong", "uoɣ̃", "翁", "wong1"], ["uang", "uɑɣ̃", "汪", "wang1"]],
    [["yu", "y", "魚", "yu2"], ["yue", "yɛ", "月", "yue1"], ["yuo", "yɤ", "樂", "yuo1"], ["yua", "ya", "髽", "zyua4", 2],
     ["yuan", "yã", "元", "yuan2"], ["yuen", "yẽ", "勻", "yuen2"], ["yuong", "yoɣ̃", "容", "yuong2"]],
]


# 声调：调号 / 调值 / 例字 / 读音
TONES = [["1", "21", "天", "tian1"], ["2", "24", "年", "nian2"], ["3", "53", "小", "xiao3"], ["4", "44", "去", "qi4"]]



# 南郊读音（data/nanjiao.json 由 tools/build_nanjiao_json.py 生成）
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
            "initials": with_nj(INITIALS),
            "finals": [with_nj(g) for g in FINALS],
            "tones": TONES,
        },
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    hant = out["langs"]["hant"]
    print("i18n.json 已生成：4 种语言；声母 %d（城区特有 bf、pf ＋ 南郊特有 rh）、韵母 %d（城区特有 uu、iai ＋ 南郊特有 yua）、声调 %d" % (
        len(INITIALS), sum(len(g) for g in FINALS), len(TONES)))
    print("繁体样例：", hant["h1"], "|", hant["search"], "|", hant["phon"]["initialsTitle"])
    print("日文样例：", out["langs"]["ja"]["h1"], "|", out["langs"]["ja"]["search"])


if __name__ == "__main__":
    main()
