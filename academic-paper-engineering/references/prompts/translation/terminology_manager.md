# 术语管理器（Terminology Manager）

## 概述

术语管理器是整个 Skill 翻译质量提升的关键组件。

核心职责：
1. 构建术语词典（从用户论文中提取）
2. 强制术语一致性（全文统一）
3. 禁止术语变体（一旦确定，禁止使用替代翻译）
4. 与翻译记忆集成

## 术语词典格式

```json
{
  "terminology_dictionary": {
    "快速充电站": {
      "english": "fast charging station",
      "alternatives_forbidden": [
        "quick charging station",
        "rapid charging station",
        "fast charge station"
      ],
      "domain": "electric_vehicle",
      "first_occurrence": "section_001",
      "confirmed": true
    },
    "充电需求": {
      "english": "charging demand",
      "alternatives_forbidden": [
        "charging requirement",
        "charging need",
        "charging request"
      ],
      "domain": "electric_vehicle",
      "first_occurrence": "section_001",
      "confirmed": true
    },
    "时空": {
      "english": "spatiotemporal",
      "alternatives_forbidden": [
        "spatial-temporal",
        "space-time",
        "spatiotemporal"
      ],
      "domain": "general",
      "first_occurrence": "section_002",
      "confirmed": true
    },
    "图神经网络": {
      "english": "graph neural network",
      "alternatives_forbidden": [
        "graph neural net",
        "GNN network"
      ],
      "domain": "deep_learning",
      "first_occurrence": "section_002",
      "confirmed": true
    },
    "预测": {
      "english": "forecasting",
      "alternatives_forbidden": [
        "prediction",
        "prognostication"
      ],
      "domain": "user_preference",
      "first_occurrence": "title",
      "confirmed": true,
      "note": "用户明确要求统一使用 forecasting 而非 prediction"
    }
  }
}
```

## 术语构建流程

### 第一步：扫描论文，提取候选术语

1. 扫描全文，识别反复出现的专业术语
2. 识别领域特有名词（如"充电利用率"、"动态网络"等）
3. 识别用户在引言/摘要中强调的核心概念
4. 识别已有的英文缩写对照（如"图神经网络(GNN)"）

### 第二步：确定标准翻译

为每个候选术语确定唯一的标准英文翻译：

1. 首先检查预置术语词典（`references/rules/terminology.md`）
2. 如果预置词典中没有，根据以下原则确定翻译：
   - 领域标准术语优先
   - 学术文献中广泛使用的翻译优先
   - 用户在原文中已给出的英文对照优先
3. 记录所有被排除的替代翻译

### 第三步：生成禁止列表

一旦确定标准翻译，生成禁止使用的替代翻译列表：

```
充电需求 -> charging demand（标准）
禁止使用：charging requirement, charging need, charging request
```

**全文执行：任何地方出现 charging requirement / charging need / charging request 都必须替换为 charging demand。**

### 第四步：用户确认

对于不确定的术语翻译，向用户确认：

```
以下术语需要确认翻译：
1. "充电利用率" -> "charging utilization" 或 "charging usage rate"？
2. "动态网络" -> "dynamic network" 或 "dynamic graph"？
```

用户确认后，记录到术语词典并标记 `confirmed: true`。

## 术语一致性执行

### 翻译阶段

翻译每一段落时：
1. 加载术语词典
2. 翻译过程中强制使用标准术语翻译
3. 翻译完成后，扫描译文，检查是否使用了禁止的替代翻译
4. 如果发现禁止的翻译，自动替换为标准翻译

### QA 阶段

翻译质量检查时：
1. 扫描全文，统计每个术语的出现次数
2. 检查是否有使用禁止替代翻译的情况
3. 生成术语一致性报告

```json
{
  "terminology_qa": {
    "total_terms": 15,
    "consistent": 14,
    "inconsistent": 1,
    "violations": [
      {
        "term": "充电需求",
        "expected": "charging demand",
        "found": "charging requirement",
        "location": "section_003, paragraph_002",
        "action": "已自动修正"
      }
    ],
    "consistency_rate": 0.933
  }
}
```

## 与翻译记忆集成

术语词典与翻译记忆协同工作：

1. **术语词典**：记录术语级别的对应关系（词/短语级）
2. **翻译记忆**：记录句子级别的对应关系（句子级）

两者关系：
- 术语词典是翻译记忆的基础
- 翻译记忆中的句子必须遵守术语词典
- 如果术语词典更新，受影响的翻译记忆条目标记为需更新

## 用户偏好支持

用户可以显式指定术语翻译偏好：

```
用户："本文统一将 prediction 翻译为 forecasting"
```

系统记录：
```json
{
  "prediction": {
    "english": "forecasting",
    "alternatives_forbidden": ["prediction", "prognostication"],
    "domain": "user_preference",
    "note": "用户明确要求"
  }
}
```

之后全文统一执行。

## 术语词典存储

术语词典保存在：
- 预置词典：`references/rules/terminology.md`
- 项目词典：输出工程的 `QA/terminology_dictionary.json`

项目词典可以在后续项目中导入复用。
