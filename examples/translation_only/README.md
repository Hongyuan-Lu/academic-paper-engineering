# 仅翻译示例

## 输入
- 中文学术论文 Markdown 文件

## 输出
- 英文学术内容（Markdown 格式）

## 流程
1. 解析中文 Markdown 文件为 Document IR
2. 加载通用翻译规则 `references/prompts/translation/general.md`
3. 按章节类型加载对应翻译提示词
4. 执行学术翻译
5. 验证术语一致性
6. 验证数字准确性
7. 验证公式完整性
8. 验证引用正确性
9. 翻译质量检查
10. 输出英文内容

## 注意
- 仅翻译，不生成 LaTeX
- 保持原文档结构
- 不修改数值和公式
