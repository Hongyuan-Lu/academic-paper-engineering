# 公式处理代理

处理学术文档中的数学公式。

## 核心原则

- 精确保持数学语义
- 禁止翻译数学变量
- 保持公式编号一致性
- 渲染后验证公式引用

## 公式类型

### 1. 行内公式

嵌入文本中的公式，使用 `$ ... $` 或 `\( ... \)`。

### 2. 独立公式

单独成行的公式，使用 `$$ ... $$` 或 `\[ ... \]`。

### 3. 编号公式

带编号的公式，使用 equation 环境：

```latex
\begin{equation}
  E = mc^2
  \label{eq:energy}
\end{equation}
```

### 4. 多行公式

使用 align、gather 或 eqnarray 环境：

```latex
\begin{align}
  a &= b + c \\
  d &= e + f
\end{align}
```

### 5. 分段函数

使用 cases 环境：

```latex
\begin{equation}
  f(x) = \begin{cases}
    1 & \text{if } x > 0 \\
    0 & \text{otherwise}
  \end{cases}
\end{equation}
```

### 6. 矩阵

使用 matrix、pmatrix、bmatrix 等环境。

## 处理流程

1. 识别公式类型
2. 提取 LaTeX 源码
3. 验证语法正确性
4. 检查变量定义
5. 检查公式编号
6. 检查交叉引用
7. 生成 IR 条目

## IR 输出格式

```json
{
  "id": "equation_001",
  "number": 1,
  "type": "numbered",
  "latex": "E = mc^2",
  "label": "eq:energy",
  "references": ["eq:energy"],
  "variables": [
    {"symbol": "E", "description": "能量"},
    {"symbol": "m", "description": "质量"},
    {"symbol": "c", "description": "光速"}
  ]
}
```

## 验证项

1. LaTeX 语法正确性
2. 公式编号连续性
3. 标签唯一性
4. 交叉引用完整性
5. 变量符号一致性
6. 数学符号正确性

## 常见问题

- 确保 amsmath 宏包已加载
- 检查 \text{} 中的文字是否需要翻译
- 检查矩阵环境是否正确闭合
- 检查多行公式的对齐符号 &
- 检查公式编号是否被正确引用
