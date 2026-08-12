# Elsevier elsarticle 模板

## 快速开始

1. 复制 elsarticle-template-num.tex 并重命名为你的论文标题
2. 修改内容，编译：

```bash
pdflatex your-paper.tex
bibtex your-paper
pdflatex your-paper.tex
pdflatex your-paper.tex
```

## 模板选项

在 \documentclass 中修改选项：

```latex
% 预印本（默认，12pt字体）
\documentclass[preprint,12pt]{elsarticle}

% 单栏，Times字体
\documentclass[final,1p,times]{elsarticle}

% 双栏，Times字体
\documentclass[final,1p,times,twocolumn]{elsarticle}

% 三栏
\documentclass[final,3p,times]{elsarticle}

% 五栏
\documentclass[final,5p,times]{elsarticle}
```

## 参考文献样式

- elsarticle-num.bst - 数字编号 [1], [2]
- elsarticle-harv.bst - 作者年份 (Author, Year)
- elsarticle-num-names.bst - 数字+作者名显示

## 文件说明

- elsarticle.cls - 文档类
- elsarticle.dtx - 源代码
- elsdoc.pdf - 官方文档
- manifest.txt - 文件清单

## 编译器

推荐使用 pdfLaTeX
