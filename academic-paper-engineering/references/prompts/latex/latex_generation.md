# LaTeX 渲染器

将学术文档 IR 渲染为目标 LaTeX 模板。

## 渲染原则

渲染器必须：

- 保持章节层级
- 保持段落顺序
- 保持公式
- 保持图片锚点
- 保持表格锚点
- 保持引用
- 生成标签
- 生成引用
- 使用模板特定环境

## 禁止事项

- 不直接复制源文档的格式
- 使用语义文档结构
- 使用可维护的 LaTeX 代码
- 避免不必要的内联格式
- 除非模板要求，不使用硬编码格式

## 渲染流程

1. 加载文档 IR
2. 加载模板规格说明
3. 加载文档-模板映射表
4. 生成文档头部（preamble）
5. 生成标题和作者
6. 生成摘要和关键词
7. 逐节渲染正文
8. 渲染图片
9. 渲染表格
10. 渲染公式
11. 渲染引用和参考文献
12. 生成文档尾部

## 工程结构

生成的 LaTeX 工程结构：

```
paper_project/
├── main.tex              # 主文件
├── sections/             # 分节文件
│   ├── introduction.tex
│   ├── methodology.tex
│   ├── results.tex
│   ├── discussion.tex
│   └── conclusion.tex
├── figures/              # 图片文件
├── tables/               # 表格文件（如使用外部文件）
├── references.bib        # BibTeX 参考文献
├── template/             # 模板文件（.cls, .sty, .bst）
└── QA/
    └── quality_report.md # 质量报告
```

## main.tex 结构

```latex
\documentclass[options]{template_class}

% 宏包声明
\usepackage{...}

% 模板特定设置
...

\begin{document}

\title{...}
\author{...}

\begin{abstract}
...
\end{abstract}

% 关键词
...

\section{引言}
\input{sections/introduction}

\section{方法论}
\input{sections/methodology}

\section{结果}
\input{sections/results}

\section{讨论}
\input{sections/discussion}

\section{结论}
\input{sections/conclusion}

\bibliographystyle{...}
\bibliography{references}

\end{document}
```

## 编码规范

- 使用 UTF-8 编码
- 每行不超过 80 字符（尽量）
- 使用一致的缩进
- 为每个图片、表格、公式添加 \label
- 使用语义化的标签命名
- 注释说明非显而易见的 LaTeX 代码
