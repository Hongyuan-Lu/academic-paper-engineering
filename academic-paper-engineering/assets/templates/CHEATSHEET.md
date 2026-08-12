# LaTeX 模板速查表

## 模板总览

| 模板 | 目录 | 主文件 | 文档类 | 参考文献样式 | 引用引擎 | 栏数 |
|------|------|--------|--------|-------------|---------|------|
| Elsevier | `Elsevier/` | elsarticle-template-num.tex | elsarticle | elsarticle-num.bst / elsarticle-harv.bst | bibtex, biber | 单栏/双栏/三栏/五栏 |
| Cell Press | `Cell-Press/` | cas-sc-template.tex / cas-dc-template.tex | cas-sc / cas-dc | cas-model2-names.bst | bibtex | 单栏 / 双栏 |
| Springer | `Springer/` | sn-article.tex | sn-jnl | sn-*.bst（9种） | bibtex | 单栏/双栏 |
| MDPI | `MDPI/` | template.tex | mdpi | mdpi.bst | bibtex | 单栏 |
| Frontiers | `Frontiers/` | frontiers.tex | FrontiersinHarvard / FrontiersinVancouver | Frontiers-Harvard.bst / Frontiers-Vancouver.bst | bibtex | 单栏 |
| Taylor & Francis | `Taylor-Francis/` | main.tex | interact | apacite.bst | bibtex | 单栏/双栏 |
| Wiley | `Wiley/` | sample1.tex / sample2.tex | book | wiley-authoringtemplate.sty | bibtex | 单栏 |
| arXiv | `arXiv/` | main.tex | article | abbrvnat | bibtex, biber | 单栏 |
| IEEE | （规范定义） | -- | IEEEtran | IEEEtran.bst | bibtex | 双栏 |

## 如何选择模板

### 按目标期刊选择

1. **确认目标期刊** -- 用户要投哪个期刊
2. **确认出版商** -- 该期刊属于哪个出版商
3. **选择对应模板** -- 使用上表中该出版商的模板
4. **确认变体** -- 如果模板有多种变体（栏数/引用样式），询问用户选择

### 按引用样式选择

| 引用样式 | 适用模板 | 说明 |
|---------|---------|------|
| 数字编号 [1] | Elsevier (num), Springer (mathphys-num, vancouver-num), MDPI, Frontiers (Vancouver), IEEE | 理工科常用 |
| 作者-年份 | Elsevier (harv), Springer (mathphys-ay, vancouver-ay), Frontiers (Harvard), Taylor & Francis (APA) | 社科、生物医学常用 |
| Nature 风格 | Springer (sn-nature) | Nature 系列期刊 |
| APA 风格 | Springer (sn-apa), Taylor & Francis (apacite) | 心理学、社会科学 |
| Chicago 风格 | Springer (sn-chicago) | 人文社科 |

### 按栏数选择

| 栏数 | 适用模板 | 说明 |
|------|---------|------|
| 单栏 | Elsevier (preprint/1p), Cell Press (cas-sc), MDPI, Frontiers, arXiv | 预印本、投稿稿 |
| 双栏 | Elsevier (twocolumn), Cell Press (cas-dc), IEEE | 正式发表版 |
| 多栏 | Elsevier (3p/5p) | 特定排版需求 |

## 各模板编译命令

```bash
# Elsevier
pdflatex elsarticle-template-num.tex && bibtex elsarticle-template-num && pdflatex elsarticle-template-num.tex && pdflatex elsarticle-template-num.tex

# Cell Press
pdflatex cas-sc-template.tex && bibtex cas-sc-template && pdflatex cas-sc-template.tex && pdflatex cas-sc-template.tex

# Springer
pdflatex sn-article.tex && bibtex sn-article && pdflatex sn-article.tex && pdflatex sn-article.tex

# MDPI
pdflatex template.tex && bibtex template && pdflatex template.tex && pdflatex template.tex

# Frontiers
pdflatex frontiers.tex && bibtex frontiers && pdflatex frontiers.tex && pdflatex frontiers.tex

# Taylor & Francis
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Wiley（需进入示例子目录）
cd sample-chapter-end-bib && pdflatex sample1.tex && bibtex sample1 && pdflatex sample1.tex && pdflatex sample1.tex

# arXiv
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# 通用（推荐使用 latexmk 自动化编译）
latexmk -pdf main.tex
```

## 各模板变体说明

### Elsevier (elsarticle)

| 选项 | 说明 |
|------|------|
| `preprint` | 预印本，12pt，单栏 |
| `final,1p,times` | 正式版，单栏，Times 字体 |
| `final,1p,times,twocolumn` | 正式版，双栏 |
| `final,3p,times` | 三栏 |
| `final,5p,times` | 五栏 |

引用样式：`elsarticle-num.bst`（数字编号）、`elsarticle-harv.bst`（作者-年份）

### Cell Press (CAS)

| 文档类 | 说明 |
|--------|------|
| `cas-sc` | 单栏布局 |
| `cas-dc` | 双栏布局 |

### Springer (sn-jnl)

| 引用样式 | 说明 |
|---------|------|
| `sn-nature` | Nature 期刊风格 |
| `sn-basic` | 基础/化学风格 |
| `sn-mathphys-num` | 数学物理（数字编号） |
| `sn-mathphys-ay` | 数学物理（作者-年份） |
| `sn-aps` | 美国物理学会风格 |
| `sn-vancouver-num` | 温哥华（数字编号） |
| `sn-vancouver-ay` | 温哥华（作者-年份） |
| `sn-apa` | APA 风格 |
| `sn-chicago` | 芝加哥风格 |

### Frontiers

| 文档类 | 适用期刊举例 |
|--------|-------------|
| `FrontiersinHarvard` | Psychology, Neuroscience, Education（作者-年份） |
| `FrontiersinVancouver` | Medicine, Immunology, Pharmacology（数字编号） |

## 常见问题

### 编译错误
1. 确保 LaTeX 发行版已安装（TeX Live 或 MiKTeX）
2. 检查是否缺少宏包：`tlmgr install <package>`
3. 编译顺序：pdflatex -> bibtex -> pdflatex -> pdflatex

### 参考文献不显示
1. 确保运行了 bibtex
2. 检查 .bib 文件路径是否正确
3. 检查引用键是否匹配

### 图片不显示
1. 确保图片文件存在
2. 检查文件路径
3. 使用 PDF 格式图片（推荐）

## 更新日期

2026年8月
