# 公式规则

## 公式环境

### 行内公式

```latex
能量 $E = mc^2$ 是著名的公式。
```

### 编号公式

```latex
\begin{equation}
  E = mc^2
  \label{eq:energy}
\end{equation}
```

### 多行公式

```latex
\begin{align}
  a &= b + c \label{eq:first} \\
  d &= e + f \label{eq:second}
\end{align}
```

### 分段函数

```latex
\begin{equation}
  f(x) = \begin{cases}
    1 & \text{if } x > 0 \\
    0 & \text{otherwise}
  \end{cases}
\end{equation}
```

### 矩阵

```latex
\begin{equation}
  \mathbf{A} = \begin{pmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
  \end{pmatrix}
\end{equation}
```

## 必需宏包

```latex
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
```

## 标签命名

- 格式：eq:描述性名称
- 示例：eq:energy, eq:loss_function

## 交叉引用

```latex
如公式 \ref{eq:energy} 所示，能量与质量成正比。
```

或使用 cleveref 宏包：

```latex
如 \cref{eq:energy} 所示。
```

## 公式规则

- 禁止翻译数学变量
- 保持公式编号连续
- 保持公式语义不变
- 变量用斜体（数学模式默认）
- 向量和矩阵用粗体
- 函数名用正体（\sin, \cos, \log 等）
- 单位用正体

## 常见数学符号

| 符号 | LaTeX |
|---|---|
| 求和 | \sum |
| 积分 | \int |
| 极限 | \lim |
| 分数 | \frac{a}{b} |
| 上标 | x^2 |
| 下标 | x_i |
| 偏导 | \partial |
| 约等于 | \approx |
| 不等于 | \neq |
| 大于等于 | \geq |
| 小于等于 | \leq |
| 无穷 | \infty |
| 属于 | \in |
| 任意 | \forall |
| 存在 | \exists |
