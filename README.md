# 西安话字音查询 · xinganhua-ziyencaxin

> 输入汉字（简繁皆可，一次最多 30 字），查它在西安话（关中片）里的全部字音：**西安话拼音**、**国际音标**、**声调**，以及词典里原有的释注。

线上地址：<https://siqyin.github.io/xinganhua-ziyencaxin/>

配色只用三种：**黑 `#000000`**（秦）、**白 `#FFFFFF`**、**绛红 `#9F363A`**（汉）。页面顶部三色条即取此意。

---

## 一、功能

| 功能 | 说明 |
|---|---|
| 汉字查询 | 简体、繁体都行；简体字会先折成字典里的繁体字头再查 |
| 多音字 | 一个字的所有读音逐条列出，按阴平→阳平→上声→去声排列 |
| 音标 | 每个读音给西安话拼音（带调号 1/2/3/4）、国际音标、调值与调名 |
| 释注 | 字表原带的 `{}` 释注一并显示（共 101 条）；「白讀／文讀」标记会单独提示 |
| 字数上限 | 一次最多 30 字，超出会提示实际字数 |
| 去重 | 输入里重复的字只查一次；简繁混输（如「鹅着軍」）各自展开 |
| 可分享 | 查询会写进地址栏 `?q=…`，复制链接即可复原结果 |

## 二、数据

- 字头 **3,344**、字音条目 **3,647**、多音字 **275**、带释注 **101**
- 来源：[osfans/MCPDict](https://github.com/osfans/MCPDict) 的《西安》数据表（国际音标），由 [xinganhua-fuvufa](https://github.com/SiqYin/xinganhua-fuvufa) 的转写脚本产出 `源表 → 西安话拼音 + IPA` 的对照，本仓库再打包成前端 JSON
- 简繁映射：OpenCC 的 `STCharacters.txt` / `TSCharacters.txt`（构建时下载，不入库）
- 调号：`1` 阴平 21、`2` 阳平 24、`3` 上声 53、`4` 去声 44

## 三、字体

页面自带 [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（LXGW WenKai Regular，OFL 授权）子集，`fonts/lxgw-wenkai.woff2`，只含页面实际用到的字形（字头、释注、拼音、音标与界面文案，约 4,700 字形 / 1.2 MB），不依赖任何 CDN。

## 四、目录

```
index.html                 单页应用：样式、查询逻辑全在这一个文件里
data/source.tsv            字音源表：字 / 拼音 / IPA[调名] / 释注
data/xian.json             打包后的字音数据（字头 → 读音数组）
data/variants.json         简繁映射：s2t（简化→繁体字头）、t2s（繁体→简体，用于并列显示）
fonts/lxgw-wenkai.woff2    霞鹜文楷子集
fonts/OFL.txt              字体授权
tools/build_data.py        源表 → JSON（简繁表缺失时自动从 OpenCC 下载）
tools/make_font.py         字体子集化（WOFF2）
.github/workflows/static.yml  推到 main 时自动部署 GitHub Pages
```

## 五、本地预览

页面用 `fetch` 读 JSON，直接双击 HTML 会失败，起个静态服务器即可：

```sh
python -m http.server 8765
# 打开 http://127.0.0.1:8765/
```

## 六、重新构建数据

```sh
python tools/build_data.py          # 生成 data/xian.json、data/variants.json
python tools/make_font.py           # 重新生成字体子集（需要本机有 LXGWWenKai-Regular.ttf）
```

`make_font.py` 默认读 `D:\Wu\NetDisk Download\lxgw-wenkai-v1.530\lxgw-wenkai-v1.530\LXGWWenKai-Regular.ttf`，也可以用参数或环境变量 `LXGW_TTF` 指定：

```sh
python tools/make_font.py /path/to/LXGWWenKai-Regular.ttf
```

改了 `index.html` 里的文案或数据，都要重跑 `make_font.py`，否则新字会落回系统字体。

## 七、部署

推到 `main` 后由 GitHub Actions 发布（Settings → Pages → Source 选 GitHub Actions）。工作流只把 `index.html`、`data/xian.json`、`data/variants.json`、`fonts/*.woff2` 和 OFL 拷进 `_site`，源表与脚本不随站点发布。

## 八、数据说明

- 用字是繁体（MCPDict 原表如此），页面在字头下方并列显示简体形，便于对照
- 原表有 3 个只有音、没有字的音节（`zou2`、`tai3`、`sao2`），不进查询
- 拼音与音标若与你的方言有出入，以 `data/source.tsv` 为准，改完重跑构建脚本即可
