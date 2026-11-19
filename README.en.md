[简体中文](README.md) ｜ [繁體中文](README.zh-Hant.md) ｜ **English** ｜ [日本語](README.ja.md)

# Xi'an Dialect Pronunciation Lookup · xinganhua-ziyencaxin

> Type Chinese characters (simplified or traditional, up to 30 at a time) and see every reading they have in the Xi'an dialect (Guanzhong group): **Xi'an pinyin**, **IPA**, **tone**, and the dictionary's own notes. The interface comes in Simplified Chinese, Traditional Chinese, English and Japanese, chosen automatically from your system language and region.

- **Live site**: <https://siqyin.github.io/xinganhua-ziyencaxin/>
- **Character table**: 3,345 characters / 3,648 readings / 275 polyphonic / 102 with notes
- **Languages**: 简体中文 · 繁體中文 · English · 日本語 (automatic + manual)
- **Colours**: black `#000000` (Qin) · white `#FFFFFF` · crimson `#9F363A` (Han)
- **Font**: a subset of LXGW WenKai, self-hosted, no CDN

---

## Contents

1. [The Xi'an pinyin scheme](#s1)
2. [What this site is](#s2)
3. [Query rules](#s3)
4. [How to read a result](#s4)
5. [Language and automatic detection](#s5)
6. [The phonology pop-up](#s6)
7. [Where the data comes from](#s7)
8. [Colours and font](#s8)
9. [Directory layout](#s9)
10. [Local preview](#s10)
11. [Rebuilding](#s11)
12. [Deployment](#s12)
13. [Data notes and TODO](#s13)
14. [Data and credits](#s14)
15. [License](#s15)

---

<a id="s1"></a>

## 1. The Xi'an pinyin scheme

Every reading on this site is written in **Xi'an pinyin**. A syllable is initial + final + tone digit, e.g. `ba1` 巴, `bfeng4` 中, `jyuen1` 軍:

- **26 initials** (including the zero initial): `b p m f v bf pf d t n l z c s j q x zh ch sh r g k h ng`
- **40 finals**: 15 open / 10 i-medial / 9 u-medial / 6 ü-medial
- **Four tones**: Yinping 21, Yangping 24, Shangsheng 53, Qusheng 44; the entering tone has merged into these four
- **The tone digit follows the syllable** with no space: `bfeng4` 中, `jyuen1` 軍
- **Syllable boundaries use an apostrophe**: `xi'ngan1` 西安 (otherwise it would split into xin 心 + gan 干)

The four figures below cover the whole scheme. They are the same figures used in the input-method repository [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa), one set per language, identical in content:

![Xi'an initials: 26](figures/onsets.en.svg)

![Xi'an finals: 40](figures/rhymes.en.svg)

![The four Xi'an tones](figures/tones.en.svg)

![Syllable structure: initial + final + tone](figures/syllable.en.svg)

For the full description — distribution rules for initials and finals, orthographic details, a point-by-point comparison with Mandarin pinyin, and the allowed short spellings — see the input-method repository's [README](https://github.com/SiqYin/xinganhua-fuvufa) ([简体](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.md) / [繁體](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.zh-Hant.md) / [English](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.en.md) / [日本語](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.ja.md)).

---

<a id="s2"></a>

## 2. What this site is

A self-contained static page: no backend, no database, no requests beyond its own JSON and fonts. It lays out **all** the readings a character has in the Xi'an dialect.

The layout has five layers, all built from black, white and crimson: warm paper background → pale card → white reading block → crimson accents (seal, buttons, tone digits, notes) → ink-black footer.

---

<a id="s3"></a>

## 3. Query rules

| Rule | Behaviour |
|---|---|
| Simplified / traditional | Simplified input is first folded to the dictionary's traditional headword (`鹅`→`鵝`, `边`→`邊`); traditional input matches directly |
| Length | Up to 30 characters at a time; beyond that the page reports the actual count and shows nothing |
| Duplicates | Repeated characters are looked up once; mixed simplified/traditional input (e.g. 「鹅着軍」) expands each |
| Non-Chinese | Letters, digits and symbols are filtered out; if nothing is left, the page says so (no pinyin reverse lookup here) |
| Not in the table | A character missing from the dictionary gets a "not found" card instead of silently disappearing |
| Sharing | The query is written to the address bar as `?q=…`, so the link reproduces the result |

---

<a id="s4"></a>

## 4. How to read a result

One card per character: the large glyph and its simplified form on the left, the readings listed on the right.

| Position | Content | Example |
|---|---|---|
| Pinyin | full spelling + tone digit (digit in crimson) | `bfeng4` |
| IPA | IPA with the tone value as a superscript | `[pfã⁴⁴]` |
| Tone | tone name + value (English UI: Yinping / Yangping / Shangsheng / Qusheng; Japanese UI: 陰平 / 陽平 / 上声 / 去声) | 去声 44 |
| Note | the `{}` gloss carried by the source table; `白讀／文讀` marked separately | 释 白读, 西~, 北~ |

Tone digits:

| Digit | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Name | Yinping | Yangping | Shangsheng | Qusheng |
| Value | 21 | 24 | 53 | 44 |
| Example | `tian1` 天 | `nian2` 年 | `xiao3` 小 | `qu4` 去 |

Polyphonic characters are ordered Yinping → Yangping → Shangsheng → Qusheng; `着`, for instance, has five readings: `zhao1` / `zhe1` / `bfuo2` / `pfuo2` / `zhao2`.

---

<a id="s5"></a>

## 5. Language and automatic detection

The top-right corner lets you pick **简 / 繁 / 日 / EN**; the choice is stored locally (`localStorage`). On a first visit the language is decided in this order:

| Priority | Signal | Result |
|---|---|---|
| 1 | Manual choice (including `?lang=hans｜hant｜ja｜en`) | used as is |
| 2 | System / browser language (**Chinese variants and Japanese only**) | `zh-Hant`, `zh-TW/HK/MO` → Traditional; other `zh-*` → Simplified; `ja-*` → Japanese; any other system language (`en-*`, `ko-*`, …) does not decide and falls through |
| 3 | IP region | Japan → Japanese; US, UK, Canada, Australia, New Zealand, France, Germany, Korea → English; Hong Kong, Macao, Taiwan → Traditional; everything else → Simplified |
| 4 | Fallback | Simplified |

In other words, **a Chinese or Japanese system language outranks the IP**: a Traditional Chinese system stays Traditional even from mainland China, and a Japanese system stays Japanese even from the US. Other system languages (English, Korean, …) do not decide the UI language and leave it to the IP — so "English system + Japanese IP" shows Japanese, not English.

> Manual choice and `?lang=` win over everything, and the manual choice is stored in `localStorage`. If you once clicked EN and the address bar still has `?lang=en`, the page will stay English; open `?lang=auto` once to clear the manual choice and re-detect.

Implementation notes:

- Geolocation uses `https://api.country.is/`, falling back to Cloudflare's `/cdn-cgi/trace`, with a 1.5 s timeout; if both fail the page uses Simplified
- Local previews (`localhost` / `127.0.0.1` / `file:`) and search-engine crawlers skip detection and stay Simplified, so development is not steered by the network and crawlers do not index the English version
- Debugging: `?lang=auto` clears the manual choice and re-detects; `?lang=debug` shows the decision and its reason in the page header (`url` / `manual` / `system` / `ip` / `offline`)
- The four text packs live in `data/i18n.json`; Traditional is converted from Simplified with OpenCC, never written by hand

---

<a id="s6"></a>

## 6. The phonology pop-up

The "Xi'an phonology & the input scheme" strip below the search area opens a pop-up (close with Esc or a click on the backdrop). Its content comes from the input-method repository's README:

- the 26 initials (spelling / IPA / example)
- the 40 finals, grouped by the four classes (open, i-medial, u-medial, ü-medial)
- the four tones and their values
- **differences from Mandarin pinyin**: identical items, nasalised finals with the same letters, a spelling-difference table (`in→ien`, `ong→uong`, `ü→yu`…), the initials and finals Xi'an has extra, characters whose initial does not match, and same digit position with different pitch
- the pop-up text follows the UI language (Simplified / Traditional / English / Japanese)

---

<a id="s7"></a>

## 7. Where the data comes from

```
MCPDict Xi'an table (IPA)
        │  tools/ipa2pinyin.mjs (input-method repo)
        ▼
   character / pinyin / IPA / notes  →  data/source.tsv
        │  tools/build_data.py (+ OpenCC simplified↔traditional tables)
        ▼
   data/xian.json (character → readings)
   data/variants.json (simplified→traditional, traditional→simplified)
```

| Item | Count |
|---|---|
| Characters | 3,345 |
| Readings | 3,648 (one reading per line) |
| Polyphonic characters | 275 |
| With notes | 102 |
| Toneless syllables | 392 |

The simplified/traditional mapping uses OpenCC's `STCharacters.txt` / `TSCharacters.txt`, downloaded on demand at build time and not distributed with the repository.

---

<a id="s8"></a>

## 8. Colours and font

| Colour | Value | Use |
|---|---|---|
| Black | `#000000` | body text, glyphs, footer background — the Qin colour |
| White | `#FFFFFF` | cards and reading blocks, input box — the "paper" of the three |
| Crimson | `#9F363A` | seal, buttons, card edge, footer emphasis, tone digits, IPA superscript, note rule — the Han colour |

Two neutral layers sit between black and white (warm paper `#F4EEE9` for the page, pale card `#FBF7F4`); they add no extra hue.

The font is a subset of [LXGW WenKai](https://github.com/lxgw/LxgwWenKai) (LXGW WenKai Regular, OFL): `fonts/lxgw-wenkai.woff2`, containing only the glyphs the page actually uses (characters, notes, pinyin, IPA and the four UI languages — about 4,900 glyphs / 1.2 MB). See `fonts/OFL.txt` for the licence.

---

<a id="s9"></a>

## 9. Directory layout

```
index.html                    single page: styles, lookup logic, i18n and the pop-up
README.zh-Hant.md             Traditional Chinese README (OpenCC output)
README.en.md / README.ja.md   English and Japanese READMEs
data/source.tsv               source table: character / pinyin / IPA[tone] / notes
data/xian.json                front-end data: character → readings
data/variants.json            simplified↔traditional maps: s2t, t2s (for the secondary glyph)
data/i18n.json                four text packs + phonology tables (hans / hant / en / ja)
figures/                      scheme figures: four diagrams × four languages (same set as the input repo)
fonts/lxgw-wenkai.woff2       LXGW WenKai subset
fonts/OFL.txt                 font licence
tools/build_data.py           source table → JSON (downloads OpenCC tables if missing)
tools/build_i18n.py           Simplified text → Traditional (OpenCC) + English + Japanese
tools/i18n.src.json           source text packs (hans / en / ja; Traditional is generated)
tools/make_font.py            font subsetting (WOFF2)
.github/workflows/static.yml  publish to GitHub Pages on push to main
```

---

<a id="s10"></a>

## 10. Local preview

The page reads JSON with `fetch`, so double-clicking the HTML will fail. Serve it:

```sh
python -m http.server 8765
# open http://127.0.0.1:8765/
```

---

<a id="s11"></a>

## 11. Rebuilding

```sh
python tools/build_data.py          # data/xian.json, data/variants.json
python tools/build_i18n.py          # data/i18n.json (Traditional via OpenCC)
python tools/make_font.py           # font subset
```

`make_font.py` reads `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf` by default; pass a path or set `LXGW_TTF`:

```sh
python tools/make_font.py /path/to/LXGWWenKai-Regular.ttf
```

After changing text in `index.html`, anything in `data/*.json`, or the data itself, rerun `make_font.py`; otherwise new glyphs (especially kana and Japanese-specific kanji) fall back to system fonts.

---

<a id="s12"></a>

## 12. Deployment

Pushing to `main` triggers GitHub Actions (Settings → Pages → Source: GitHub Actions). The workflow copies `index.html`, `data/xian.json`, `data/variants.json`, `data/i18n.json`, `fonts/*.woff2` and the OFL into `_site`; the source table and build scripts are not published.

---

<a id="s13"></a>

## 13. Data notes and TODO

- Glyphs are traditional (as in the MCPDict source), with the simplified form shown alongside on each card for comparison
- Three syllables in the source have a sound but no character (`zou2`, `tai3`, `sao2`) and are not searchable
- If a reading disagrees with your own dialect, `data/source.tsv` is the authority; edit it and rerun the build
- TODO: reverse lookup by pinyin/IPA, query by tone, paginated browsing of the character table

---

<a id="s14"></a>

## 14. Data and credits

- [osfans/MCPDict](https://github.com/osfans/MCPDict) (`tools/tables/data/西安.tsv`) — reading data
- [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) — the Xi'an pinyin scheme, transliteration script, phonology notes and the four-language figures
- [OpenCC](https://github.com/BYVoid/OpenCC) — simplified/traditional tables
- [LXGW WenKai](https://github.com/lxgw/LxgwWenKai) — CJK font (OFL)
- [wugniu_zyinzozin](https://github.com/SiqYin/wugniu_zyinzozin) — reference for the site's approach, language detection and pop-up layout

---

<a id="s15"></a>

## 15. License

The page and build scripts may be used, modified and redistributed freely. The reading data comes from MCPDict and the font from LXGW WenKai; follow their respective terms.

---

## Note

The Simplified Chinese version is the source; the Traditional version is converted from it with OpenCC, and the English and Japanese versions are translations. All four are meant to be identical; if they diverge, the Simplified version wins. This document was written and translated with AI assistance.
