# 复杂论文完整处理示例

## 输入
- 中文学术论文（DOCX）
- 实验数据（XLSX）
- 实验图片（PNG）
- 实验汇报（PPTX）

## 输出
- Elsevier CAS 格式的英文 LaTeX 工程

## 流程
1. 解析 DOCX 为 Document IR
2. 从 XLSX 提取表格数据
3. 从 PPTX 提取图片和表格
4. 匹配图片到论文
5. 学术翻译
6. 分析 Elsevier CAS 模板
7. 映射 IR 到模板
8. 渲染 LaTeX 工程
9. 编译验证
10. 全面 QA
