# Frontiers 模板

## 快速开始

1. 复制 frontiers.tex 并重命名
2. 修改内容，编译：

```bash
pdflatex frontiers.tex
bibtex frontiers
pdflatex frontiers.tex
pdflatex frontiers.tex
```

## 引用样式选择

修改 \documentclass 中的选项：

```latex
% Harvard引用样式（作者-年份）- 大部分Frontiers期刊使用
\documentclass[utf8]{FrontiersinHarvard}

% Vancouver引用样式（数字编号）
\documentclass[utf8]{FrontiersinVancouver}

% 物理/数学统计期刊专用
\documentclass[utf8]{frontiersinFPHY_FAMS}
```

## 引用样式查询

请访问: https://zendesk.frontiersin.org/hc/en-us/articles/360017860337

常见期刊引用样式：
- Harvard: Psychology, Neuroscience, Education等
- Vancouver: Medicine, Immunology, Pharmacology等
- Physics/AMS: Physics, Applied Mathematics等

## 文件说明

- FrontiersinHarvard.cls - Harvard引用样式文档类
- FrontiersinVancouver.cls - Vancouver引用样式文档类
- frontiersinFPHY_FAMS.cls - 物理/数学期刊文档类
- Frontiers-Harvard.bst - Harvard参考文献样式
- Frontiers-Vancouver.bst - Vancouver参考文献样式
- frontiers_suppmat.cls - 补充材料文档类
- logo1.pdf / logo2.pdf - Frontiers logo

## 适用期刊

Frontiers in Psychology, Frontiers in Neuroscience, Frontiers in Immunology, 等Frontiers系列期刊（150+期刊）

## 补充材料

如需提交补充材料，使用：

```latex
\documentclass[utf8]{frontiers_suppmat}
```

参考 frontiers_SupplementaryMaterial.tex 示例

## 编译器

推荐使用 pdfLaTeX
