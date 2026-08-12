# 表格规则

## LaTeX 表格环境

```latex
\begin{table}[htbp]
  \centering
  \caption{表格标题说明。}
  \label{tab:example}
  \begin{tabular}{lcc}
    \toprule
    方法 & 准确率 & F1 分数 \\
    \midrule
    方法A & 95.3 & 0.94 \\
    方法B & 92.1 & 0.91 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## 表格排版规则

### 线条

- 使用 booktabs 宏包
- \toprule: 顶部线
- \midrule: 中间线（表头与数据之间）
- \bottomrule: 底部线
- 禁止使用 \hline（除非模板要求）
- 禁止使用竖线（除非数据需要）

### 对齐

- 文本列：左对齐 (l)
- 数值列：右对齐 (r)
- 表头：居中对齐 (c)
- 长文本：使用 p{width} 或 m{width}

### 合并单元格

- 横向合并：\multicolumn{2}{c}{标题}
- 纵向合并：\multirow{2}{*}{标题}

## 数值规则

- 禁止修改数值
- 保持原始精度
- 小数位数一致
- 统计标记保持 (*, **, ***)
- 单位保持原始格式

## 表格标题说明

- 放在表格上方（\begin{tabular} 之前）
- 以句号结尾
- 简洁描述表格内容
- 包含必要的缩写说明

## 跨页表格

使用 longtable 或 supertabular 宏包：

```latex
\begin{longtable}{lcc}
  \caption{表格标题说明。} \\
  \toprule
  方法 & 准确率 & F1 分数 \\
  \midrule
  \endfirsthead
  ...
```

## 旋转表格

使用 rotating 宏包：

```latex
\begin{sidewaystable}
  ...
\end{sidewaystable}
```

## 脚注

表格脚注使用 \multicolumn 或 minipage：

```latex
\multicolumn{3}{l}{\footnotesize 注：* p < 0.05, ** p < 0.01}
```
