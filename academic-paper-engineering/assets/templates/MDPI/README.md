# MDPI 模板

## 快速开始

1. 复制 template.tex 并重命名
2. 修改内容，编译：

```bash
pdflatex template.tex
bibtex template
pdflatex template.tex
pdflatex template.tex
```

## 期刊选择

修改 \documentclass 中的 journal=XXXX：

```latex
\documentclass[journal=sensors,article,submit,pdftex,moreauthors]{Definitions/mdpi}
```

## 常用期刊缩写

| 缩写 | 期刊全称 |
|------|---------|
| sensors | Sensors |
| materials | Materials |
| energies | Energies |
| applsci | Applied Sciences |
| remotesensing | Remote Sensing |
| mathematics | Mathematics |
| symmetry | Symmetry |
| entropy | Entropy |
| water | Water |
| forests | Forests |
| plants | Plants |
| animals | Animals |
| foods | Foods |
| ijms | Int. J. Molecular Sciences |
| jcm | J. Clinical Medicine |
| diagnostics | Diagnostics |
| processes | Processes |
| electronics | Electronics |
| machines | Machines |
| micromachines | Micromachines |
| nanomaterials | Nanomaterials |
| crystals | Crystals |
| catalysts | Catalysts |
| coatings | Coatings |
| polymers | Polymers |
| metals | Metals |
| biology | Biology |
| life | Life |
| genes | Genes |
| cells | Cells |
| viruses | Viruses |
| cancers | Cancers |
| brainsci | Brain Sciences |
| children | Children |
| healthcare | Healthcare |
| nutrients | Nutrients |
| pharmaceutics | Pharmaceutics |
| axioms | Axioms |
| algorithms | Algorithms |
| information | Information |
| systems | Systems |
| jmse | J. Marine Science and Engineering |
| sustainability | Sustainability |
| environment | Environments |
| climate | Climate |
| land | Land |
| geosciences | Geosciences |
| aerospace | Aerospace |
| drones | Drones |
| vehicles | Vehicles |
| wevj | World Electric Vehicle Journal |
| futureinternet | Future Internet |
| computers | Computers |
| ai | AI |
| robotics | Robotics |
| automation | Automation |
| vision | Vision |

**完整期刊列表**: 参见 Definitions/journalnames.tex

## 文章类型

修改 \documentclass 中的类型选项：

```latex
% 研究论文（默认）
\documentclass[journal=sensors,article,submit,pdftex,moreauthors]{Definitions/mdpi}

% 综述
\documentclass[journal=sensors,review,submit,pdftex,moreauthors]{Definitions/mdpi}

% 通讯
\documentclass[journal=sensors,communication,submit,pdftex,moreauthors]{Definitions/mdpi}

% 信件
\documentclass[journal=sensors,letter,submit,pdftex,moreauthors]{Definitions/mdpi}
```

## 提交状态

- submit - 投稿状态（显示行号）
- accept - 接受状态（去除行号）

## 文件说明

- Definitions/mdpi.cls - 文档类
- Definitions/mdpi.bst - 参考文献样式
- Definitions/journalnames.tex - 期刊名称定义
- Definitions/logo-mdpi.eps - MDPI logo

## 编译器

推荐使用 pdfLaTeX
