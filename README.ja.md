[简体中文](README.md) ｜ [繁體中文](README.zh-Hant.md) ｜ [English](README.en.md) ｜ **日本語**

# 西安方言 字音検索 · xinganhua-ziyencaxin

> 漢字（簡体字・繁体字のどちらでも、一度に最大 30 字）を入力すると、西安方言（関中片）でのすべての読み方が出ます：**西安方言ピンイン**、**国際音声記号（IPA）**、**声調**、そして原表の注記。UI は簡体中文・繁體中文・English・日本語の四言語で、システム言語と接続地域から自動判定します。

- **公開サイト**：<https://siqyin.github.io/xinganhua-ziyencaxin/>
- **字表**：字頭 3,345 ／ 字音 3,648 ／ 多音字 275 ／ 注記つき 102
- **言語**：簡体中文 · 繁體中文 · English · 日本語（自動判定＋手動選択）
- **配色**：黒 `#000000`（秦）· 白 `#FFFFFF` · 緋 `#9F363A`（漢）
- **フォント**：霞鹜文楷のサブセットを自前配信（CDN 不使用）

---

## 目次

1. [西安方言ピンインの方案](#s1)
2. [このサイトについて](#s2)
3. [検索の規則](#s3)
4. [結果の読み方](#s4)
5. [言語と自動判定](#s5)
6. [音韻と入力方案のポップアップ](#s6)
7. [データの出所](#s7)
8. [配色とフォント](#s8)
9. [ディレクトリ構成](#s9)
10. [ローカルで見る](#s10)
11. [再生成](#s11)
12. [デプロイ](#s12)
13. [データの注意と今後](#s13)
14. [データと謝辞](#s14)
15. [ライセンス](#s15)

---

<a id="s1"></a>

## 1. 西安方言ピンインの方案

本サイトの読みはすべて**西安方言ピンイン**で書かれています。1 音節は「声母＋韻母＋声調番号」で、たとえば `ba1` 巴、`bfeng4` 中、`jyuen1` 軍：

- **声母 26 個**（ゼロ声母を含む）：`b p m f v bf pf d t n l z c s j q x zh ch sh r g k h ng`
- **韻母 40 個**：開 15 ／ 斉 10 ／ 合 9 ／ 撮 6
- **四声**：陰平 21、陽平 24、上声 53、去声 44。入声はすでにこの四声に統合
- **声調番号は音節の直後**に、空白を入れずに置く：`bfeng4` 中、`jyuen1` 軍
- **音節の境界は撇号（アポストロフィ）**：`xi'ngan1` 西安（そのまま書くと xin 心 ＋ gan 干 に切られる）

以下の四枚で方案の全体が分かります。入力法リポジトリ [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) と同じ図を言語ごとに用意したもので、内容は各言語版で一致しています：

![西安方言の声母 26](figures/onsets.ja.svg)

![西安方言の韻母 40](figures/rhymes.ja.svg)

![西安方言の四声](figures/tones.ja.svg)

![音節の構造：声母＋韻母＋声調番号](figures/syllable.ja.svg)

声母・韻母の分布規則、正書法の細則、普通話ピンインとの項目別の対照、使える簡拼まで含む完全な説明は、入力法リポジトリの [README](https://github.com/SiqYin/xinganhua-fuvufa)（[简体](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.md) ／ [繁體](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.zh-Hant.md) ／ [English](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.en.md) ／ [日本語](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.ja.md)）を参照してください。

---

<a id="s2"></a>

## 2. このサイトについて

外部に依存しない静的ページです。サーバーもデータベースもなく、ページ自身の JSON とフォント以外にリクエストを出しません。1 字が西安方言に持つ**すべての**読みを並べて見せます。

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

1 字につき 1 枚のカード。左に大きな字と簡体形、右に読みを列挙します。

| 位置 | 内容 | 例 |
|---|---|---|
| ピンイン | 全拼＋声調番号（番号は緋色） | `bfeng4` |
| 音声記号 | 国際音声記号＋調値の上付き | `[pfã⁴⁴]` |
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

## 5. 言語と自動判定

右上で **简 / 繁 / 日 / EN** を手動選択でき、選択はローカル（`localStorage`）に保存されます。初回訪問時は次の優先順で決まります。

| 優先度 | 根拠 | 結果 |
|---|---|---|
| 1 | 手動選択（URL の `?lang=hans｜hant｜ja｜en` を含む） | そのまま使用 |
| 2 | システム／ブラウザの言語（**中国語の変種と日本語のみ**） | `zh-Hant`、`zh-TW/HK/MO` → 繁体；その他の `zh-*` → 簡体；`ja-*` → 日本語；中国語でも日本語でもないシステム言語（`en-*`、`ko-*` など）は判定に加わらず次へ |
| 3 | 接続 IP の地域 | 日本 → 日本語；米・英・加・豪・NZ・仏・独・韓 → 英語；香港・澳門・台湾 → 繁体；それ以外 → 簡体 |
| 4 | 既定 | 簡体 |

つまり**中国語と日本語のシステム言語は IP より優先**されます：繁体字中国語のシステムなら、IP が中国大陸でも繁体で表示し、日本語のシステムなら IP が米国でも日本語で表示します。それ以外のシステム言語（英語・韓国語…）は UI の言語を決めず、IP の判定に委ねます。したがって「英語システム＋日本 IP」は英語ではなく日本語になります。

> 手動選択と `?lang=` が最優先で、手動選択は `localStorage` に残ります。以前 EN を押してアドレス欄に `?lang=en` が残っていると英語のままです。一度 `?lang=auto` を開けば手動選択を消して判定し直します。

実装の詳細：

- 地域判定は `https://api.country.is/`、失敗時は Cloudflare の `/cdn-cgi/trace` に退避し、どちらも 1.5 秒でタイムアウトしたら簡体
- ローカル（`localhost` / `127.0.0.1` / `file:`）と検索エンジンのクローラーは自動判定をせず簡体のまま。開発時にネットワーク環境へ引きずられず、英語版が収録されるのも避けられます
- デバッグ：`?lang=auto` で手動選択を消して再判定、`?lang=debug` でページ上部に判定結果と理由（`url` / `manual` / `system` / `ip` / `offline`）を表示
- 四言語のテキストは `data/i18n.json`。繁体は OpenCC による変換で、手書きはしません

---

<a id="s6"></a>

## 6. 音韻と入力方案のポップアップ

ページ下部の「西安方言の音韻と入力方案」は全体がクリックできる入口で、開くとポップアップになります（Esc または背景のクリックで閉じる）。内容は入力法リポジトリの README によります：

- 声母 26 個（綴り／国際音声記号／例字）
- 韻母 40 個、開斉合撮の四呼で分類
- 四声と調値
- **普通話ピンインとの異同**：まったく同じもの、字は同じで音価が異なる鼻母音、綴りの違いの表（`in→ien`、`ong→uong`、`ü→yu`…）、西安方言にしかない声母・韻母、声母が対応しない字、番号の位置は同じで調値が違うこと
- ポップアップ内のテキストも UI の言語に追随（簡 / 繁 / 英 / 日）

---

<a id="s7"></a>

## 7. データの出所

```
MCPDict「西安」データ表（国際音声記号）
        │  tools/ipa2pinyin.mjs（入力法リポジトリ）
        ▼
   字 / ピンイン / IPA / 注記  →  data/source.tsv
        │  tools/build_data.py（＋ OpenCC の簡繁表）
        ▼
   data/xian.json（字頭 → 読みの配列）
   data/variants.json（簡→繁、繁→簡）
```

| 項目 | 数 |
|---|---|
| 字頭 | 3,345 |
| 字音項目 | 3,648（一字一音一行） |
| 多音字 | 275 |
| 注記つき | 102 |
| 声調なし音節 | 392 |

簡繁の対応には OpenCC の `STCharacters.txt` / `TSCharacters.txt` を使い、ビルド時に必要に応じて取得します（リポジトリには同梱しません）。

---

<a id="s8"></a>

## 8. 配色とフォント

| 色 | 値 | 用途 |
|---|---|---|
| 黒 | `#000000` | 本文、字頭、フッターの下地。秦の色 |
| 白 | `#FFFFFF` | カードと読みブロック、入力欄。三色のうちの「紙」 |
| 緋 | `#9F363A` | 印章、ボタン、カードの左辺、フッターの強調、声調番号、音声記号の上付き、注記の罫線。漢の色 |

黒と白の間には中性の二層（暖かい紙 `#F4EEE9` の下地、淡いカード `#FBF7F4`）を置き、色相は増やしていません。

フォントは [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（LXGW WenKai Regular、OFL）のサブセット `fonts/lxgw-wenkai.woff2` で、ページが実際に使う字形だけを含みます（字頭、注記、ピンイン、音声記号、四言語の UI テキストで約 4,900 字形 / 1.2 MB）。ライセンスは `fonts/OFL.txt`。

---

<a id="s9"></a>

## 9. ディレクトリ構成

```
index.html                    単一ページ：スタイル、検索ロジック、i18n、ポップアップ
README.zh-Hant.md             繁体の説明（OpenCC 変換）
README.en.md / README.ja.md   英語・日本語の説明
data/source.tsv               字音の原表：字 / ピンイン / IPA[調名] / 注記
data/xian.json                フロント用データ：字頭 → 読みの配列
data/variants.json            簡繁の対応：s2t（簡→繁）、t2s（繁→簡、併記用）
data/i18n.json                四言語のテキスト＋音韻表データ（簡 / 繁 / 英 / 日）
figures/                      方案の図：四枚 × 四言語（入力法リポジトリと同じセット）
fonts/lxgw-wenkai.woff2       霞鹜文楷のサブセット
fonts/OFL.txt                 フォントのライセンス
tools/build_data.py           原表 → JSON（OpenCC の表がなければ自動取得）
tools/build_i18n.py           簡体のテキスト → 繁体（OpenCC）＋英・日
tools/i18n.src.json           四言語テキストの原本（簡 / 英 / 日。繁体はスクリプト生成）
tools/make_font.py            フォントのサブセット化（WOFF2）
.github/workflows/static.yml  main への push で GitHub Pages に公開
```

---

<a id="s10"></a>

## 10. ローカルで見る

ページは `fetch` で JSON を読むため、HTML を直接開くと失敗します。静的サーバーを立ててください：

```sh
python -m http.server 8765
# http://127.0.0.1:8765/ を開く
```

---

<a id="s11"></a>

## 11. 再生成

```sh
python tools/build_data.py          # data/xian.json、data/variants.json
python tools/build_i18n.py          # data/i18n.json（繁体は OpenCC）
python tools/make_font.py           # フォントのサブセット
```

`make_font.py` は既定で `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf` を読みます。引数か環境変数 `LXGW_TTF` でも指定できます：

```sh
python tools/make_font.py /path/to/LXGWWenKai-Regular.ttf
```

`index.html` のテキスト、`data/*.json`、データを変えたら、必ず `make_font.py` を走らせてください。そうしないと新しい字（とくに仮名と日本語固有の漢字）がシステムフォントに落ちます。

---

<a id="s12"></a>

## 12. デプロイ

`main` に push すると GitHub Actions が公開します（Settings → Pages → Source で GitHub Actions を選択）。ワークフローは `index.html`、`data/xian.json`、`data/variants.json`、`data/i18n.json`、`fonts/*.woff2`、OFL を `_site` にコピーし、原表とビルドスクリプトは公開しません。

---

<a id="s13"></a>

## 13. データの注意と今後

- 用字は繁体（MCPDict の原表がそうであるため）。カードには簡体形も併記して対照できるようにしています
- 原表には音だけで字がない音節が 3 つ（`zou2`、`tai3`、`sao2`）あり、検索には出しません
- ピンインや音声記号が自分の方言と違う場合は `data/source.tsv` が正です。直してビルドし直してください
- 今後：ピンイン／音声記号からの逆引き、声調による検索、字表のページ送り

---

<a id="s14"></a>

## 14. データと謝辞

- [osfans/MCPDict](https://github.com/osfans/MCPDict)（`tools/tables/data/西安.tsv`）—— 字音データの出所
- [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) —— 西安方言ピンインの方案、転写スクリプト、音韻の説明、四言語の図
- [OpenCC](https://github.com/BYVoid/OpenCC) —— 簡繁の対照表
- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai) —— 中国語フォント（OFL）
- [wugniu_zyinzozin](https://github.com/SiqYin/wugniu_zyinzozin) —— サイトの作り方、言語判定、ポップアップ版面の参照元

---

<a id="s15"></a>

## 15. ライセンス

ページとビルドスクリプトは自由に使用・改変・再配布できます。字音データは MCPDict、フォントは霞鹜文楷に由来するため、それぞれのプロジェクトの説明に従ってください。

---

## 注記

簡体中文版が原文で、繁體中文版は OpenCC による変換、English 版と日本語版は対応する翻訳です。四版は内容を同一に保つ想定で、相違があれば簡体版を正とします。本文は AI の補助を受けて作成・翻訳しました。
