# LaTeX 模板分析器

分析所提供的 LaTeX 模板。

## 检查项

检查以下模板组件：

- 主 .tex 文件
- .cls 文件
- .sty 文件
- .bst 文件
- .bib 文件
- 所用宏包（packages）
- 文档类（document class）
- 参考文献系统
- 引用样式
- 图片环境
- 表格环境
- 公式环境
- 章节层级
- 作者元数据格式
- 标题元数据格式
- 附录规则

## 输出

生成模板规格说明（Template Specification）。

```json
{
  "template_name": "...",
  "document_class": "...",
  "class_options": [],
  "citation_engine": "bibtex/biber",
  "citation_style": "...",
  "bibliography_bst": "...",
  "figure_environment": "figure",
  "table_environment": "table",
  "equation_environment": "equation",
  "section_levels": ["section", "subsection", "subsubsection"],
  "required_packages": [],
  "forbidden_packages": [],
  "author_format": "...",
  "title_format": "...",
  "abstract_format": "...",
  "bibliography_command": "...",
  "appendix_command": "...",
  "acknowledgement_format": "..."
}
```

## 内置模板分析

系统内置以下模板，可按需分析：

### Elsevier (elsarticle)
- 文档类：elsarticle
- 引用引擎：bibtex
- BST 文件：elsarticle-num.bst / elsarticle-harv.bst / elsarticle-num-names.bst
- 支持格式：单栏/双栏/三栏

### Elsevier CAS
- 文档类：cas-sc (单栏) / cas-dc (双栏)
- 引用引擎：bibtex
- BST 文件：cas-model2-names.bst

### Springer
- 文档类：sn-jnl
- 引用引擎：bibtex
- BST 文件：sn-basic.bst / sn-nature.bst / sn-vancouver-num.bst 等

### MDPI
- 文档类：mdpi
- 引用引擎：bibtex
- BST 文件：mdpi.bst

### Frontiers
- 文档类：FrontiersinHarvard / FrontiersinVancouver
- 引用引擎：bibtex
- BST 文件：Frontiers-Harvard.bst / Frontiers-Vancouver.bst

### Taylor & Francis
- 文档类：interact
- 引用引擎：bibtex

### Wiley
- 文档类：Wiley-authoringtemplate

### arXiv (NeurIPS)
- 文档类：article (使用 nips_2018.sty)
- 引用引擎：bibtex/biber

## 注意事项

- 分析过程中不修改模板
- 记录模板的特殊约束
- 标记不兼容的宏包
- 记录模板对图片格式的偏好
