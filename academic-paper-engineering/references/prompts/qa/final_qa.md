# 最终学术论文质量检查

最终必须有一个 Academic Paper QA Agent，专门负责"挑错"。

## 12 项检查清单

### 1. 翻译完整性

检查所有章节是否都已翻译：
- 段落遗漏
- 章节遗漏
- 翻译不完整

### 2. 数字一致性

检查所有数字是否与原文完全一致：
- 实验数据
- 统计指标
- 百分比
- 测量值

### 3. 公式一致性

检查所有公式是否与原文一致：
- 公式内容未被修改
- 变量符号未被翻译
- 公式编号连续

### 4. 术语一致性

检查术语翻译是否全文统一：
- 对照术语词典验证
- 检查禁止替代翻译
- 术语一致性率 >= 95%

### 5. 图编号一致性

检查图片编号是否连续正确：
- 编号无遗漏
- 编号无重复
- 引用与编号匹配

### 6. 表编号一致性

检查表格编号是否连续正确：
- 编号无遗漏
- 编号无重复
- 引用与编号匹配

### 7. 引用完整性

检查所有引用是否解析：
- 每个引用有对应参考文献
- 未解析引用标记为 unresolved
- 禁止编造参考文献

### 8. 参考文献一致性

检查参考文献完整性：
- 无重复参考文献
- 引用键格式正确
- BibTeX 格式正确

### 9. 图片完整性

检查图片资产完整性：
- 图片文件存在
- 图片已正确匹配
- 标题说明存在
- 未匹配图片已报告

### 10. 表格完整性

检查表格结构完整性：
- 行列数一致
- 合并单元格正确
- 数值未被修改
- 标题说明存在

### 11. LaTeX 编译

检查 LaTeX 编译状态：
- 编译成功
- 无语法错误
- 无资源缺失
- 无引用错误
- 无交叉引用错误

### 12. LaTeX 警告

检查 LaTeX 编译警告：
- Overfull hbox 数量
- Underfull hbox 数量
- 浮动体位置警告
- 字体替换警告

## 输出

生成 `quality_report.md`。

状态：

- PASS
- PASS_WITH_WARNINGS
- FAIL

## 质量报告格式

```markdown
# Paper Translation & LaTeX QA Report

## Translation
✓ All sections translated
✓ Terminology consistency: 98.7%
✓ Numerical consistency: 100%

## References
✓ 36 citations resolved
⚠ 2 unresolved citations
  - Huang et al. (2025)
  - Wang et al. (2024)

## Figures
✓ 8 figures inserted
⚠ 1 image unmatched
  - image_07.png (Please rename to Fig8.png)

## Tables
✓ 6 tables converted
✓ No structural mismatch detected

## Equations
✓ 12 equations preserved
✓ No variable translation detected

## LaTeX
✓ Compilation successful
⚠ 3 overfull \hbox warnings

## Overall Status
PASS WITH WARNINGS
```
