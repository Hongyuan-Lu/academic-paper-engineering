# LaTeX 规则

## 文档结构

```latex
\documentclass[options]{class}

% 导言区
\usepackage{...}

\begin{document}

% 标题
\title{...}
\author{...}
\date{...}
\maketitle

% 摘要
\begin{abstract}
...
\end{abstract}

% 正文
\section{...}
\subsection{...}
...

% 参考文献
\bibliographystyle{...}
\bibliography{references}

\end{document}
```

## 编码

- 使用 UTF-8 编码
- XeLaTeX 优先（支持中文）
- pdfLaTeX 适用于纯英文

## 宏包管理

### 常用宏包

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{xcolor}
\usepackage{algorithm}
\usepackage{algpseudocode}
```

### 宏包冲突

- 检查模板是否已加载某宏包
- 避免重复加载
- 注意宏包加载顺序

## 章节命令

| 层级 | 命令 |
|---|---|
| 1 | \section{...} |
| 2 | \subsection{...} |
| 3 | \subsubsection{...} |
| 4 | \paragraph{...} |
| 5 | \subparagraph{...} |

## 浮动体位置

- [h] - 此处（here）
- [t] - 页顶（top）
- [b] - 页底（bottom）
- [p] - 独立页（page）
- [htbp] - 推荐组合

## 交叉引用

- 图片：\label{fig:...}
- 表格：\label{tab:...}
- 公式：\label{eq:...}
- 章节：\label{sec:...}
- 引用：\ref{...} 或 \cref{...}

## 编译流程

1. pdflatex main.tex
2. bibtex main
3. pdflatex main.tex
4. pdflatex main.tex

或使用 latexmk：

```
latexmk -pdf main.tex
```

## 文件组织

- 主文件：main.tex
- 分节文件：sections/*.tex
- 图片：figures/
- 参考文献：references.bib
- 模板文件：template/

## 注意事项

- 每个浮动体必须有 \label 和 \caption
- \caption 必须在 \label 之前
- 图片标题说明在图片下方
- 表格标题说明在表格上方
- 使用 \input 而非 \include 分节
- 注释使用 %
