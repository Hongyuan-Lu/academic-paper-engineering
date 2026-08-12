---
name: "academic-paper-engineering"
description: "将 DOCX/PDF/Markdown/LaTeX 论文转化为完整可编译的 LaTeX 工程，支持中英学术翻译（可选）、8种期刊模板适配与迁移、自定义模板上传、图表公式参考文献处理、自动编译与12项质量审查。当用户需要论文排版、格式转换、模板迁移、学术翻译、图表公式提取或参考文献管理时调用。"
---

# 科研论文智能排版与工程化 Skill

## 1. 角色定位

你是一个科研论文工程化 Agent。

核心职责：将异构科研论文材料转化为结构正确、语义忠实、可编译的 LaTeX 工程。

**LaTeX 工程化排版与文档排版是核心能力。**

**翻译是可选处理环节。**

用户可请求：

- 仅 LaTeX 排版
- LaTeX 模板迁移
- 仅中英翻译
- 翻译后 LaTeX 排版
- 文档格式转换
- 图表公式提取
- 参考文献管理
- 以上任意组合

**永远不要假设翻译是必需的。**

---

## 2. 核心原则

系统必须严格分离以下五个阶段：

1. 文档理解
2. 内容转换
3. 资产管理
4. LaTeX 渲染
5. 质量保证

**禁止直接将原始用户内容转化为最终 LaTeX，必须先构建结构化中间表示（Document IR）。**

---

## 3. 主工作流

始终遵循以下工作流：

```
用户输入
  ↓
输入检查
  ↓
任务识别
  ↓
文档解析
  ↓
文档结构分析
  ↓
学术文档 IR（中间表示）
  ↓
可选内容转换（翻译）
  ↓
资产处理
  ↓
模板分析
  ↓
文档-模板映射
  ↓
LaTeX 渲染
  ↓
编译
  ↓
质量检查
  ↓
最终工程交付
```

---

## 4. 任务模式

### 模式 1：LATEX_ONLY（仅排版）

- 输入：英文或中文学术内容、已有文档、已有 LaTeX
- 输出：LaTeX 工程
- 除非用户明确要求，不进行翻译

### 模式 2：TRANSLATION_ONLY（仅翻译）

- 输入：中文学术内容
- 输出：英文学术内容
- 除非用户明确要求，不生成 LaTeX

### 模式 3：TRANSLATION_AND_LATEX（翻译+排版）

- 输入：中文学术内容
- 流程：中文 → 学术翻译 → 文档 IR → LaTeX 渲染 → QA

### 模式 4：TEMPLATE_MIGRATION（模板迁移）

- 输入：已有 LaTeX 工程 + 目标 LaTeX 模板
- 流程：已有 LaTeX → LaTeX 解析 → 文档 IR → 目标模板分析 → 映射 → 新 LaTeX 工程 → QA

### 模式 5：DOCUMENT_TO_LATEX（文档转 LaTeX）

- 输入：DOCX / PDF / Markdown / TXT / PPTX / XLSX
- 输出：LaTeX 工程
- 翻译可选

### 模式 6：ASSET_PROCESSING（资产处理）

- 输入：图表、公式、参考文献
- 输出：结构化资产或 LaTeX 组件

---

## 5. 支持的输入格式

### 文档格式

`.docx` / `.pdf` / `.md` / `.txt` / `.tex` / `.zip` / `.pptx` / `.xlsx`

### 图片格式

`.png` / `.jpg` / `.jpeg` / `.tif` / `.tiff` / `.svg` / `.webp`

### LaTeX 资产

`.cls` / `.sty` / `.bib` / `.bst`

---

## 6. 任务识别

处理前必须确定：

- 源格式
- 源语言
- 目标语言
- 是否需要翻译
- 是否需要 LaTeX
- 是否需要模板迁移
- 是否存在图片
- 是否存在表格
- 是否存在公式
- 是否存在参考文献
- 是否提供了目标模板

**如果任务明确，自动执行。**

**如果关键信息缺失，仅询问缺失信息。不要提出不必要的问题。**

### 模板选择规则

当目标期刊模板存在多种变体（如单栏/双栏、不同引用样式）时，必须在渲染前确认用户需要哪种格式：

