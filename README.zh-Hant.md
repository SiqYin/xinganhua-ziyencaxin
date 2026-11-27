[简体中文](README.md) ｜ **繁體中文** ｜ [English](README.en.md) ｜ [日本語](README.ja.md)

# 西安話字音查詢 · xinganhua-ziyencaxin

> 在線查單字在西安話裏的**城區音**與**南郊音**兩套讀法：西安話拼音、國際音標、四聲調值及詞典原注一併呈列。界面備有簡體中文、繁體中文、English、日本語四版，可隨環境自動切換，也可右上角手動點選。

- **線上地址**：<https://siqyin.github.io/xinganhua-ziyencaxin/>
- **字表規模**：城區字頭 3,346 ／ 城區音 3,649 條 · 南郊音 4,594 條（南郊字頭 4,065，含渭南獨有等增補 720 字）
- **界面語言**：簡體中文 · 繁體中文 · English · 日本語
- **頁面配色**：墨黑 `#000000`（秦）· 素白 `#FFFFFF` · 絳紅 `#9F363A`（漢）
- **自託管字體**：霞鶩文楷子集（OFL），不依賴外部字體 CDN

---

## 目錄

1. [西安話拼音方案](#s1)
2. [站點結構與分工](#s2)
3. [查字與反查規則](#s3)
4. [讀音卡片說明](#s4)
5. [音系浮窗內容](#s5)
6. [字音數據來源](#s6)
7. [色彩與字體子集](#s7)
8. [目錄說明](#s8)
9. [本地預覽](#s9)
10. [數據重建](#s10)
11. [靜態部署](#s11)
12. [字表體例與後續計劃](#s12)
13. [參考與致謝](#s13)
14. [授權許可](#s14)

---

<a id="s1"></a>

## 一、西安話拼音方案

全站採用統一的一套**西安話拼音**拼寫，城區音與南郊音各有字表。每個音節由「聲母 + 韻母 + 調號」組成，例如 `ba1` 巴、`jyuen1` 軍；「中」在城區讀 `bfeng4`，南郊讀 `zung4`：

- **聲母**：共用 24 個（含零聲母），城區音另有 `bf`、`pf`（共 26），南郊音另有 `rh`（共 25）。按發音部位排作：`b p m bf pf f v` / `d t n l` / `g k h ng` / `j q x` / `zh ch sh r` / `z c s rh`（`n` 拼 `i`、`y` 細音時音值爲 `[ȵ]`）。
- **韻母**：城區音 39 個（開 14 ／ 齊 10 ／ 合 9 ／ 撮 6），南郊音 37 個（開 13 ／ 齊 9 ／ 合 9 ／ 撮 6；無 `uu`、`iae`，合口鼻尾韻直接作 `ung`）。
- **四聲**：陰平 31、陽平 24、上聲 53、去聲 55；古入聲已併入四調。
- **標調與隔音**：調號緊跟音節末尾不空格（`bfeng4`、`jyuen1`）；音節連寫易誤切處用撇號隔開（`xi'ngan1` 西安）。
- **簡拼與全簡切換**：輸入與反查端支持簡拼（`in / iu / o / ui / un` 限前有輔音聲母，`j q x` 後的 `yuo` 簡作 `o`，零聲母與 `n` 後簡作 `yo`，`yuen` 簡作 `yun`；至於 `uong → ung`，城區音中拼音可以這樣簡化，南郊音本來的拼寫就是後者 `ung`）。頂部切換按鈕可在「全拼」與「簡拼」顯示間即時切換（音標保持不變）。

下方六張配圖與輸入法倉庫 [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) 共用，簡繁英日四語內容同步：

![西安話聲母（城區音 26；南郊音 25——多 rh，無 bf、pf）](figures/onsets.hant.svg)

![西安話韻母（城區音 39；南郊音 37，無 uu、iae）](figures/rhymes.hant.svg)

![西安話四聲](figures/tones.hant.svg)

**連讀變調**：兩字相連主要變前字，分兩類——連續兩個陰平（`31-31`）時前字改讀陽平（`24-31`）；連續兩個上聲（`53-53`）時前字改讀陰平（`31-53`）。

![音節結構：聲母 + 韻母 + 調號](figures/syllable.hant.svg)

![西安話簡拼對照圖（城區 9 條 · 南郊 8 條）](figures/abbrev.hant.svg)

![南郊音的變體](figures/variant.hant.svg)

**南郊音變體**：南郊音 `z`、`c`、`s`、`rh` 四組聲母與 `u` 相接時，另有 `zh`、`ch`、`sh`、`r` 翹舌變體；其中 `sh` 拼 `u` 時另有 `f` 聲母變體。變體只加注在城區音讀 `bf`、`pf`、`f`、`v` 的字與逐字審定的渭南獨有字上（如「水」南郊音 `suei3` 另有變體 `shuei3`、`fei3`），與基本讀音同調，結果卡片內以「變體」標籤標出。

### 城區音與南郊音對照

- **城區音**：傳統西安城內口音。
- **南郊音**：西安南郊（高新、小寨、曲江一帶）口音，平翹舌分布屬**渭南型**：聲母 25 個（多 `rh`，無 `bf`、`pf`），韻母 37 個（無 `uu`、`iae`，合口鼻尾韻作 `ung`），四聲調值與城區相同。

| 項 | 城區音 | 南郊音 |
|---|---|---|
| 聲母 | 26（含 `bf`、`pf`） | 25（含 `rh`，無 `bf`、`pf`） |
| 韻母 | 39（含 `uu`、`iae`、`uong`） | 37（無 `uu`、`iae`，作 `ung`） |
| `rh` | 入 `vu1`、若 `vuo1` | `rhu1`、`rhuo1` |
| 知系合口 | 豬 `bfu1`、春 `pfen1` | `zu1`、`cuen1` |
| 書母合口 | 書 `fu1`、水 `fei3` | `su1`、`suei3` |
| 遇攝一等 | 都 `du1`、粗 `cu1` | `dou1`、`cou1` |
| `uong / ung` 韻 | `uong [uɤŋ]`（東 `duong1`、翁 `wong1`） | `ung [uŋ]`（東 `dung1`、翁 `wung1`） |
| 聲調 | 陰平 31、陽平 24、上聲 53、去聲 55 | 同城區音 |

完整的聲韻母配合規則、正字法與普通話拼音對照，可參閱輸入法倉庫 [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa)（[簡體](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.md) ／ [繁體](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.zh-Hant.md) ／ [English](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.en.md) ／ [日本語](https://github.com/SiqYin/xinganhua-fuvufa/blob/main/README.ja.md)）。

---

<a id="s2"></a>

## 二、站點結構與分工

整站爲純靜態單頁應用，無後端服務或遠程數據庫，頁面加載後只讀取隨站部署的 JSON 數據與本地字體子集，一次性把單個漢字在城區與南郊兩套口音中的所有讀法並排展開。

頁面下半部分附有「西安市的口音分區」簡介與示意圖：以明城牆內城區爲中心環列四郊，城區、北郊、西郊大致歸西安型，南郊、東郊大致歸渭南型；圖中兩條虛線僅爲方位示意，並非行政區劃邊界。

---

<a id="s3"></a>

## 三、查字與反查規則

| 項 | 規則說明 |
|---|---|
| 簡繁自動映射 | 輸入簡體字先按 OpenCC 映射展開至詞典繁體字頭（如 `鵝`→`鵝`、`邊`→`邊`），輸入繁體直接命中 |
| 字數與去重 | 單次最多查 30 個漢字，重複字只渲染一張卡片；中英文標點與空白自動剝離 |
| 拼音反查 | 純字母（可帶調號 1–4）輸入按單個西安話音節反查字表，同時兼容全拼與簡拼，兩套字表合併展示 |
| 混排校驗 | 漢字與英文字母混輸時提示分開查詢 |
| 未收錄提示 | 詞典未收的字會列出缺字提示卡片，不靜默跳過 |
| 鏈接分享 | 查詢詞寫入 URL `?q=…`，複製鏈接即可復現結果 |

---

<a id="s4"></a>

## 四、讀音卡片說明

每張結果卡片左側展示繁體字頭與對應簡體，右側分欄並排顯示**城區音**（紅調）與**南郊音**（藍調）：

| 字段 | 內容 | 示例 |
|---|---|---|
| 拼音 | 全拼（或簡拼）+ 調號 | `bfeng4` ／ `zung4` |
| 音標 | 國際音標 + 調值上標 | `[pfəŋ⁵⁵]` ／ `[tsuŋ⁵⁵]` |
| 聲調 | 調名 + 調值（隨界面語言切換） | 去聲 55 |
| 釋注 | 原詞表所附 `{}` 釋義及 `白讀／文讀`、`變體` 標記 | 釋 白讀, 西~, 北~ |

調號與調值對照：

| 調號 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 調名 | 陰平 | 陽平 | 上聲 | 去聲 |
| 調值 | 31 | 24 | 53 | 55 |
| 例字 | `tian1` 天 | `nian2` 年 | `xiao3` 小 | `qi4` 去 |

多音字按陰平、陽平、上聲、去聲先後排列（如 `着` 收五讀：`zhao1` / `zhe1` / `bfuo2` / `pfuo2` / `zhao2`）。

---

<a id="s5"></a>

## 五、音系浮窗內容

點開搜索欄下方的「西安話音系與輸入方案」橫條可呼出浮窗（按 `Esc` 或點擊遮罩關閉），按新音系順序完整列出：

- 聲母表：按六組發音部位及零聲母 7 行排布，標出城區音特有 `bf`、`pf` 與南郊音特有 `rh`（含 `n` 逢細音讀 `[ȵ]` 註釋）。
- 韻母表：按開（14）、齊（10）、合（9）、撮（6）四呼分行排列，`uu`、`iae` 標示城區特有，`uong / ung` 並列城區 `duong1 [uɤŋ]` 與南郊 `dung1 [uŋ]`。
- 四聲與連讀變調規則（`31 / 24 / 53 / 55` 及 `31-31→24-31`、`53-53→31-53`）。
- 城區音與南郊音對照、南郊音變體說明、與普通話拼音異同、輸入端簡化拼寫及字音來源鏈接。

---

<a id="s6"></a>

## 六、字音數據來源

西安話城區音直接取自記錄城區音的西安話音檔；南郊音參考西安話、渭南話、臨潼話、華縣話等音檔逐字釐定，僅供參考，錯漏之處歡迎反饋指正。

- [西安話音檔](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E8%A5%BF%E5%AE%89.tsv)
- [渭南話音檔](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E6%B8%AD%E5%8D%97.tsv)
- [臨潼話音檔](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E4%B8%B4%E6%BD%BC%E6%96%B9%E8%A8%80%E8%AF%AD%E9%9F%B3%E7%A0%94%E7%A9%B6.tsv)
- [華縣話音檔](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E5%8D%8E%E5%8E%BF.tsv)

---

<a id="s7"></a>

## 七、色彩與字體子集

| 顏色 | 色值 | 角色 |
|---|---|---|
| 墨黑 | `#000000` | 字頭、主文、頁腳底色（秦） |
| 素白 | `#FFFFFF` | 讀音白底塊與輸入框 |
| 絳紅 | `#9F363A` | 印章、主按鈕、卡片邊線、調號與上標（漢） |

另以暖紙 `#F4EEE9` 與淺卡 `#FBF7F4` 鋪底，南郊音分欄採用靛藍 `#2F5D8C` 區分。字體使用 [霞鶩文楷](https://github.com/lxgw/LxgwWenKai)（OFL），由構建腳本掃描頁面、四語 JSON 與全部擴展區字頭及國際音標符號子集化爲 `fonts/lxgw-wenkai.woff2`。

---

<a id="s8"></a>

## 八、目錄說明

```
index.html                    單頁主文件（樣式、查詢、反查與音系浮窗）
README.zh-Hant.md             繁體說明（由 OpenCC 從簡體轉出）
README.en.md / README.ja.md   英文、日文說明
data/source.tsv               城區音字源表：字 / 拼音 / IPA[調名] / 釋注
data/xian.json                城區音前端數據
data/nanjiao.json             南郊音前端數據
data/variants.json            OpenCC 簡繁對照映射（s2t / t2s）
data/i18n.json                四語界面文案與音系表數據
figures/                      六張音系配圖 × 四種語言（共 24 份）
fonts/lxgw-wenkai.woff2       霞鶩文楷子集字體
fonts/OFL.txt                 字體授權文件
tools/build_data.py           source.tsv → xian.json / variants.json
tools/build_nanjiao_json.py   南郊音字表.tsv → nanjiao.json
tools/build_i18n.py           i18n.src.json → i18n.json（自動生成繁體）
tools/i18n.src.json           簡、英、日三語文案源文件
tools/make_font.py            生成 WOFF2 字體子集
.github/workflows/static.yml  GitHub Pages 自動部署流程
```

---

<a id="s9"></a>

## 九、本地預覽

因頁面通過 `fetch` 加載同源 JSON 數據，請勿直接雙擊打開 HTML，需在倉庫根目錄啓動本地靜態服務器：

```sh
python -m http.server 8765
# 瀏覽器訪問 http://127.0.0.1:8765/
```

---

<a id="s10"></a>

## 十、數據重建

```sh
python tools/build_data.py
python tools/build_nanjiao_json.py
python tools/build_i18n.py
python tools/make_font.py
```

`make_font.py` 默認讀取 `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf`，也可通過命令行參數或環境變量 `LXGW_TTF` 指定字體路徑。每次修改文案、音標符號或字表後，需重跑 `make_font.py` 以免新字符回退到系統字體。

---

<a id="s11"></a>

## 十一、靜態部署

代碼推送至 `main` 分支後，由 `.github/workflows/static.yml` 將 `index.html`、`data/*.json` 與 `fonts/` 打包發佈至 GitHub Pages，源表與構建工具不會進入線上產物。

---

<a id="s12"></a>

## 十二、字表體例與後續計劃

- 詞典字頭保留 MCPDict 原本繁體字形，卡片上同時列出對應簡體形。
- 南郊音由逐字裁定表與兩地一致讀音合成：無 `bf`/`pf`（改讀 `z`/`c` 並增 `u` 介音）、無 `uu`/`iae`（併入 `e`/`ie`）、新增 `rh`（對應城區 `v`），並按審定規則補充翹舌與 `f` 變體；特例字如 `癌 ngae2`、`涯 ya2`、`後 hou4`、`芍 shuo2`。
- 源表中 3 個有音無字音節（`zou2`、`tae3`、`sao2`）未收入查詢字表。
- 後續計劃補入按聲調篩選、音標反查與全字表分頁瀏覽。

---

<a id="s13"></a>

## 十三、參考與致謝

- [西安話音檔](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E8%A5%BF%E5%AE%89.tsv)、[渭南話音檔](https://github.com/osfans/MCPDict/blob/master/tools/tables/data/%E6%B8%AD%E5%8D%97.tsv)、[臨潼話音檔](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E4%B8%B4%E6%BD%BC%E6%96%B9%E8%A8%80%E8%AF%AD%E9%9F%B3%E7%A0%94%E7%A9%B6.tsv)、[華縣話音檔](https://github.com/osfans/MCPDict/blob/master/tools%2Ftables%2Fdata%2F%E5%8D%8E%E5%8E%BF.tsv)（[osfans/MCPDict](https://github.com/osfans/MCPDict)）。
- **南郊話音檔**無現成字表可依：在西安話、渭南話、臨潼話、華縣話音檔底本上，參照知乎關於南郊音、東郊音平翹舌歸併的討論，並與本人及家人讀音逐字覈對而成，**僅供參考**。
- [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) —— 西安話拼音方案本體、轉寫腳本與配圖來源。
- [OpenCC](https://github.com/BYVoid/OpenCC) —— 簡繁字形對照表；[霞鶩文楷](https://github.com/lxgw/LxgwWenKai) —— 頁面正文及音標字體（OFL）。
- [wugniu_zyinzozin](https://github.com/SiqYin/wugniu_zyinzozin) —— 本站頁面佈局與浮窗交互參照。

---

<a id="s14"></a>

## 十四、授權許可

頁面代碼與構建腳本可自由使用、修改與再分發。字音資料與字體的版權歸屬及使用條款分別遵循 MCPDict 與霞鶩文楷原項目規定。
