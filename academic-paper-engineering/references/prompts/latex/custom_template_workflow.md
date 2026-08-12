# 自定义模板工作流

## 概述

当用户需要使用预制模板库中不存在的 LaTeX 模板时，Skill 支持用户上传自定义模板。

## 触发条件

- 用户上传 .zip 格式的模板文件
- 用户明确指定使用自定义模板
- 路由器识别 `template_source: "custom"`

## 完整工作流

```
用户上传 my_template.zip
  ↓
解压模板文件
  ↓
Template Analyzer 分析
  ↓
生成 Template Specification
  ↓
文档-模板映射
  ↓
LaTeX 渲染
  ↓
编译验证
  ↓
QA 检查
```

## 第一步：解压模板文件

用户上传的 .zip 文件通常包含：

```
my_template.zip
├── template.cls          # 文档类文件
├── template.sty          # 宏包文件（可选）
├── template.bst          # 参考文献样式文件（可选）
├── sample.tex            # 示例文档（可选）
├── references.bib        # 示例参考文献（可选）
├── figures/              # 示例图片（可选）
└── README.md             # 模板说明（可选）
```

解压后，将文件复制到输出工程的 `template/` 目录。

## 第二步：Template Analyzer 分析

对解压后的模板执行全面分析（参见 `references/prompts/latex/template_analysis.md`）。

### 必须分析的文件

| 文件类型 | 分析内容 |
|---|---|
| .cls | 文档类名称、选项、章节层级、作者格式、标题格式、摘要环境 |
| .sty | 宏包依赖、自定义命令、环境定义 |
| .bst | 参考文献格式、引用样式 |
| .tex | 文档结构示例、宏包使用、命令调用方式 |
| .bib | 参考文献格式示例 |

### 分析检查清单

- [ ] 识别文档类名称
- [ ] 识别文档类选项
- [ ] 识别所有必需宏包
- [ ] 识别参考文献引擎（bibtex/biber）
- [ ] 识别引用命令格式（\cite/\citep/\citet）
- [ ] 识别图片环境格式
- [ ] 识别表格环境格式
- [ ] 识别公式环境格式
- [ ] 识别章节层级命令
- [ ] 识别作者/标题/摘要格式
- [ ] 识别关键词命令
- [ ] 识别附录命令
- [ ] 识别致谢格式

## 第三步：生成 Template Specification

```json
{
  "template_name": "用户自定义模板",
  "template_source": "custom",
  "document_class": "从 .cls 文件识别",
  "class_options": [],
  "citation_engine": "bibtex/biber",
  "citation_style": "numeric/author-year",
  "bibliography_bst": "从 .bst 文件识别",
  "figure_environment": "figure",
  "table_environment": "table",
  "equation_environment": "equation",
  "section_levels": [],
  "required_packages": [],
  "forbidden_packages": [],
  "author_format": "从示例 .tex 识别",
  "title_format": "从示例 .tex 识别",
  "abstract_format": "从示例 .tex 识别",
  "keywords_format": "从示例 .tex 识别",
  "bibliography_command": "从示例 .tex 识别",
  "appendix_command": "从示例 .tex 识别",
  "acknowledgement_format": "从示例 .tex 识别",
  "special_commands": [],
  "constraints": []
}
```

## 第四步：文档-模板映射

使用生成的 Template Specification 进行文档-模板映射（参见 `references/prompts/latex/document_mapping.md`）。

特别注意：
- 自定义模板可能有特殊的作者格式
- 自定义模板可能有特殊的关键词命令
- 自定义模板可能有特殊的致谢/附录格式

## 第五步：LaTeX 渲染

使用 Template Specification 渲染 LaTeX 工程：
- 将模板文件（.cls, .sty, .bst）复制到 `template/` 目录
- 在 main.tex 中正确引用模板文件
- 使用模板特定的命令格式

## 第六步：编译验证

编译时特别注意：
- 自定义模板可能依赖特定的 LaTeX 发行版
- 自定义模板可能需要额外的字体文件
- 编译错误需要详细分析，因为自定义模板可能有不规范的部分

## 第七步：QA 检查

额外检查：
- Template Specification 是否完整
- 模板文件是否全部复制
- main.tex 是否正确引用了模板文件
- 编译是否成功

## 注意事项

- 分析过程中不修改用户上传的模板文件
- 如果模板文件缺失关键组件（如 .cls），必须报告
- 如果模板与标准 LaTeX 命令不兼容，必须报告
- 如果模板有特殊约束（如禁止使用某些宏包），必须在 Specification 中记录
- 自定义模板的 Template Specification 应保存在 `template/template_spec.json` 中