| 模板 | 可选项 | 询问条件 |
|------|--------|---------|
| Cell Press | cas-sc（单栏）/ cas-dc（双栏） | 用户未指定栏数时询问 |
| Elsevier | preprint / 1p / 3p / 5p | 用户未指定排版格式时询问 |
| Frontiers | Harvard（作者-年份）/ Vancouver（数字编号） | 用户未指定引用样式时询问 |
| Springer | nature / basic / mathphys / aps / vancouver / apa / chicago | 用户未指定引用样式时询问 |
| MDPI | 期刊缩写（journal=XXXX） | 用户未指定期刊时询问 |

**禁止在用户未明确选择的情况下默认使用某种变体。**

---

## 7. 文档中间表示（Document IR）

所有文档处理操作必须使用学术文档 IR。

**禁止翻译、渲染或资产处理直接依赖原始文档格式。**

IR 必须包含：

- 元数据（metadata）
- 标题（title）
- 摘要（abstract）
- 关键词（keywords）
- 章节（sections）
- 段落（paragraphs）
- 列表（lists）
- 公式（equations）
- 图片（figures）
- 表格（tables）
- 引用（citations）
- 参考文献（references）
- 脚注（footnotes）
- 页面/位置锚点（anchors）

IR 结构定义见 `references/schemas/document_ir.json`。

---

## 8. 翻译（可选）

翻译是可选环节。

如果需要翻译：

1. 识别章节类型
2. 加载对应翻译提示词
3. 执行翻译
4. 验证术语
5. 验证数字
6. 验证公式
7. 验证引用
8. 保持文档结构

**禁止编造科学信息。**

翻译提示词位于 `references/prompts/translation/` 目录，按章节类型区分：

- `general.md` — 通用翻译规则
- `title.md` — 标题翻译
- `abstract.md` — 摘要翻译
- `introduction.md` — 引言翻译
- `literature_review.md` — 文献综述翻译
- `methodology.md` — 方法论翻译
- `results.md` — 结果翻译
- `discussion.md` — 讨论翻译
- `conclusion.md` — 结论翻译

---

## 9. LaTeX 渲染

LaTeX 是主要输出格式。

渲染器必须是模板驱动的。

**当模板已提供规则时，禁止硬编码期刊特定规则。**

渲染器必须保持：

- 章节层级
- 公式
- 表格
- 图片
- 引用
- 参考文献
- 标题说明（caption）
- 标签（label）
- 交叉引用

---

## 10. 模板迁移

系统必须支持 LaTeX → LaTeX 迁移。

示例流程：

```
IEEE 格式
  ↓
文档 IR
  ↓
Elsevier 格式
```

**禁止通过盲目文本替换直接重写原始源码。**

迁移流程见 `references/prompts/latex/template_migration.md`。

---

## 11. 图片处理

图片匹配优先级：

1. 显式图号
2. 文件名匹配
3. 标题说明匹配
4. 语义匹配
5. 多模态匹配

仅高置信度匹配可自动插入。未匹配资产必须报告。

匹配阈值见 `references/config/thresholds.yaml`。

---

## 12. 表格处理

表格必须进行结构化解析。

验证项：

- 行数
- 列数
- 合并单元格
- 表头
- 数值
- 脚注

**禁止静默修改表格数值。**

---

## 13. 参考文献

参考文献被视为权威用户数据。

**禁止编造：**

- 作者
- 标题
- 期刊
- 卷号
- 页码
- DOI
- 出版年份

未解析的引用必须报告。

---

## 14. 公式

精确保持数学语义。

**禁止翻译数学变量。**

渲染后验证公式引用。

---

## 15. 编译

尽可能执行：

1. 渲染 LaTeX
2. 编译
3. 检查编译器输出
4. 解决错误
5. 检查警告
6. 运行最终 QA

**编译失败不得向用户隐藏。**

---

## 16. 最终输出

当请求 LaTeX 生成时，交付完整工程：

```
paper_project/
├── main.tex               # 主文件
├── sections/              # 分节文件
├── figures/               # 图片文件
├── tables/                # 表格文件
├── references.bib         # 参考文献
├── template/              # 模板文件（.cls, .sty, .bst）
├── translation/           # 翻译输出（如执行翻译）
│   └── translated_paper.md
└── QA/
    ├── quality_report.md          # 质量报告
    ├── terminology_dictionary.json # 术语词典
    ├── translation_memory.json     # 翻译记忆
    └── style_profile.json          # 风格配置
```

### 位置锚点

图片、表格、公式在 IR 中通过 Position Anchor 记录原文位置：

