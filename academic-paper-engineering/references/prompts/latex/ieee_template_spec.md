# IEEE 模板规范

## 概述

IEEE 模板是学术界最常用的模板之一，用于 IEEE 期刊和会议论文。

当前系统未内置 IEEE 模板文件（.cls/.bst），但支持 IEEE 模板规范。

## 模板规格

```json
{
  "template_name": "IEEE",
  "document_class": "IEEEtran",
  "class_options": ["conference", "journal", "letters", "compsoc"],
  "citation_engine": "bibtex",
  "citation_style": "numeric",
  "bibliography_bst": "IEEEtran.bst",
  "figure_environment": "figure",
  "table_environment": "table",
  "equation_environment": "equation",
  "section_levels": ["section", "subsection", "subsubsection", "paragraph"],
  "required_packages": ["graphicx", "amsmath", "amssymb", "booktabs", "url"],
  "forbidden_packages": [],
  "author_format": "\\author{...\\IEEEauthorblockN{Author Name}\\IEEEauthorblockA{Affiliation}}",
  "title_format": "\\title{...}",
  "abstract_format": "\\begin{abstract}...\\end{abstract}",
  "bibliography_command": "\\bibliographystyle{IEEEtran}\\bibliography{...}",
  "appendix_command": "\\appendix",
  "acknowledgement_format": "\\section*{Acknowledgment}"
}
```

## IEEEtran 文档类选项

| 选项 | 说明 |
|---|---|
| conference | 会议论文格式（双栏） |
| journal | 期刊论文格式（双栏） |
| letters | 简短投稿 |
| compsoc | 计算机学会格式 |
| 10pt | 10磅字体（默认） |
| 11pt | 11磅字体 |
| 12pt | 12磅字体 |

## 引用格式

IEEE 使用数字引用格式：[1], [2], [3]

```latex
\cite{key}              % [1]
\cite{key1, key2}       % [1, 2]
\cite{key1}--\cite{key2} % [1]--[3]
```

## 典型文档结构

```latex
\documentclass[conference]{IEEEtran}

\usepackage{graphicx}
\usepackage{amsmath, amssymb}
\usepackage{booktabs}
\usepackage{url}

\begin{document}

\title{Paper Title}
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Affiliation\\Email}
}

\maketitle

\begin{abstract}
...
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2
\end{IEEEkeywords}

\section{Introduction}
...

\section{Methodology}
...

\section{Results}
...

\section{Conclusion}
...

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

## 使用方式

如果用户请求 IEEE 格式但未提供模板文件：

1. 提示用户需要 IEEEtran.cls 文件
2. 或从 CTAN 获取：https://ctan.org/pkg/ieeetran
3. 提供上述文档结构模板作为起点
4. 在 LaTeX 安装中通常已预装 IEEEtran

## 迁移场景

### IEEE -> Elsevier

- 文档类：IEEEtran -> elsarticle
- 引用：数字 -> 数字或作者-年
- 作者格式：IEEEauthorblock -> \author{}
- 关键词：IEEEkeywords -> 模板特定命令
- 栏数：双栏 -> 可选单/双/三栏

### IEEE -> Springer

- 文档类：IEEEtran -> sn-jnl
- BST：IEEEtran.bst -> sn-basic.bst 等
- 作者格式变化
- 关键词格式变化

### IEEE -> arXiv (NeurIPS)

- 文档类：IEEEtran -> article + nips_2018.sty
- 引用格式简化
- 单栏格式
