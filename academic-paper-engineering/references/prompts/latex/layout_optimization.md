# 自动版面优化

## 概述

在 LaTeX 渲染完成后，自动检测和优化版面问题，提升排版质量。

## 检测项

### 1. Overfull/Underfull Hbox

检测行溢出和行间距问题：

- Overfull hbox：行内容超出页面宽度
- Underfull hbox：行间距过大
- 检测方法：分析 .log 文件中的警告

### 2. 浮动体位置

检测图片和表格的位置问题：

- 浮动体离引用位置过远
- 浮动体堆积在章节末尾
- 浮动体跨页

### 3. 页面利用率

检测页面空间利用问题：

- 页面空白过多
- 段落末尾孤行/寡行
- 章节标题与内容分离

### 4. 公式排版

检测公式排版问题：

- 公式过长溢出
- 公式编号位置异常
- 行间公式间距不一致

### 5. 表格排版

检测表格排版问题：

- 表格宽度超出页面
- 表格列宽不合理
- 表格内容换行过多

## 优化策略

### Overfull Hbox 修复

```latex
% 方案1：微调断词
\hyphenation{speci-fic ex-am-ple}

% 方案2：调整间距
\sloppy

% 方案3：手动断行
\linebreak

% 方案4：缩小内容
\resizebox{\columnwidth}{!}{...}
```

### 浮动体位置优化

```latex
% 方案1：调整位置选项
\begin{figure}[htbp] -> \begin{figure}[!ht]

% 方案2：使用 float 宏包的 H 选项
\usepackage{float}
\begin{figure}[H]

% 方案3：使用 \FloatBarrier
\usepackage{placeins}
\FloatBarrier
```

### 页面利用率优化

```latex
% 方案1：调整段落间距
\setlength{\parskip}{...}

% 方案2：调整行距
\linespread{1.1}

% 方案3：使用 microtype 微调
\usepackage{microtype}
```

### 表格宽度优化

```latex
% 方案1：使用 tabularx 自适应宽度
\usepackage{tabularx}
\begin{tabularx}{\textwidth}{Xcc}

% 方案2：使用 resizebox
\resizebox{\textwidth}{!}{\begin{tabular}...\end{tabular}}

% 方案3：使用 adjustbox
\usepackage{adjustbox}
\begin{adjustbox}{max width=\textwidth}
```

## 优化流程

1. 编译 LaTeX 工程
2. 解析 .log 文件
3. 识别版面问题
4. 匹配优化策略
5. 应用优化
6. 重新编译
7. 验证改善效果
8. 生成优化报告

## 优化报告

```json
{
  "layout_optimization": {
    "issues_found": 5,
    "issues_fixed": 4,
    "issues_remaining": 1,
    "details": [
      {
        "type": "overfull_hbox",
        "location": "line 45",
        "severity": "minor",
        "action": "applied \\sloppy",
        "status": "fixed"
      },
      {
        "type": "float_position",
        "location": "figure_003",
        "severity": "moderate",
        "action": "changed [htbp] to [!ht]",
        "status": "fixed"
      }
    ]
  }
}
```

## 注意事项

- 优化不得改变文档内容
- 优化不得改变科学语义
- 每次优化后必须重新编译验证
- 无法自动修复的问题需报告给用户
- 优化策略需考虑模板约束
