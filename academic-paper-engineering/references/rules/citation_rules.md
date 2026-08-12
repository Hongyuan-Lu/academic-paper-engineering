# 引用规则

## 引用格式

### 数字引用格式

- 格式：[1], [2], [3]
- LaTeX 命令：\cite{key}
- 适用模板：IEEE, Elsevier (num), Springer (basic)

### 作者-年引用格式

- 格式：Smith et al. (2020) 或 (Smith et al., 2020)
- LaTeX 命令：\citep{key}, \citet{key}
- 适用模板：Elsevier (harv), Springer (aps)

### 引用类型

| 引用类型 | 说明 | LaTeX 命令 |
|---|---|---|
| 括号引用 | (Smith, 2020) | \citep{key} |
| 文中引用 | Smith (2020) | \citet{key} |
| 多引用 | (Smith, 2020; Jones, 2021) | \citep{key1, key2} |
| 页码引用 | (Smith, 2020, p. 15) | \citep[p. 15]{key} |

## 引用键规则

- 格式：作者姓 + 年份 + 关键词
- 全小写
- 无空格和特殊字符
- 示例：smith2020deep, jones2021transformer

## 多作者引用

- 两位作者：Smith and Jones (2020)
- 三位及以上作者：Smith et al. (2020)
- et al. 不斜体（视模板要求）

## 引用完整性

- 每个引用必须有对应参考文献
- 未解析引用必须报告
- 禁止编造参考文献

## 各模板引用格式

### IEEE
- 数字引用 [1]
- BST: IEEEtran.bst
- 命令: \cite{key}

### Elsevier (elsarticle)
- 数字: \cite{key}
- 作者-年: \citep{key}, \citet{key}
- BST: elsarticle-num.bst / elsarticle-harv.bst

### Springer (sn-jnl)
- 多种 BST 可选
- \cite{key} 或 \citep{key}

### MDPI
- 数字引用
- BST: mdpi.bst

### Frontiers
- Harvard 或 Vancouver 格式
- BST: Frontiers-Harvard.bst / Frontiers-Vancouver.bst
