# Taylor & Francis 模板

## 快速开始

1. 复制 main.tex 并重命名
2. 修改内容，编译：

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## 模板类型

当前使用 interact 文档类，适用于Taylor & Francis旗下期刊。

## 引用样式选择

在导言区修改：

### APA引用样式（作者-年份，默认）

```latex
\usepackage[longnamesfirst,sort]{natbib}
\bibpunct[, ]{(}{)}{;}{a}{,}{,}
```

### 数字编号样式

```latex
\usepackage[numbers,sort&compress]{natbib}
```

### APA专用样式

```latex
\usepackage[natbibapa,nodoi]{apacite}
```

## 文件说明

- interact.cls - 文档类
- natbib.sty - 引用支持包
- apacite.bst - APA参考文献样式
- booktabs.sty - 表格美化包
- subfig.sty - 子图支持包
- rotating.sty - 旋转支持包
- epsfig.sty - EPS图片支持包
- interactapasample.bib - 示例参考文献
- interactapasample.pdf - 编译示例

## 适用期刊

Taylor & Francis旗下期刊，包括：
- Journal of the American Statistical Association
- International Journal of Production Research
- 等2700+期刊

## 编译器

推荐使用 pdfLaTeX
