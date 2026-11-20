[简体中文](README.md) ｜ [繁體中文](README.zh-Hant.md) ｜ [English](README.en.md) ｜ **日本語**

# 西安方言 字音検索 · xinganhua-ziyencaxin

> 漢字（簡体字・繁体字のどちらでも、一度に最大 30 字）を入力すると、西安方言の**城区音**と**南郊音**、二系統の読み方が出ます：**西安方言ピンイン**、**国際音声記号（IPA）**、**声調**、そして原表の注記。UI は簡体中文・繁體中文・English・日本語の四言語で、システム言語と接続地域から自動判定します。

- **公開サイト**：<https://siqyin.github.io/xinganhua-ziyencaxin/>
- **字表**：城区字頭 3,345 ／ 城区音 3,648 件・南郊音 4,594 件（南郊字頭 4,065、渭南のみの 720 字を含む）
- **言語**：簡体中文 · 繁體中文 · English · 日本語（自動判定＋手動選択）
- **配色**：黒 `#000000`（秦）· 白 `#FFFFFF` · 緋 `#9F363A`（漢）
- **フォント**：霞鹜文楷のサブセットを自前配信（CDN 不使用）

---

## 目次

1. [西安方言ピンインの方案](#s1)
2. [このサイトについて](#s2)
3. [検索の規則](#s3)
4. [結果の読み方](#s4)
5. [音韻と入力方案のポップアップ](#s5)
6. [データの出所](#s6)
7. [配色とフォント](#s7)
8. [ディレクトリ構成](#s8)
9. [ローカルで見る](#s9)
10. [再生成](#s10)
11. [デプロイ](#s11)
12. [データの注意と今後](#s12)
13. [データと謝辞](#s13)
14. [ライセンス](#s14)

---

<a id="s1"></a>

## 1. 西安方言ピンインの方案

本サイトの読みはすべて**西安方言ピンイン**で書かれ、城区音・南郊音それぞれ一套です。1 音節は「声母＋韻母＋声調番号」で、たとえば `ba1` 巴、`jyuen1` 軍；`bfeng4` 中は城区音、南郊音では `zuong4`：

- **声母**：両系統に共通する 24 個（零声母を含む）＋城区音だけの `bf`・`pf`（計 26 個）、南郊音だけの `rh`（計 25 個）：`b p m f v bf pf d t n l z c s rh j q x zh ch sh r g k h ng`
- **韻母**：共通する 38 個（開 15 ／ 斉 8 ／ 合 9 ／ 撮 6）＋城区音だけの `uu`・`iai`（計 40 個：開 16 ／ 斉 9 ／ 合 9 ／ 撮 6）
- **四声**：陰平 21、陽平 24、上声 53、去声 44。入声はすでにこの四声に統合
- **声調番号は音節の直後**に、空白を入れずに置く：`bfeng4` 中、`jyuen1` 軍
- **音節の境界は撇号（アポストロフィ）**：`xi'ngan1` 西安（そのまま書くと xin 心 ＋ gan 干 に切られる）
- **簡拼**：入力側では `in / ing / iu / ui / un / ung / yun / yung` が使えます（それぞれ `ien / ieng / iou / uei / uen / uong / yuen / yuong` に対応。零声母は `yuen`・`yuong` のみ）。声調番号は入力しません。
- **ピンインからの逆引き**：音節を 1 つ入力（全拼／簡拼、声調番号ありなし）すると、その読みを持つ字を検索できます。ページには**全拼／簡拼の表示切替**があり、簡拼に切り替えるとカードの注音が略式綴りになります（音声記号は変わりません）。

以下の五枚で方案の全体が分かります。入力法リポジトリ [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) と同じ図を言語ごとに用意したもので、内容は各言語版で一致しています：

![西安方言の声母（城区音 26；南郊音 25——rh あり、bf・pf なし）](figures/onsets.ja.svg)

![西安方言の韻母（城区音 40；南郊音 38、uu・iai なし）](figures/rhymes.ja.svg)

![西安方言の四声](figures/tones.ja.svg)

西安方言の連続変調は主に前の字が変わるもので、二種類あります。二つの字が続けてともに一声（陰平）21-21 のとき、前の一声の字は二声（陽平）に変わって 24-21 になります。二つの字が続けてともに三声（上声）53-53 のとき、前の三声の字は一声（陰平）に変わって 21-53 になります。

![音節の構造：声母＋韻母＋声調番号](figures/syllable.ja.svg)

![入力側の略式綴り（8 つのルール）](figures/abbrev.ja.svg)

![南郊音の変体](figures/variant.ja.svg)

**南郊音の変体**：南郊音の z・c・s・rh の四組の声母が u と結合するとき、zh・ch・sh・r のそり舌の変体もあります。また sh と u が結合する場合（shu）には f の変体もあります。これらの変体は城区音が bf・pf・f・v と読む字にのみ付けます。たとえば「水」の南郊音は `suei3` で、変体 `shuei3`・`fei3` があります。変体は基本の読みと同じ声調で、字表では別の行として「変体」と記します。


### 城区音と南郊音

西安方言は一様ではなく、当サイトは二系統の読みを収録しています：

- **城区音**：西安城内地の話しことば。
- **南郊音**：西安南部（高新・小寨・曲江一帯）の話しことば。平舌音・そり舌音の分布は**渭南型**で、声母 25 個（`rh` あり、`bf`・`pf` なし）、韻母 38 個（`uu`・`iai` なし）、声調は同じ四声です。

| 項目 | 城区音 | 南郊音 |
|---|---|---|
| 声母 | 26（`bf`・`pf` を含む） | 25（`rh` を含み、`bf`・`pf` なし） |
| 韻母 | 40（`uu`・`iai` を含む） | 38（`uu`・`iai` なし） |
| rh | 入 `vu1`、若 `vo1` | `rhu1`、`rhuo1` |
| 知系合口 | 豬 `bfu1`、春 `pfen1` | `zu1`、`cuen1` |
| 書母合口 | 書 `fu1`、水 `fei3` | `su1`、`suei3` |
| 遇摂一等 | 都 `du1`、粗 `cu1` | `dou1`、`cou1` |
| 声調 | 陰平 21・陽平 24・上声 53・去声 44 | 城区音と同じ |

3,345 字のうち、両系統で読みが完全に同じなのは 2,971 字、異なるのは 374 字。検索結果では 1 字ごとに二系統の読みを並べて表示します。

声母・韻母の分布規則、正書法の細則、普通話ピンインとの項目別の対照、使える簡拼まで含む完全な説明は、入力法リポジトリの [README](https://github.com/SiqYin/xinganhua-fuvufa)（[简体](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.md) ／ [繁體](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.zh-Hant.md) ／ [English](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.en.md) ／ [日本語](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.ja.md)）を参照してください。

---

<a id="s2"></a>

## 2. このサイトについて

外部に依存しない静的ページです。サーバーもデータベースもなく、ページ自身の JSON とフォント以外にリクエストを出しません。1 字が西安方言に持つ**すべての**読みを並べて見せます。
検索欄の下には「西安のアクセント分区」という短い解説と模式図があります。明城壁の内側の城区を中心に、東・西・南・北の四郊が広がり、城区・北郊・西郊が西安型、南郊・東郊が渭南型に属します。北東側は城壁の東辺から北へ引いた直線、南西側は城壁の南西角から南西へ引いた斜線が境です。図は方位の模式図で、行政界ではありません。

版面は五層で、すべて黒・白・緋の濃淡でできています：暖かい紙の下地 → 淡いカード → 白い読みブロック → 緋の強調（印章・ボタン・声調番号・注記）→ 墨色のフッター。

---

<a id="s3"></a>

## 3. 検索の規則

| 規則 | 動作 |
|---|---|
| 簡体・繁体 | 簡体字はまず字表の繁体字字頭に折り畳んでから検索（`鹅`→`鵝`、`边`→`邊`）。繁体字はそのまま一致 |
| 字数 | 一度に最大 30 字。超えると実際の字数を知らせ、結果は出さない |
| 重複 | 同じ字は 1 回だけ検索。簡体・繁体の混在（例「鹅着軍」）はそれぞれ展開 |
| 漢字以外 | 字母・数字・記号は除く。漢字が 1 字も残らない場合はその旨を表示（本ページではピンインからの逆引きはしない） |
| 未収録 | 字表にない字は「未収録」カードを出す。黙って消えることはない |
| 共有 | 検索内容をアドレス欄に `?q=…` として書き出すので、リンクをコピーすれば結果が再現する |

---

<a id="s4"></a>

## 4. 結果の読み方

1 字につき 1 枚のカード。左に大きな字と簡体形、右に**城区音**と**南郊音**の二列を並べ、それぞれの読みを列挙します。南郊音は又読を統合することが多いため、二列の件数は一致しないことがあります。

| 位置 | 内容 | 例 |
|---|---|---|
| ピンイン | 全拼＋声調番号（城区音は緋色、南郊音は青） | `bfeng4` ／ `zuong4` |
| 音声記号 | 国際音声記号＋調値の上付き。左欄のピンインと一対一（城区音は赤、南郊音は青） | `[pfəɣ̃⁴⁴]` ／ `[ʦuoɣ̃⁴⁴]` |
| 声調 | 調名＋調値（English UI は Yinping / Yangping / Shangsheng / Qusheng、日本語 UI は 陰平 / 陽平 / 上声 / 去声） | 去声 44 |
| 注記 | 原表が持つ `{}` の注釈。`白讀／文讀` は別途表示 | 释 白读, 西~, 北~ |

声調番号の対応：

| 番号 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 調名 | 陰平 | 陽平 | 上声 | 去声 |
| 調値 | 21 | 24 | 53 | 44 |
| 例 | `tian1` 天 | `nian2` 年 | `xiao3` 小 | `qu4` 去 |

多音字は陰平 → 陽平 → 上声 → 去声の順に並びます。たとえば `着` は五読：`zhao1` / `zhe1` / `bfuo2` / `pfuo2` / `zhao2`。

---

<a id="s5"></a>

## 5. 音韻と入力方案のポップアップ

ページ下部の「西安方言の音韻と入力方案」は全体がクリックできる入口で、開くとポップアップになります（Esc または背景のクリックで閉じる）。内容は入力法リポジトリの README によります：

- 声母 27 枠（共通 24 ＋ 城区特有 `bf`・`pf` ＋ 南郊特有 `rh`、破線枠で表示）
- 韻母 40 枠、開斉合撮の四呼で分類。`uu`・`iai` は城区音特有です
- 四声と調値（両系統で同じ）
- **城区音と南郊音の違い**：声母・韻母の数、`rh`、`bf`／`pf` と `uu`／`iai` の対応、その他の規則的な違い
- **普通話ピンインとの異同**：声母は完全に一致、鼻母音の韻母、城区音だけにある声母・韻母（南郊音には `rh` がある）、声母が対応しない字、番号の位置は同じで調値が違うこと
- ポップアップ内のテキストも UI の言語に追随（簡 / 繁 / 英 / 日）

---

<a id="s6"></a>

## 6. データの出所

西安話の城区音は、城区音を記録した西安話の音声資料によります。南郊音は西安話・渭南話・臨潼話・華県話などの音声資料を参照して一字ずつ定めたものです。誤りがあればご指摘いただければ幸いです。

- [西安話の音声資料](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E8%A5%BF%E5%AE%89.tsv)
- [渭南話の音声資料](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E6%B8%AD%E5%8D%97.tsv)
- [臨潼話の音声資料](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E4%B8%B4%E6%BD%BC%E6%96%B9%E8%A8%80%E8%AF%AD%E9%9F%B3%E7%A0%94%E7%A9%B6.tsv)
- [華県話の音声資料](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E5%8D%8E%E5%8E%BF.tsv)

---

<a id="s7"></a>

## 7. 配色とフォント

| 色 | 値 | 用途 |
|---|---|---|
| 黒 | `#000000` | 本文、字頭、フッターの下地。秦の色 |
| 白 | `#FFFFFF` | カードと読みブロック、入力欄。三色のうちの「紙」 |
| 緋 | `#9F363A` | 印章、ボタン、カードの左辺、フッターの強調、声調番号、音声記号の上付き、注記の罫線。漢の色 |

黒と白の間には中性の二層（暖かい紙 `#F4EEE9` の下地、淡いカード `#FBF7F4`）を置き、色相は増やしていません。

フォントは [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（LXGW WenKai Regular、OFL）のサブセット `fonts/lxgw-wenkai.woff2` で、ページが実際に使う字形だけを含みます（字頭、注記、ピンイン、音声記号、四言語の UI テキストで約 4,900 字形 / 1.2 MB）。ライセンスは `fonts/OFL.txt`。

---

<a id="s8"></a>

## 8. ディレクトリ構成

```
index.html                    単一ページ：スタイル、検索ロジック、i18n、ポップアップ
README.zh-Hant.md             繁体の説明（OpenCC 変換）
README.en.md / README.ja.md   英語・日本語の説明
data/source.tsv               字音の原表：字 / ピンイン / IPA[調名] / 注記
data/xian.json                フロント用データ：字頭 → 城区音の読みの配列
data/nanjiao.json             フロント用データ：字頭 → 南郊音の読みの配列
data/variants.json            簡繁の対応：s2t（簡→繁）、t2s（繁→簡、併記用）
data/i18n.json                四言語のテキスト＋音韻表データ（簡 / 繁 / 英 / 日）
figures/                      方案の図：五枚 × 四言語（入力法リポジトリと同じセット）
fonts/lxgw-wenkai.woff2       霞鹜文楷のサブセット
fonts/OFL.txt                 フォントのライセンス
tools/build_data.py           原表 → JSON（OpenCC の表がなければ自動取得）
tools/build_nanjiao_json.py   南郊音の字表 → data/nanjiao.json
tools/build_i18n.py           簡体のテキスト → 繁体（OpenCC）＋英・日
tools/i18n.src.json           四言語テキストの原本（簡 / 英 / 日。繁体はスクリプト生成）
tools/make_font.py            フォントのサブセット化（WOFF2）
.github/workflows/static.yml  main への push で GitHub Pages に公開
```

---

<a id="s9"></a>

## 9. ローカルで見る

ページは `fetch` で JSON を読むため、HTML を直接開くと失敗します。静的サーバーを立ててください：

```sh
python -m http.server 8765
# http://127.0.0.1:8765/ を開く
```

---

<a id="s10"></a>

## 10. 再生成

```sh
python tools/build_data.py          # data/xian.json、data/variants.json
python tools/build_nanjiao_json.py  # data/nanjiao.json（南郊音）
python tools/build_i18n.py          # data/i18n.json（繁体は OpenCC）
python tools/make_font.py           # フォントのサブセット
```

`make_font.py` は既定で `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf` を読みます。引数か環境変数 `LXGW_TTF` でも指定できます：

```sh
python tools/make_font.py /path/to/LXGWWenKai-Regular.ttf
```

`index.html` のテキスト、`data/*.json`、データを変えたら、必ず `make_font.py` を走らせてください。そうしないと新しい字（とくに仮名と日本語固有の漢字）がシステムフォントに落ちます。

---

<a id="s11"></a>

## 11. デプロイ

`main` に push すると GitHub Actions が公開します（Settings → Pages → Source で GitHub Actions を選択）。ワークフローは `index.html`、`data/xian.json`、`data/nanjiao.json`、`data/variants.json`、`data/i18n.json`、`fonts/*.woff2`、OFL を `_site` にコピーし、原表とビルドスクリプトは公開しません。

---

<a id="s12"></a>

## 12. データの注意と今後

- 用字は繁体（MCPDict の原表がそうであるため）。カードには簡体形も併記して対照できるようにしています
- 南郊音は西安南郊音の逐字裁定表（2026-11-20）と両系統共通の読みから折り出したもの。拘束条件は「`bf`・`pf` なし（城区特有）、`uu`・`iai` なし（城区特有）」で、`rh`（城区音は v）が加わります。`bf→z`、`pf→c`（韻母に u 介音が加わる）、`uu→e`、`iai→ie`。一部の字は校訂により上書き：癌は `ngai2` のみ、涯 `ya2`、後は `hou4` のみ、芍 `shuo2`
- 原表には音だけで字がない音節が 3 つ（`zou2`、`tai3`、`sao2`）あり、検索には出しません
- ピンインや音声記号が自分の方言と違う場合は `data/source.tsv` が正です。直してビルドし直してください
- 今後：音声記号からの逆引き、声調による検索、字表のページ送り（ピンイン逆引きと全拼／簡拼の表示切替は公開済み）

---

<a id="s13"></a>

## 13. データと謝辞

- [西安話データ表](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E8%A5%BF%E5%AE%89.tsv)、[渭南話データ表](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E6%B8%AD%E5%8D%97.tsv)、[臨潼話データ表](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E4%B8%B4%E6%BD%BC%E6%96%B9%E8%A8%80%E8%AF%AD%E9%9F%B3%E7%A0%94%E7%A9%B6.tsv)、[華県データ表](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E5%8D%8E%E5%8E%BF.tsv)——いずれも [osfans/MCPDict](https://github.com/osfans/MCPDict) によるもの。西安話データ表は城区音の字音データ源（国際音声記号）、渭南・臨潼・華県の三表は南郊音の整理時の参照資料
- **南郊話の音档**に既成の字表はない：西安話・渭南話・臨潼話・華県話などのデータ表を下敷きに、南郊音・東郊音の平翘舌（平舌／翘舌声母）の帰属をめぐる知乎（Zhihu）の議論を参照し、筆者自身と家族の発音で一字ずつ照合して整理したものであるため、**参考程度にとどめてください**
- [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) —— 西安方言ピンインの方案、転写スクリプト、音韻の説明、四言語の図
- [OpenCC](https://github.com/BYVoid/OpenCC) —— 簡繁の対照表
- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai) —— 中国語フォント（OFL）
- [wugniu_zyinzozin](https://github.com/SiqYin/wugniu_zyinzozin) —— サイトの作り方、言語判定、ポップアップ版面の参照元

---

<a id="s14"></a>

## 14. ライセンス

ページとビルドスクリプトは自由に使用・改変・再配布できます。字音データは MCPDict、フォントは霞鹜文楷に由来するため、それぞれのプロジェクトの説明に従ってください。

---

## 注記

簡体中文版が原文で、繁體中文版は OpenCC による変換、English 版と日本語版は対応する翻訳です。四版は内容を同一に保つ想定で、相違があれば簡体版を正とします。本文は AI の補助を受けて作成・翻訳しました。
