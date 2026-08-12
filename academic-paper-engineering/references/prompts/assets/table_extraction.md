# 表格提取代理

表格提取独立为 Table Extraction Engine，不由 LLM 直接"表格 -> LaTeX"。

## 8 步解析流程

```
Original Table（原始表格）
      ↓
Step 1: Table Structure Detection（表格结构检测）
      ↓
Step 2: Header Detection（表头检测）
      ↓
Step 3: Row / Column Detection（行列检测）
      ↓
Step 4: Merged Cell Detection（合并单元格检测）
      ↓
Step 5: Cell Content Extraction（单元格内容提取）
      ↓
Step 6: Semantic Validation（语义验证）
      ↓
Step 7: Structure Validation（结构校验）
      ↓
Step 8: LaTeX Table Generation（LaTeX 表格生成）
```

## 识别项

- 标题
- 标题说明（caption）
- 表头
- 行
- 列
- 合并单元格
- 脚注
- 单位
- 统计符号
- 上标
- 显著性标记

## 结构校验（必须执行）

表格必须进行结构校验，不能直接输出。

验证规则：

```
Header = 5 columns
Row 1 = 5 columns  ✓
Row 2 = 5 columns  ✓
Row 3 = 3 columns  ✗ -> Table structure error
```

必须验证：

```
len(row) == len(headers)
```

如果不一致，报告错误，不能直接输出。

### 验证项

1. 表头列数
2. 行列数一致性（len(row) == len(headers)）
3. 合并单元格一致性
4. 数值一致性
5. 标题说明一致性

## 数值处理规则

- 禁止修改数值
- 保持原始精度
- 保持统计标记（*, **, ***）
- 保持置信区间格式
- 保持单位格式

## 结构歧义处理

如果存在结构歧义（如不确定的合并单元格、不规则的行列结构），报告歧义而不是猜测。

## LaTeX 表格策略决策树

根据表格复杂度选择 LaTeX 环境：

```
表格列数 <= 5 且行数 <= 20？
  ├── 是 -> 简单表格
  │   └── \begin{table} + \begin{tabular} + booktabs
  │
  └── 否 -> 需要特殊处理
      ├── 列数 > 5 或列宽不均？
      │   └── tabularx（自适应列宽）
      │
      ├── 行数 > 30（跨页）？
      │   └── longtable（跨页表格）
      │
      ├── 需要表格脚注？
      │   └── threeparttable（表格脚注）
      │
      ├── 表格过宽？
      │   └── \resizebox 或 sidewaystable（旋转表格）
      │
      └── 有合并单元格？
          └── multirow + multicolumn
```

### 标准科研表格（优先策略）

普通科研表格优先使用 booktabs：

```latex
\begin{table}[htbp]
\centering
\caption{表格标题说明。}
\label{tab:example}
\begin{tabular}{lcc}
\toprule
方法 & 准确率 & F1分数 \\
\midrule
方法A & 95.3 & 0.94 \\
方法B & 92.1 & 0.91 \\
\bottomrule
\end{tabular}
\end{table}
```

### 支持的 LaTeX 表格宏包

| 宏包 | 用途 |
|---|---|
| booktabs | 专业表格线条（\toprule, \midrule, \bottomrule） |
| tabularx | 自适应列宽 |
| longtable | 跨页表格 |
| threeparttable | 表格脚注 |
| multirow | 纵向合并单元格 |
| multicolumn | 横向合并单元格 |
| rotating | 旋转表格（sidewaystable） |
| adjustbox | 表格缩放 |

## 输出格式

```json
{
  "id": "table_001",
  "number": 1,
  "caption": "表格标题说明",
  "label": "tab:example",
  "placement": "htbp",
  "position_anchor": {
    "after_paragraph": "para_045",
    "after_section": "section_003",
    "anchor_type": "float"
  },
  "headers": [
    {
      "row": 0,
      "cells": [
        {"text": "方法", "colspan": 1, "rowspan": 1},
        {"text": "准确率", "colspan": 1, "rowspan": 1}
      ]
    }
  ],
  "rows": [
    {
      "row": 1,
      "cells": [
        {"text": "方法A", "type": "text"},
        {"text": "95.3%", "type": "number"}
      ]
    }
  ],
  "footnotes": [],
  "notes": "表格脚注内容",
  "validation": {
    "column_count": 2,
    "header_columns": 2,
    "row_columns_consistent": true,
    "structure_valid": true
  },
  "latex_strategy": "tabular+booktabs"
}
```
