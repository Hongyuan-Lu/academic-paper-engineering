# 图片规则

## 图片插入规则

### LaTeX 图片环境

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/figure1.png}
  \caption{图片标题说明。}
  \label{fig:example}
\end{figure}
```

### 图片格式

- 优先使用 PDF 或 EPS 格式（矢量图）
- PNG 适用于位图/截图
- JPG 适用于照片
- SVG 需转换为 PDF/EPS

### 图片尺寸

- 单栏图片：width = \columnwidth
- 双栏图片：width = \textwidth
- 一般不超过页面宽度

### 标签命名

- 格式：fig:描述性名称
- 示例：fig:architecture, fig:results_comparison

### 标题说明规则

- 以句号结尾
- 首字母大写（视期刊要求）
- 简洁描述图片内容
- 包含必要的图例说明

## 图片匹配规则

### 置信度阈值

| 置信度 | 操作 |
|---|---|
| >= 0.85 | 自动插入 |
| 0.60 - 0.85 | 插入但警告 |
| < 0.60 | 不自动插入 |

### 匹配优先级

1. 显式图号
2. 文件名匹配
3. 标题说明匹配
4. 上下文文本
5. 语义相似度
6. 视觉理解

## 子图规则

```latex
\begin{figure}[htbp]
  \centering
  \subfloat[子图A]{\includegraphics[width=0.45\textwidth]{fig_a.png}}
  \hfill
  \subfloat[子图B]{\includegraphics[width=0.45\textwidth]{fig_b.png}}
  \caption{总体标题说明。}
  \label{fig:example}
\end{figure}
```

## 注意事项

- 禁止编造图片关系
- 未匹配的图片必须报告
- 图片文件必须存在
- 路径使用相对路径
