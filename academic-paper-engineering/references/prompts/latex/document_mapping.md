# 文档-模板映射器

将学术文档 IR 映射到目标 LaTeX 模板。

## 映射原则

1. 语义结构映射，非格式映射
2. 保持内容完整性
3. 遵循模板约束
4. 不硬编码期刊特定规则

## 映射规则

### 元数据映射

| IR 元素 | LaTeX 模板元素 |
|---|---|
| title | \title{...} |
| authors | \author{...} 或模板特定格式 |
| affiliations | 模板特定的机构格式 |
| abstract | \begin{abstract}...\end{abstract} 或模板特定环境 |
| keywords | 模板特定的关键词命令 |

### 结构映射

| IR 元素 | LaTeX 命令 |
|---|---|
| section (level 1) | \section{...} |
| section (level 2) | \subsection{...} |
| section (level 3) | \subsubsection{...} |
| section (level 4) | \paragraph{...} |
| paragraph | 普通段落文本 |
| list (ordered) | \begin{enumerate}...\end{enumerate} |
| list (unordered) | \begin{itemize}...\end{itemize} |

### 资产映射

| IR 元素 | LaTeX 环境 |
|---|---|
| figure | \begin{figure}...\end{figure} |
| table | \begin{table}...\end{table} |
| equation | \begin{equation}...\end{equation} |

### 引用映射

| IR 元素 | LaTeX 命令 |
|---|---|
| citation | \cite{...} 或模板特定引用命令 |
| reference | BibTeX 条目 |

## 映射流程

1. 加载文档 IR
2. 加载模板规格说明
3. 逐元素映射
4. 处理特殊模板要求
5. 生成映射表
6. 标记无法映射的元素

## 输出

```json
{
  "mapping_table": [
    {
      "ir_element_id": "section_001",
      "ir_type": "section",
      "latex_command": "\\section{...}",
      "status": "mapped"
    }
  ],
  "unmapped_elements": [],
  "warnings": []
}
```

## 注意事项

- 不同模板对作者格式的处理方式不同
- 不同模板的引用命令不同（\cite, \citep, \citet 等）
- 部分模板有特殊的摘要环境
- 部分模板需要特定的宏包声明
