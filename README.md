# 西安话字音查询 · xinganhua-ziyencaxin

> 输入汉字（简繁皆可，一次最多 30 字），查它在西安话（关中片）里的全部字音：**西安话拼音**、**国际音标**、**声调**，以及词典原有的释注。界面有简、繁、英三种语言，并按系统语言与接入地区自动判定。

![西安话字音查询界面](screenshot.png)

- **线上地址**：<https://siqyin.github.io/xinganhua-ziyencaxin/>
- **字表**：字头 3,345 ／ 字音 3,648 ／ 多音字 275 ／ 带释注 102
- **语言**：简体中文 · 繁體中文 · English（自动判定 + 手选）
- **配色**：黑 `#000000`（秦）· 白 `#FFFFFF` · 绛红 `#9F363A`（汉）
- **字体**：霞鹜文楷子集，自托管，不依赖 CDN

---

## 目录

1. [这个网站是什么](#一这个网站是什么)
2. [查询规则](#二查询规则)
3. [结果怎么读](#三结果怎么读)
4. [语言与自动判定](#四语言与自动判定)
5. [音系与输入方案浮窗](#五音系与输入方案浮窗)
6. [数据从哪来](#六数据从哪来)
7. [配色与字体](#七配色与字体)
8. [目录结构](#八目录结构)
9. [本地预览](#九本地预览)
10. [重新构建](#十重新构建)
11. [部署](#十一部署)
12. [数据说明与待办](#十二数据说明与待办)
13. [数据与致谢](#十三数据与致谢)
14. [授权](#十四授权)

---

## 一、这个网站是什么

一个离线的静态网页：没有后端、没有数据库，除页面自身的 JSON 与字体外不发任何请求，把一个字在西安话里的**所有**读音摊开给你看。

版面分五层，全是黑白绛红三色的不同层次：暖纸页底 → 浅色卡片 → 白色读音块 → 绛红强调（印章、按钮、调号、释注）→ 墨黑页脚。

## 二、查询规则

| 规则 | 行为 |
|---|---|
| 简繁 | 输入简体先折成字典里的繁体字头再查（`鹅`→`鵝`、`边`→`邊`）；输入繁体直接命中 |
| 字数 | 一次最多 30 个汉字，超出会提示实际字数，不出结果 |
| 去重 | 输入里重复的字只查一次；简繁混输（如「鹅着軍」）各自展开 |
| 非汉字 | 字母、数字、符号会被过滤；全是非汉字时给出提示（本页不做拼音反查） |
| 未收录 | 字表里没有的字会显示一张「未收录」卡片，不会静默消失 |
| 分享 | 查询写入地址栏 `?q=…`，复制链接可复原结果 |

## 三、结果怎么读

每个字一张卡片：左边是大字与简体形，右边逐条列读音。

| 位置 | 内容 | 例 |
|---|---|---|
| 拼音 | 全拼 + 调号（调号用绛红） | `bfeng4` |
| 音标 | 国际音标 + 调值上标 | `[pfã⁴⁴]` |
| 声调 | 调名 + 调值（英文界面显示 Yinping / Yangping / Shangsheng / Qusheng） | 去声 44 |
| 释注 | 字表原带的 `{}` 注释；`白讀／文讀` 单独标出 | 释 白读, 西~, 北~ |

调号对照：

| 调号 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 调名 | 阴平 | 阳平 | 上声 | 去声 |
| 调值 | 21 | 24 | 53 | 44 |
| 例 | `tian1` 天 | `nian2` 年 | `xiao3` 小 | `qu4` 去 |

多音字按阴平 → 阳平 → 上声 → 去声排序，例如 `着` 有五读：`zhao1` / `zhe1` / `bfuo2` / `pfuo2` / `zhao2`。

## 四、语言与自动判定

界面右上角可以手选 **简 / 繁 / EN**，选择会记在本地（`localStorage`）。首次访问时按下面的优先级判定：

| 优先级 | 依据 | 结果 |
|---|---|---|
| 1 | 手动选择（含网址 `?lang=hans｜hant｜en`） | 直接使用 |
| 2 | 系统／浏览器语言 | `zh-Hant`、`zh-TW/HK/MO` → 繁体；其他 `zh-*` → 简体；`en-*` → 英文 |
| 3 | 访问 IP 归属地 | 美国、英国、加拿大、澳大利亚、新西兰、法国、德国、韩国 → 英文；香港、澳门、台湾 → 繁体；其余全部 → 简体 |
| 4 | 兜底 | 简体 |

也就是说**系统语言优先于 IP**：系统是繁体中文，即使 IP 在中国大陆也显示繁体。系统语言不在上表（如日语、俄语）时，才交给 IP 判断。

实现细节：

- 地理判定用 `https://api.country.is/`，失败时回退 Cloudflare 的 `/cdn-cgi/trace`，都超时（1.5 秒）就按简体
- 本地预览（`localhost` / `127.0.0.1` / `file:`）与搜索引擎爬虫不做自动判定，保持简体，避免开发时被网络环境带着跑、也避免收录到英文版
- 调试用 `?lang=auto` 可清掉手选后重新判定
- 三套文案在 `data/i18n.json`；繁体由 OpenCC 从简体转换，不手写

## 五、音系与输入方案浮窗

页面下方的「西安话音系与输入方案」是一整块可点的入口，点开是浮窗（Esc 或点遮罩关闭），内容取自输入法仓库 [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) 的 README：

- 声母 26 个（写法 / 国际音标 / 例字）
- 韵母 40 个，按开齐合撮四呼分组
- 四声与调值
- **与普通话拼音的异同**：完全一样的、字母相同音值不同的鼻化韵、拼写差异表（`in→ien`、`ong→uong`、`ü→yu`…）、西安多出来的声母韵母、声母对不上的字、调号同位不同调值
- 浮窗内的文案随界面语言切换（简 / 繁 / 英）

## 六、数据从哪来

```
MCPDict《西安》数据表（国际音标）
        │  tools/ipa2pinyin.mjs（输入法仓库）
        ▼
   字 / 拼音 / IPA / 释注  →  data/source.tsv
        │  tools/build_data.py（+ OpenCC 简繁表）
        ▼
   data/xian.json（字头 → 读音数组）
   data/variants.json（简→繁、繁→简）
```

| 项 | 数 |
|---|---|
| 字头 | 3,345 |
| 字音条目 | 3,648（一字一音一行） |
| 多音字 | 275 |
| 带释注 | 102 |
| 不计调音节 | 392 |

简繁映射用 OpenCC 的 `STCharacters.txt` / `TSCharacters.txt`，构建时按需下载，不随仓库分发。

## 七、配色与字体

| 颜色 | 值 | 用途 |
|---|---|---|
| 黑 | `#000000` | 正文、字头、页脚底；秦色 |
| 白 | `#FFFFFF` | 卡片与读音块、输入框；三色之中的「纸」 |
| 绛红 | `#9F363A` | 印章、按钮、卡片左边、页脚强调、调号、音标上标、释注边线；汉色 |

底色还有两层中性层次（暖纸 `#F4EEE9` 页底、浅卡 `#FBF7F4`），是黑白之间的过渡，不另立色相。

字体是 [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（LXGW WenKai Regular，OFL 授权）的子集：`fonts/lxgw-wenkai.woff2`，只含页面实际用到的字形（字头、释注、拼音、音标与界面文案，约 4,800 字形 / 1.2 MB）。字体授权见 `fonts/OFL.txt`。

## 八、目录结构

```
index.html                    单页：样式、查询逻辑、i18n 与浮窗都在这一个文件里
screenshot.png                本说明用的界面截图
data/source.tsv               字音源表：字 / 拼音 / IPA[调名] / 释注
data/xian.json                前端数据：字头 → 读音数组
data/variants.json            简繁映射：s2t（简→繁）、t2s（繁→简，用于并列显示）
data/i18n.json                三语文案 + 音系表数据（简 / 繁 / 英）
fonts/lxgw-wenkai.woff2       霞鹜文楷子集
fonts/OFL.txt                 字体授权
tools/build_data.py           源表 → JSON（OpenCC 表缺失时自动下载）
tools/build_i18n.py           简体文案 → 繁体（OpenCC）+ 英文，输出 i18n.json
tools/i18n.src.json           三语文案的源文件（简 / 英，繁体由脚本生成）
tools/make_font.py            字体子集化（WOFF2）
.github/workflows/static.yml  推到 main 时自动发布 GitHub Pages
```

## 九、本地预览

页面用 `fetch` 读 JSON，直接双击 HTML 会失败，起个静态服务器即可：

```sh
python -m http.server 8765
# 打开 http://127.0.0.1:8765/
```

## 十、重新构建

```sh
python tools/build_data.py          # 生成 data/xian.json、data/variants.json
python tools/build_i18n.py          # 生成 data/i18n.json（繁体由 OpenCC 转出）
python tools/make_font.py           # 重新生成字体子集
```

`make_font.py` 默认读 `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf`，也可以用参数或环境变量 `LXGW_TTF` 指定：

```sh
python tools/make_font.py /path/to/LXGWWenKai-Regular.ttf
```

改了 `index.html` 里的文案、`data/*.json` 或数据后都要重跑 `make_font.py`，否则新字会落回系统字体。

## 十一、部署

推到 `main` 后由 GitHub Actions 发布（仓库 Settings → Pages → Source 选 GitHub Actions）。工作流把 `index.html`、`data/xian.json`、`data/variants.json`、`data/i18n.json`、`fonts/*.woff2` 与 OFL 拷进 `_site`，源表与构建脚本不随站点发布。

## 十二、数据说明与待办

- 用字是繁体（MCPDict 原表如此），卡片上并列显示简体形，便于对照
- 原表有 3 个只有音、没有字的音节（`zou2`、`tai3`、`sao2`），不进查询
- 拼音与音标若与你的方言有出入，以 `data/source.tsv` 为准，改完重跑构建脚本即可
- 待办：拼音／音标反查、按声调查询、字表分页浏览

## 十三、数据与致谢

- [osfans/MCPDict](https://github.com/osfans/MCPDict)（`tools/tables/data/西安.tsv`）—— 字音数据源
- [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) —— 西安话拼音方案、转写脚本与音系说明
- [OpenCC](https://github.com/BYVoid/OpenCC) —— 简繁对照表
- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai) —— 中文字体（OFL）
- [wugniu_zyinzozin](https://github.com/SiqYin/wugniu_zyinzozin) —— 站点做法、语言判定与浮窗版面的参照

## 十四、授权

网页与构建脚本可自由使用、修改、再分发。字音数据来自 MCPDict，字体来自霞鹜文楷，版权与授权请遵循各自项目说明。

---

## 声明

本 README 的全部内容由 Qoder 平台下的 Qwen 模型撰写输出。
