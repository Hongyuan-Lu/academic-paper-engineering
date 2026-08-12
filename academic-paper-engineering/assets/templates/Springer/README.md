# Springer Nature 模板

## 快速开始

1. 复制 sn-article.tex 并重命名
2. 修改内容，编译：

```bash
pdflatex sn-article.tex
bibtex sn-article
pdflatex sn-article.tex
pdflatex sn-article.tex
```

## 参考文献样式选择

修改 \documentclass 中的选项：

```latex
% Nature期刊风格
\documentclass[pdflatex,sn-nature]{sn-jnl}

% 基础/化学风格
\documentclass[pdflatex,sn-basic]{sn-jnl}

% 数学物理（数字编号）
\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}

% 数学物理（作者年份）
\documentclass[pdflatex,sn-mathphys-ay]{sn-jnl}

% 美国物理学会
\documentclass[pdflatex,sn-aps]{sn-jnl}

% 温哥华（数字编号）
\documentclass[pdflatex,sn-vancouver-num]{sn-jnl}

% 温哥华（作者年份）
\documentclass[pdflatex,sn-vancouver-ay]{sn-jnl}

% APA风格
\documentclass[pdflatex,sn-apa]{sn-jnl}

% 芝加哥风格
\documentclass[pdflatex,sn-chicago]{sn-jnl}
```

## 文件说明

- sn-jnl.cls - 文档类
- bst/ - 参考文献样式目录
- user-manual.pdf - 官方用户手册
- sn-article.pdf - 编译示例

## 适用期刊

Nature, Scientific Reports, Nature Communications, 等Springer Nature旗下期刊

## 编译器

推荐使用 pdfLaTeX
