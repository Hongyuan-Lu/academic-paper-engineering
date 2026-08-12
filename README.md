# Academic Paper Engineering

[中文](#中文文档) | [English](#english-document)

---

# 中文文档

## 项目简介

**科研论文智能排版与工程化 Skill** —— 将异构科研论文材料（DOCX / PDF / Markdown / LaTeX / PPTX / XLSX）转化为结构正确、语义忠实、可编译的 LaTeX 工程。支持中英学术翻译（可选）、8+1 种期刊模板适配与迁移、自定义模板上传、图表公式参考文献处理、自动编译与 12 项质量审查。

这是一个面向 AI Agent 的 Skill，核心设计原则是：**LaTeX 工程化排版是核心能力，翻译是可选环节。**

## 核心特性

- **多格式输入**：支持 DOCX、PDF、Markdown、TXT、LaTeX、ZIP、PPTX、XLSX 等 8 种文档格式
- **中英学术翻译**：按章节类型加载专用翻译提示词，支持术语词典、翻译记忆、风格记忆
- **8+1 期刊模板**：内置 Elsevier、Springer、MDPI、Frontiers、Taylor & Francis、Wiley、arXiv 等 8 套模板，另含 IEEE 规范定义
- **模板迁移**：支持 LaTeX → LaTeX 跨模板迁移（如 IEEE → Elsevier）
- **资产管理**：图片匹配（5 级优先级）、表格结构化解析、公式精确保持、参考文献权威处理
- **自动编译**：pdflatex/xelatex 双引擎，bibtex 参考文献，最多 3 轮编译
- **质量审查**：12 项 QA 检查，覆盖翻译质量、LaTeX 规范、引用一致性、资产完整性
- **文档中间表示（Document IR）**：所有处理基于结构化 IR，禁止直接将原始内容转化为最终 LaTeX

## 目录结构

```
学术论文翻译和排版/                     # GitHub 仓库
├── .gitignore
├── README.md                         # 本文件
├── LICENSE
│
└── academic-paper-engineering/       # Skill 主目录
    ├── SKILL.md                      # Skill 主定义文件
    │
    ├── references/                   # 参考文档（AI Agent 读取）
│   ├── config/                       # 系统配置
│   │   ├── system.yaml               # 系统配置（模板路径、编译配置、输出结构）
│   │   ├── task_modes.yaml           # 6 种任务模式定义与路由规则
│   │   └── thresholds.yaml           # 质量阈值（图片匹配、翻译质量、编译警告）
│   ├── prompts/                      # 处理提示词
│   │   ├── router.md                 # 任务路由与识别
│   │   ├── document_analysis.md      # 文档结构解析
│   │   ├── translation/              # 翻译提示词（12 个，按章节类型）
│   │   ├── latex/                    # LaTeX 提示词（7 个）
│   │   ├── assets/                   # 资产处理提示词（5 个）
│   │   ├── references/               # 参考文献处理
│   │   └── qa/                       # 质量检查提示词（3 个）
│   ├── rules/                        # 处理规则（7 个）
│   │   ├── core_rules.md             # 核心规则
│   │   ├── terminology.md            # 术语规则
│   │   ├── citation_rules.md         # 引用规则
│   │   ├── figure_rules.md           # 图片规则
│   │   ├── table_rules.md            # 表格规则
│   │   ├── equation_rules.md         # 公式规则
│   │   └── latex_rules.md            # LaTeX 规则
│   └── schemas/                      # JSON Schema 定义
│       ├── document_ir.json          # 文档 IR 模式
│       ├── figure.json               # 图片模式
│       ├── table.json                # 表格模式
│       ├── reference.json            # 参考文献模式
│       └── task.json                 # 任务模式
│
├── assets/                           # 静态资源（LaTeX 模板）
│   └── templates/                    # LaTeX 期刊模板
│       ├── Elsevier/                 # elsarticle 模板
│       ├── Cell-Press/               # CAS 模板（Cell Press 期刊）
│       ├── Springer/                 # sn-jnl 模板
│       ├── MDPI/                     # mdpi.cls 模板
│       ├── Frontiers/                # Harvard/Vancouver 模板
│       ├── Taylor-Francis/           # interact.cls 模板
│       ├── Wiley/                    # Wiley-authoringtemplate
│       ├── arXiv/                    # NeurIPS 2018 模板
│       └── CHEATSHEET.md             # 模板速查表
│
├── src/                              # Python 核心引擎库
│   ├── parsers/                      # 文档解析器（6 个）
│   ├── processors/                   # 内容处理器（6 个）
│   ├── latex/                        # LaTeX 引擎（渲染器、编译器、验证器）
│   └── qa/                           # 质量检查器（4 个）
│
├── scripts/                          # 文档处理脚本
│   ├── docx/                         # Word 文档处理
│   ├── pdf/                          # PDF 表单与转换
│   ├── pptx/                         # PPT 幻灯片处理
│   ├── xlsx/                         # Excel 数据表处理
│   └── common/                       # Office 公共模块（验证器、XSD 模式）
│
├── examples/                         # 使用示例
│   ├── latex_only/                   # 仅 LaTeX 排版示例
│   ├── translation_only/             # 仅翻译示例
│   ├── translation_latex/            # 翻译 + LaTeX 排版示例
│   ├── template_migration/           # 模板迁移示例
│   └── complex_paper/                # 复杂论文完整处理示例
│
└── tests/                            # 测试套件
    ├── test_parsers/                 # 解析器测试
    ├── test_translation/             # 翻译测试
    ├── test_figures/                 # 图片管理测试
    ├── test_tables/                  # 表格管理测试
    ├── test_references/              # 参考文献测试
    ├── test_latex/                   # LaTeX 渲染测试
    └── test_end_to_end/              # 端到端工作流测试
```

## 任务模式

系统支持 6 种任务模式，根据用户输入自动路由：

| 模式 | 说明 | 翻译 | LaTeX | 模板分析 |
|------|------|------|-------|---------|
| `LATEX_ONLY` | 仅排版，将已有内容排版为 LaTeX 工程 | 否 | 是 | 是 |
| `TRANSLATION_ONLY` | 仅翻译，中文学术内容翻译为英文 | 是 | 否 | 否 |
| `TRANSLATION_AND_LATEX` | 翻译 + 排版，中文翻译为英文并排版 | 是 | 是 | 是 |
| `TEMPLATE_MIGRATION` | 模板迁移，LaTeX 工程跨模板转换 | 否 | 是 | 是 |
| `DOCUMENT_TO_LATEX` | 文档转 LaTeX，DOCX/PDF等转 LaTeX | 否 | 是 | 是 |
| `ASSET_PROCESSING` | 资产处理，图表公式参考文献提取 | 否 | 可选 | 否 |

## 支持的输入格式

| 类型 | 格式 |
|------|------|
| 文档 | `.docx` `.pdf` `.md` `.txt` `.tex` `.zip` `.pptx` `.xlsx` |
| 图片 | `.png` `.jpg` `.jpeg` `.tif` `.tiff` `.svg` `.webp` |
| LaTeX 资产 | `.cls` `.sty` `.bib` `.bst` |

## 内置期刊模板

| 期刊/出版商 | 文档类 | 引用引擎 | 目录 |
|------------|--------|---------|------|
| Elsevier (elsarticle) | `elsarticle` | bibtex, biber | `assets/templates/Elsevier/` |
| Cell Press | `cas-sc` / `cas-dc` | bibtex | `assets/templates/Cell-Press/` |
| Springer | `sn-jnl` | bibtex | `assets/templates/Springer/` |
| MDPI | `mdpi` | bibtex | `assets/templates/MDPI/` |
| Frontiers | `FrontiersinHarvard` / `FrontiersinVancouver` | bibtex | `assets/templates/Frontiers/` |
| Taylor & Francis | `interact` | bibtex | `assets/templates/Taylor-Francis/` |
| Wiley | `Wiley-authoringtemplate` | bibtex | `assets/templates/Wiley/` |
| arXiv (NeurIPS) | `article` | bibtex, biber | `assets/templates/arXiv/` |
| IEEE | `IEEEtran` | bibtex | 规范定义（无模板文件） |

## 工作流程

```
用户输入
  ↓
输入检查 → 任务识别（6 种模式自动路由）
  ↓
文档解析（DOCX/PDF/Markdown/LaTeX/PPTX/XLSX）
  ↓
文档结构分析 → 学术文档 IR（中间表示）
  ↓
可选内容转换（中英学术翻译）
  ↓
资产处理（图片匹配 / 表格解析 / 公式保持 / 参考文献管理）
  ↓
模板分析 → 文档-模板映射
  ↓
LaTeX 渲染（模板驱动）
  ↓
编译（pdflatex/xelatex + bibtex，最多 3 轮）
  ↓
质量检查（12 项 QA）
  ↓
最终工程交付
```

## 输出工程结构

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

## 配置说明

### 系统配置 (`references/config/system.yaml`)

- 支持的输入格式与语言
- 内置模板路径与引用引擎
- 文档解析脚本路径
- Python 模块路径
- 编译配置（引擎：pdflatex，备选：xelatex，超时：120s）
- 输出工程目录结构

### 质量阈值 (`references/config/thresholds.yaml`)

| 检查项 | 阈值 |
|--------|------|
| 图片自动插入置信度 | ≥ 0.85 |
| 图片插入但警告 | 0.60 - 0.85 |
| 术语准确率 | ≥ 0.95 |
| 数字准确率 | 100% |
| 引用准确率 | 100% |
| 结构保持率 | ≥ 0.98 |
| 参考文献自动关联 | ≥ 0.90 |
| 编译错误数 | 0 |
| 编译警告上限 | 10 |

## 编译配置

| 配置项 | 值 |
|--------|---|
| 主引擎 | `pdflatex` |
| 备选引擎 | `xelatex` |
| 参考文献工具 | `bibtex` |
| 最大编译轮数 | 3 |
| 超时时间 | 120 秒 |

## 测试

```bash
cd academic-paper-engineering/tests && python -m pytest -v
```

测试覆盖 7 个模块：

| 测试模块 | 测试内容 |
|---------|---------|
| `test_parsers` | Markdown 解析器 |
| `test_translation` | 翻译处理器 |
| `test_figures` | 图片管理器 |
| `test_tables` | 表格管理器 |
| `test_references` | 参考文献管理器 |
| `test_latex` | LaTeX 渲染器 |
| `test_end_to_end` | 端到端工作流 |

## 示例

| 示例 | 说明 |
|------|------|
| `examples/latex_only/` | 英文论文 → LaTeX 工程 |
| `examples/translation_only/` | 中文论文 → 英文翻译 |
| `examples/translation_latex/` | 中文论文 → 英文翻译 → LaTeX 工程 |
| `examples/template_migration/` | IEEE 格式 → Elsevier 格式迁移 |
| `examples/complex_paper/` | DOCX + XLSX + PPTX → 完整 LaTeX 工程 |

## 核心设计原则

1. **五阶段分离**：文档理解 → 内容转换 → 资产管理 → LaTeX 渲染 → 质量保证
2. **Document IR 优先**：禁止直接将原始内容转化为最终 LaTeX，必须先构建结构化中间表示
3. **模板驱动渲染**：当模板已提供规则时，禁止硬编码期刊特定规则
4. **翻译可选**：永远不要假设翻译是必需的
5. **忠实处理**：禁止编造作者、标题、DOI 等参考文献信息；禁止翻译数学变量；禁止静默修改表格数值
6. **编译透明**：编译失败不得向用户隐藏

## 联系方式

如有任何问题、建议或合作意向，请通过以下方式联系：

- 邮箱: hongyuanlu9@gmail.com
- GitHub Issues: [项目 Issues 页面](https://github.com/Hongyuan-Lu/academic-paper-engineering/issues)

欢迎提交 Issue 或 Pull Request！

---

# English Document

## Overview

**Academic Paper Engineering Skill** — Transform heterogeneous research paper materials (DOCX / PDF / Markdown / LaTeX / PPTX / XLSX) into structurally correct, semantically faithful, compilable LaTeX projects. Supports optional Chinese-English academic translation, 8+1 journal template adaptation and migration, custom template upload, figure/table/equation/reference processing, automatic compilation, and 12-item quality assurance.

This is an AI Agent-oriented Skill. The core design principle: **LaTeX engineering is the primary capability; translation is an optional step.**

## Key Features

- **Multi-format Input**: Supports 8 document formats including DOCX, PDF, Markdown, TXT, LaTeX, ZIP, PPTX, XLSX
- **Chinese-English Academic Translation**: Section-specific translation prompts with terminology dictionary, translation memory, and style memory
- **8+1 Journal Templates**: Built-in templates for Elsevier, Springer, MDPI, Frontiers, Taylor & Francis, Wiley, arXiv, plus IEEE specification
- **Template Migration**: LaTeX-to-LaTeX cross-template migration (e.g., IEEE → Elsevier)
- **Asset Management**: Figure matching (5-level priority), table structured parsing, equation precise preservation, reference authoritative handling
- **Automatic Compilation**: pdflatex/xelatex dual-engine, bibtex references, up to 3 compilation passes
- **Quality Assurance**: 12-item QA checks covering translation quality, LaTeX compliance, citation consistency, and asset integrity
- **Document IR**: All processing based on structured Intermediate Representation — no direct raw-to-LaTeX conversion allowed

## Directory Structure

```
Academic Paper Engineering (repo root)
├── .gitignore
├── README.md                         # This file
├── LICENSE
│
└── academic-paper-engineering/       # Skill directory
    ├── SKILL.md                      # Main skill definition
    │
    ├── references/                   # Reference documentation (AI-readable)
│   ├── config/                       # System configuration
│   │   ├── system.yaml               # System config (template paths, compilation, output)
│   │   ├── task_modes.yaml           # 6 task mode definitions & routing rules
│   │   └── thresholds.yaml           # Quality thresholds (figure matching, translation, compilation)
│   ├── prompts/                      # Processing prompts
│   │   ├── router.md                 # Task routing & recognition
│   │   ├── document_analysis.md      # Document structure analysis
│   │   ├── translation/              # Translation prompts (12 files, by section type)
│   │   ├── latex/                    # LaTeX prompts (7 files)
│   │   ├── assets/                   # Asset processing prompts (5 files)
│   │   ├── references/               # Reference processing
│   │   └── qa/                       # Quality check prompts (3 files)
│   ├── rules/                        # Processing rules (7 files)
│   │   ├── core_rules.md             # Core rules
│   │   ├── terminology.md            # Terminology rules
│   │   ├── citation_rules.md         # Citation rules
│   │   ├── figure_rules.md           # Figure rules
│   │   ├── table_rules.md            # Table rules
│   │   ├── equation_rules.md         # Equation rules
│   │   └── latex_rules.md            # LaTeX rules
│   └── schemas/                      # JSON Schema definitions
│       ├── document_ir.json          # Document IR schema
│       ├── figure.json               # Figure schema
│       ├── table.json                # Table schema
│       ├── reference.json            # Reference schema
│       └── task.json                 # Task schema
│
├── assets/                           # Static assets (LaTeX templates)
│   └── templates/                    # LaTeX journal templates
│       ├── Elsevier/                 # elsarticle template
│       ├── Cell-Press/               # CAS templates (Cell Press journals)
│       ├── Springer/                 # sn-jnl template
│       ├── MDPI/                     # mdpi.cls template
│       ├── Frontiers/                # Harvard/Vancouver templates
│       ├── Taylor-Francis/           # interact.cls template
│       ├── Wiley/                    # Wiley-authoringtemplate
│       ├── arXiv/                    # NeurIPS 2018 template
│       └── CHEATSHEET.md             # Template quick reference
│
├── src/                              # Python core engine library
│   ├── parsers/                      # Document parsers (6)
│   ├── processors/                   # Content processors (6)
│   ├── latex/                        # LaTeX engine (renderer, compiler, validator)
│   └── qa/                           # Quality checkers (4)
│
├── scripts/                          # Document processing scripts
│   ├── docx/                         # Word document processing
│   ├── pdf/                          # PDF form & conversion
│   ├── pptx/                         # PowerPoint slide processing
│   ├── xlsx/                         # Excel spreadsheet processing
│   └── common/                       # Shared Office modules (validators, XSD schemas)
│
├── examples/                         # Usage examples
│   ├── latex_only/                   # LaTeX-only typesetting example
│   ├── translation_only/             # Translation-only example
│   ├── translation_latex/            # Translation + LaTeX example
│   ├── template_migration/           # Template migration example
│   └── complex_paper/                # Complex paper full processing example
│
└── tests/                            # Test suite
    ├── test_parsers/                 # Parser tests
    ├── test_translation/             # Translation tests
    ├── test_figures/                 # Figure manager tests
    ├── test_tables/                  # Table manager tests
    ├── test_references/              # Reference manager tests
    ├── test_latex/                   # LaTeX renderer tests
    └── test_end_to_end/              # End-to-end workflow tests
```

## Task Modes

The system supports 6 task modes with automatic routing based on user input:

| Mode | Description | Translation | LaTeX | Template Analysis |
|------|-------------|-------------|-------|-------------------|
| `LATEX_ONLY` | Typesetting only — convert content to LaTeX project | No | Yes | Yes |
| `TRANSLATION_ONLY` | Translation only — Chinese to English academic translation | Yes | No | No |
| `TRANSLATION_AND_LATEX` | Translation + typesetting — translate then render LaTeX | Yes | Yes | Yes |
| `TEMPLATE_MIGRATION` | Template migration — LaTeX-to-LaTeX cross-template conversion | No | Yes | Yes |
| `DOCUMENT_TO_LATEX` | Document to LaTeX — convert DOCX/PDF/etc. to LaTeX | No | Yes | Yes |
| `ASSET_PROCESSING` | Asset processing — extract figures, tables, equations, references | No | Optional | No |

## Supported Input Formats

| Type | Formats |
|------|---------|
| Documents | `.docx` `.pdf` `.md` `.txt` `.tex` `.zip` `.pptx` `.xlsx` |
| Images | `.png` `.jpg` `.jpeg` `.tif` `.tiff` `.svg` `.webp` |
| LaTeX Assets | `.cls` `.sty` `.bib` `.bst` |

## Built-in Journal Templates

| Publisher | Document Class | Citation Engine | Directory |
|-----------|---------------|-----------------|-----------|
| Elsevier (elsarticle) | `elsarticle` | bibtex, biber | `assets/templates/Elsevier/` |
| Cell Press | `cas-sc` / `cas-dc` | bibtex | `assets/templates/Cell-Press/` |
| Springer | `sn-jnl` | bibtex | `assets/templates/Springer/` |
| MDPI | `mdpi` | bibtex | `assets/templates/MDPI/` |
| Frontiers | `FrontiersinHarvard` / `FrontiersinVancouver` | bibtex | `assets/templates/Frontiers/` |
| Taylor & Francis | `interact` | bibtex | `assets/templates/Taylor-Francis/` |
| Wiley | `Wiley-authoringtemplate` | bibtex | `assets/templates/Wiley/` |
| arXiv (NeurIPS) | `article` | bibtex, biber | `assets/templates/arXiv/` |
| IEEE | `IEEEtran` | bibtex | Specification only (no template files) |

## Workflow

```
User Input
  ↓
Input Check → Task Recognition (auto-routing across 6 modes)
  ↓
Document Parsing (DOCX/PDF/Markdown/LaTeX/PPTX/XLSX)
  ↓
Document Structure Analysis → Academic Document IR (Intermediate Representation)
  ↓
Optional Content Transformation (Chinese-English Academic Translation)
  ↓
Asset Processing (Figure Matching / Table Parsing / Equation Preservation / Reference Management)
  ↓
Template Analysis → Document-Template Mapping
  ↓
LaTeX Rendering (Template-Driven)
  ↓
Compilation (pdflatex/xelatex + bibtex, up to 3 passes)
  ↓
Quality Check (12-item QA)
  ↓
Final Project Delivery
```

## Output Project Structure

```
paper_project/
├── main.tex               # Main file
├── sections/              # Section files
├── figures/               # Figure files
├── tables/                # Table files
├── references.bib         # Bibliography
├── template/              # Template files (.cls, .sty, .bst)
├── translation/           # Translation output (if translation performed)
│   └── translated_paper.md
└── QA/
    ├── quality_report.md          # Quality report
    ├── terminology_dictionary.json # Terminology dictionary
    ├── translation_memory.json     # Translation memory
    └── style_profile.json          # Style profile
```

## Configuration

### System Configuration (`references/config/system.yaml`)

- Supported input formats and languages
- Built-in template paths and citation engines
- Document parsing script paths
- Python module paths
- Compilation config (engine: pdflatex, fallback: xelatex, timeout: 120s)
- Output project directory structure

### Quality Thresholds (`references/config/thresholds.yaml`)

| Check Item | Threshold |
|------------|-----------|
| Figure auto-insert confidence | ≥ 0.85 |
| Figure insert with warning | 0.60 - 0.85 |
| Terminology accuracy | ≥ 0.95 |
| Number accuracy | 100% |
| Citation accuracy | 100% |
| Structure preservation | ≥ 0.98 |
| Reference auto-linking | ≥ 0.90 |
| Compilation errors | 0 |
| Max compilation warnings | 10 |

## Compilation Configuration

| Config | Value |
|--------|-------|
| Primary engine | `pdflatex` |
| Fallback engine | `xelatex` |
| Bibliography tool | `bibtex` |
| Max compilation passes | 3 |
| Timeout | 120 seconds |

## Testing

```bash
cd academic-paper-engineering/tests && python -m pytest -v
```

Tests cover 7 modules:

| Test Module | Content |
|-------------|---------|
| `test_parsers` | Markdown parser |
| `test_translation` | Translation processor |
| `test_figures` | Figure manager |
| `test_tables` | Table manager |
| `test_references` | Reference manager |
| `test_latex` | LaTeX renderer |
| `test_end_to_end` | End-to-end workflow |

## Examples

| Example | Description |
|---------|-------------|
| `examples/latex_only/` | English paper → LaTeX project |
| `examples/translation_only/` | Chinese paper → English translation |
| `examples/translation_latex/` | Chinese paper → English translation → LaTeX project |
| `examples/template_migration/` | IEEE format → Elsevier format migration |
| `examples/complex_paper/` | DOCX + XLSX + PPTX → Complete LaTeX project |

## Core Design Principles

1. **Five-Stage Separation**: Document Understanding → Content Transformation → Asset Management → LaTeX Rendering → Quality Assurance
2. **Document IR First**: No direct raw-to-LaTeX conversion — structured Intermediate Representation must be built first
3. **Template-Driven Rendering**: When a template provides rules, hardcoding journal-specific rules is prohibited
4. **Translation is Optional**: Never assume translation is required
5. **Faithful Processing**: Do not fabricate authors, titles, DOIs, or other reference information; do not translate mathematical variables; do not silently modify table values
6. **Compilation Transparency**: Compilation failures must not be hidden from the user

## Python Module Index

### Parsers (`src/parsers/`)

| Module | Class | Description |
|--------|-------|-------------|
| `docx_parser.py` | `DocxParser` | DOCX document parser |
| `pdf_parser.py` | `PdfParser` | PDF document parser |
| `markdown_parser.py` | `MarkdownParser` | Markdown document parser |
| `latex_parser.py` | `LatexParser` | LaTeX document parser |
| `pptx_parser.py` | `PptxParser` | PPTX slide parser |
| `xlsx_parser.py` | `XlsxParser` | XLSX spreadsheet parser |

### Processors (`src/processors/`)

| Module | Class | Description |
|--------|-------|-------------|
| `document_ir.py` | `DocumentIRManager` | Document IR manager |
| `translator.py` | `Translator` | Translation processor |
| `reference_manager.py` | `ReferenceManager` | Reference manager |
| `figure_manager.py` | `FigureManager` | Figure manager |
| `table_manager.py` | `TableManager` | Table manager |
| `equation_manager.py` | `EquationManager` | Equation manager |

### LaTeX Engine (`src/latex/`)

| Module | Class | Description |
|--------|-------|-------------|
| `renderer.py` | `LatexRenderer` | LaTeX renderer |
| `compiler.py` | `LatexCompiler` | LaTeX compiler |
| `validator.py` | `LatexValidator` | LaTeX validator |

### Quality Assurance (`src/qa/`)

| Module | Class | Description |
|--------|-------|-------------|
| `checker.py` | `QAChecker` | Main QA checker |
| `citation_checker.py` | `CitationChecker` | Citation checker |
| `asset_checker.py` | `AssetChecker` | Asset checker |
| `report.py` | `QAReport` | Report generator |

## License

This project is provided as-is for academic and research purposes.

## Contact

For any questions, suggestions, or collaboration inquiries, please reach out via:

- Email: hongyuanlu9@gmail.com
- GitHub Issues: [Project Issues Page](https://github.com/Hongyuan-Lu/academic-paper-engineering/issues)

Issues and Pull Requests are welcome!
