# Wiley 模板

## 模板类型

本目录包含Wiley出版的书籍/专著模板，不是期刊论文模板。

## 快速开始

### 单章节引用样式

1. 进入 sample-chapter-end-bib 目录
2. 编译：

```bash
pdflatex sample1.tex
bibtex sample1
pdflatex sample1.tex
pdflatex sample1.tex
```

### 书末引用样式

1. 进入 sample-book-end-bib 目录
2. 编译：

```bash
pdflatex sample2.tex
bibtex sample2
pdflatex sample2.tex
pdflatex sample2.tex
```

## 引用样式选择

在导言区修改：

### 作者-年份引用（默认）

```latex
\usepackage[sectionbib,authoryear]{natbib}
```

### 数字编号引用

```latex
\usepackage[sectionbib,numbers]{natbib}
```

## 文件说明

### 核心文件

- Template&Manual/wiley-authoringtemplate.sty - 主要模板样式文件
- Template&Manual/AuthoringTemplate_Manual.pdf - 官方使用手册
- Template&Manual/boites_exemples.sty - 示例样式包
- Template&Manual/wiley-authoringtemplate.docx - Word 版模板

### 示例目录

- sample-chapter-end-bib/ - 每章末尾参考文献示例
- sample-book-end-bib/ - 书末统一参考文献示例
- math-examples/ - 数学公式示例

## 章节结构

书籍模板包含：
- fm.tex - 前言（封面、目录等）
- ch01.tex ~ ch05.tex - 正文章节
- app01.tex ~ app02.tex - 附录

## 适用场景

- 学术专著
- 教科书
- 会议论文集
- Wiley出版的书籍

## 编译器

推荐使用 pdfLaTeX

## 注意事项

这是书籍模板，结构比期刊模板复杂。如需期刊论文模板，请访问Wiley官网获取具体期刊的模板。
