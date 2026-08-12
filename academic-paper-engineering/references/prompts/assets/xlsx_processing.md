# Excel 处理代理

将 Excel 电子表格作为科研论文外部资产进行处理。

## 定位

Excel 不直接转换为 LaTeX，而是作为科研论文外部资产来源。

## 处理流程

```
Excel 文件 (.xlsx)
  ↓
数据表解析
  ↓
识别数据结构（表头/数据行/统计行）
  ↓
Table IR
  ↓
LaTeX Table
```

## 解析能力

使用 `scripts/xlsx/` 中的脚本解析 Excel 文件：

- 提取工作表（Sheet）列表
- 提取每个工作表的数据区域
- 识别表头行和数据行
- 识别合并单元格
- 提取单元格格式信息（数字格式、字体、对齐等）

## 资产提取

### 数据表提取

- 识别数据区域的起始和结束位置
- 区分表头行和数据行
- 识别汇总行（如"平均值"、"标准差"、"总计"等）
- 处理多级表头

### 统计数据提取

- 识别描述性统计（均值、标准差、中位数等）
- 识别显著性标记（*, **, ***）
- 识别置信区间
- 保持数值精度

### 多工作表处理

- 每个工作表可独立提取为一个 Table IR
- 工作表之间的关联关系需记录
- 合并多个工作表的数据时需报告

## 输出格式

```json
{
  "source_file": "实验结果.xlsx",
  "sheets": [
    {
      "sheet_name": "Sheet1",
      "table_id": "table_001",
      "data_range": "A1:D20",
      "headers": [
        {
          "row": 0,
          "cells": [
            {"text": "方法", "colspan": 1, "rowspan": 1},
            {"text": "准确率", "colspan": 1, "rowspan": 1},
            {"text": "F1分数", "colspan": 1, "rowspan": 1},
            {"text": "推理时间(ms)", "colspan": 1, "rowspan": 1}
          ]
        }
      ],
      "rows": [
        {
          "row": 1,
          "cells": [
            {"text": "方法A", "type": "text"},
            {"text": "95.3", "type": "number", "format": "0.0"},
            {"text": "0.94", "type": "number", "format": "0.00"},
            {"text": "12.5", "type": "number", "format": "0.0"}
          ]
        }
      ],
      "summary_rows": [],
      "notes": [],
      "suggested_caption": "各方法性能对比"
    }
  ]
}
```

## 数值处理规则

- 禁止修改数值
- 保持原始精度
- 保持数字格式（小数位数、科学计数法）
- 保持统计标记
- 保持单位

## LaTeX 表格生成建议

- 使用 booktabs 宏包
- 数值列右对齐
- 文本列左对齐
- 表头居中对齐
- 汇总行用 \midrule 分隔
- 多级表头使用 \multicolumn

## 注意事项

- Excel 中的公式应计算后提取结果值
- 空单元格需标记为空字符串或 N/A
- 隐藏行/列需报告
- 图表对象无法直接转为 LaTeX 表格，需报告