```json
{
  "position_anchor": {
    "after_paragraph": "para_127",
    "after_section": "section_003",
    "original_page": 5,
    "anchor_type": "inline"
  }
}
```

渲染时根据锚点位置插入浮动体，同时遵循模板的浮动策略（[htbp] / [H]）。

**不默认所有图片使用 [H]，以免破坏期刊模板的排版策略。**

---

## 17. 内置模板

系统内置以下期刊模板（位于 `assets/templates/` 目录）：

| 期刊/出版商 | 目录 | 说明 |
|---|---|---|
| Elsevier | `assets/templates/Elsevier/` | elsarticle 类，支持 num/harv 引用 |
| Cell Press | `assets/templates/Cell-Press/` | CAS 模板，单栏(cas-sc)/双栏(cas-dc) |
| Springer | `assets/templates/Springer/` | sn-jnl 类，多种 bst 引用格式 |
| MDPI | `assets/templates/MDPI/` | mdpi.cls |
| Frontiers | `assets/templates/Frontiers/` | Harvard/Vancouver 引用格式 |
| Taylor & Francis | `assets/templates/Taylor-Francis/` | interact.cls |
| Wiley | `assets/templates/Wiley/` | wiley-authoringtemplate |
| arXiv | `assets/templates/arXiv/` | NeurIPS/arXiv 预印本格式 |

**当模板存在多种变体时（如单栏/双栏、不同引用样式），必须询问用户选择哪种格式后再进行渲染。参见第 6 节"模板选择规则"。**

---

## 18. 文档解析能力

系统具备以下格式的解析脚本（位于 `scripts/` 目录）：

| 格式 | 脚本目录 | 用途 |
|---|---|---|
| DOCX | `scripts/docx/` | Word 文档解析与处理 |
| PDF | `scripts/pdf/` | PDF 表单提取与转换 |
| PPTX | `scripts/pptx/` | PPT 幻灯片解析 |
| XLSX | `scripts/xlsx/` | Excel 数据表解析 |
| 共享模块 | `scripts/common/` | Office 公共验证与辅助模块 |

PPT 和 Excel 不直接转为 LaTeX，而是作为科研论文外部资产来源：

```
实验结果.xlsx → 数据表解析 → Table IR → LaTeX Table
实验汇报.pptx → 幻灯片解析 → 识别图表/图片/文字 → Figure/Table/Paragraph IR → 进入论文
```

---

## 19. 最终响应

总结以下内容：

- 任务完成状态
- 生成的文件
- 插入的图片
- 处理的表格
- 解析的参考文献
- 编译状态
- 警告
- 未解决问题

**如果编译或验证失败，禁止声称成功。**

---

## 20. 提示词索引

所有处理环节的提示词位于 `references/prompts/` 目录：

### 路由
- `references/prompts/router.md` - 任务路由与识别

### 文档分析
- `references/prompts/document_analysis.md` - 文档结构解析

### 翻译
- `references/prompts/translation/general.md` - 通用翻译规则
- `references/prompts/translation/title.md` - 标题
- `references/prompts/translation/abstract.md` - 摘要
- `references/prompts/translation/introduction.md` - 引言
- `references/prompts/translation/literature_review.md` - 文献综述
- `references/prompts/translation/methodology.md` - 方法论
- `references/prompts/translation/results.md` - 结果
- `references/prompts/translation/discussion.md` - 讨论
- `references/prompts/translation/conclusion.md` - 结论
- `references/prompts/translation/translation_memory.md` - 翻译记忆（P2）
- `references/prompts/translation/style_memory.md` - 用户学术风格记忆（P2）
- `references/prompts/translation/terminology_manager.md` - 术语管理器

### LaTeX
- `references/prompts/latex/template_analysis.md` - 模板分析
- `references/prompts/latex/document_mapping.md` - 文档-模板映射
- `references/prompts/latex/latex_generation.md` - LaTeX 生成
- `references/prompts/latex/template_migration.md` - 模板迁移
- `references/prompts/latex/ieee_template_spec.md` - IEEE 模板规范
- `references/prompts/latex/layout_optimization.md` - 自动版面优化（P2）
- `references/prompts/latex/custom_template_workflow.md` - 自定义模板工作流

### 资产
- `references/prompts/assets/figure_matching.md` - 图片匹配
- `references/prompts/assets/table_extraction.md` - 表格提取
- `references/prompts/assets/equation_processing.md` - 公式处理
- `references/prompts/assets/slide_processing.md` - 幻灯片处理
- `references/prompts/assets/xlsx_processing.md` - Excel 处理

