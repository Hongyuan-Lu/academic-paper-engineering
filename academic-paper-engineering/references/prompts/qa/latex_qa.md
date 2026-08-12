# LaTeX 质量检查

对生成的 LaTeX 工程进行质量检查。

## 编译检查流程

1. 编译 LaTeX 工程
2. 检查编译器输出
3. 解决编译错误
4. 检查编译警告
5. 运行最终编译

## 五级编译检查

### Level 1：语法检查

检查 LaTeX 语法错误：

- Missing `}`
- Undefined control sequence
- Missing `$`
- 环境未闭合
- 命令参数错误

### Level 2：资源检查

检查文件资源完整性：

- 图片文件不存在
- .bib 文件不存在
- .sty 宏包缺失
- .cls 文档类缺失
- \input 引用的文件不存在

### Level 3：引用检查

检查参考文献引用：

- Undefined citation（未定义引用）
- 引用键格式不正确
- BibTeX 编译是否成功
- 每个引用是否有对应参考文献
- 每个参考文献是否被引用

### Level 4：交叉引用检查

检查交叉引用完整性：

- `?? Figure`（图片引用未定义）
- `?? Table`（表格引用未定义）
- `?? Section`（章节引用未定义）
- `?? Equation`（公式引用未定义）
- 每个标签是否被引用
- 每个引用是否有对应标签

### Level 5：版面检查

如果编译成功生成 PDF，进一步检查版面问题：

- Overfull \hbox（行溢出）
- Underfull \hbox（行间距过大）
- Table overflow（表格溢出）
- Figure overflow（图片溢出）
- Page overflow（页面溢出）

## 警告阈值

| 警告类型 | 上限 |
|---|---|
| 编译错误（Level 1-2） | 0 |
| 引用错误（Level 3） | 0 |
| 交叉引用错误（Level 4） | 0 |
| 编译警告 | <= 10 |
| Overfull hbox（Level 5） | <= 5 |
| Underfull hbox（Level 5） | <= 10 |

## 输出

```json
{
  "latex_qa": {
    "status": "PASS / PASS_WITH_WARNINGS / FAIL",
    "level_1_syntax": {
      "errors": [],
      "status": "PASS"
    },
    "level_2_resources": {
      "missing_files": [],
      "status": "PASS"
    },
    "level_3_citations": {
      "total": 25,
      "resolved": 25,
      "unresolved": 0,
      "status": "PASS"
    },
    "level_4_cross_references": {
      "total": 15,
      "resolved": 15,
      "unresolved": 0,
      "status": "PASS"
    },
    "level_5_layout": {
      "overfull_hbox": [],
      "underfull_hbox": [],
      "status": "PASS_WITH_WARNINGS"
    },
    "compilation": {
      "engine": "pdflatex",
      "passes": 3,
      "success": true
    }
  }
}
```
