# Elsevier CAS 模板 (Cell Press期刊)

## 快速开始

1. 选择模板：
   - cas-sc-template.tex - 单栏布局
   - cas-dc-template.tex - 双栏布局

2. 复制并重命名，修改内容，编译：

```bash
pdflatex cas-sc-template.tex
bibtex cas-sc-template
pdflatex cas-sc-template.tex
pdflatex cas-sc-template.tex
```

## 模板类型

### 单栏 (cas-sc)

```latex
\documentclass[a4paper,fleqn]{cas-sc}
```

### 双栏 (cas-dc)

```latex
\documentclass[a4paper,fleqn]{cas-dc}
```

## 文件说明

- cas-sc.cls - 单栏文档类
- cas-dc.cls - 双栏文档类
- cas-common.sty - 公共宏包
- cas-model2-names.bst - 参考文献样式
- cas-refs.bib - 示例参考文献
- elsdoc-cas.pdf - 官方文档（在doc目录）

## 适用期刊

Cell, Neuron, Cell Reports, iScience, Molecular Cell, 等Cell Press期刊

## 编译器

推荐使用 pdfLaTeX