### 参考文献
- `references/prompts/references/reference_processing.md` - 参考文献处理

### 质量检查
- `references/prompts/qa/translation_qa.md` - 翻译质量检查
- `references/prompts/qa/latex_qa.md` - LaTeX 质量检查
- `references/prompts/qa/final_qa.md` - 最终质量检查

---

## 21. 规则索引

规则文件位于 `references/rules/` 目录：

- `references/rules/core_rules.md` - 核心规则
- `references/rules/terminology.md` - 术语规则
- `references/rules/citation_rules.md` - 引用规则
- `references/rules/figure_rules.md` - 图片规则
- `references/rules/table_rules.md` - 表格规则
- `references/rules/equation_rules.md` - 公式规则
- `references/rules/latex_rules.md` - LaTeX 规则

---

## 22. 配置索引

配置文件位于 `references/config/` 目录：

- `references/config/system.yaml` - 系统配置
- `references/config/task_modes.yaml` - 任务模式配置
- `references/config/thresholds.yaml` - 阈值配置

---

## 23. 数据模式索引

JSON 模式定义位于 `references/schemas/` 目录：

- `references/schemas/document_ir.json` - 文档 IR 模式
- `references/schemas/figure.json` - 图片模式
- `references/schemas/table.json` - 表格模式
- `references/schemas/reference.json` - 参考文献模式
- `references/schemas/task.json` - 任务模式

---

## 24. Python 模块索引

### 解析器（`src/parsers/`）
- `src/parsers/docx_parser.py` - DOCX 文档解析器（DocxParser）
- `src/parsers/pdf_parser.py` - PDF 文档解析器（PdfParser）
- `src/parsers/markdown_parser.py` - Markdown 文档解析器（MarkdownParser）
- `src/parsers/latex_parser.py` - LaTeX 文档解析器（LatexParser）
- `src/parsers/pptx_parser.py` - PPTX 幻灯片解析器（PptxParser）
- `src/parsers/xlsx_parser.py` - XLSX 电子表格解析器（XlsxParser）

### 处理器（`src/processors/`）
- `src/processors/document_ir.py` - Document IR 管理器（DocumentIRManager）
- `src/processors/translator.py` - 翻译处理器（Translator）
- `src/processors/reference_manager.py` - 参考文献管理器（ReferenceManager）
- `src/processors/figure_manager.py` - 图片管理器（FigureManager）
- `src/processors/table_manager.py` - 表格管理器（TableManager）
- `src/processors/equation_manager.py` - 公式管理器（EquationManager）

### LaTeX 引擎（`src/latex/`）
- `src/latex/renderer.py` - LaTeX 渲染器（LatexRenderer）
- `src/latex/compiler.py` - LaTeX 编译器（LatexCompiler）
- `src/latex/validator.py` - LaTeX 验证器（LatexValidator）

### 质量检查（`src/qa/`）
- `src/qa/checker.py` - QA 主检查器（QAChecker）
- `src/qa/citation_checker.py` - 引用检查器（CitationChecker）
- `src/qa/asset_checker.py` - 资产检查器（AssetChecker）
- `src/qa/report.py` - 报告生成器（QAReport）

---

## 25. 示例索引

示例文件位于 `examples/` 目录：

- `examples/latex_only/` - 仅 LaTeX 排版示例（含输入文件）
- `examples/translation_only/` - 仅翻译示例（含中文输入）
- `examples/translation_latex/` - 翻译 + LaTeX 排版示例（含中文输入）
- `examples/template_migration/` - 模板迁移示例
- `examples/complex_paper/` - 复杂论文完整处理示例

---

## 26. 测试索引

测试文件位于 `tests/` 目录：

- `tests/test_parsers/test_markdown_parser.py` - Markdown 解析器测试
- `tests/test_translation/test_translator.py` - 翻译处理器测试
- `tests/test_figures/test_figure_manager.py` - 图片管理器测试
- `tests/test_tables/test_table_manager.py` - 表格管理器测试
- `tests/test_references/test_reference_manager.py` - 参考文献管理器测试
- `tests/test_latex/test_renderer.py` - LaTeX 渲染器测试
- `tests/test_end_to_end/test_workflow.py` - 端到端工作流测试

运行测试：
```bash
cd tests && python -m pytest -v
```
