# 用户学术风格记忆

## 概述

记录用户的学术写作风格偏好，在后续项目中保持一致的写作风格。

## 风格维度

### 1. 语气与人称

| 维度 | 选项 | 说明 |
|---|---|---|
| 人称 | 第一人称 / 被动语态 | "We propose..." vs "A method is proposed..." |
| 语气强度 | 谨慎 / 中性 / 强烈 | "may indicate" vs "shows" vs "proves" |

### 2. 时态偏好

| 章节 | 推荐时态 | 用户偏好 |
|---|---|---|
| 背景 | 现在时 | 可配置 |
| 方法 | 过去时 | 可配置 |
| 结果 | 过去时 | 可配置 |
| 讨论 | 现在时/过去时 | 可配置 |

### 3. 句式偏好

| 维度 | 选项 |
|---|---|
| 句子长度 | 短句为主 / 中等 / 长句为主 |
| 从句使用 | 少 / 适中 / 多 |
| 列举偏好 | 行内列举 / 独立列表 |
| 连接词频率 | 低 / 中 / 高 |

### 4. 术语偏好

| 维度 | 选项 |
|---|---|
| 缩写使用 | 首次全称+缩写 / 直接使用缩写 / 避免缩写 |
| 拉丁语 | 使用 et al. / i.e. / e.g. 等 / 避免使用 |
| 数字表达 | 数字 / 文字（ten vs 10） |

### 5. 引用风格偏好

| 维度 | 选项 |
|---|---|
| 引用频率 | 每句引用 / 每段引用 / 关键处引用 |
| 引用位置 | 句末 / 句中 / 句首 |
| 多引用格式 | [1,2,3] / [1-3] |

## 记忆文件格式

```json
{
  "style_profile": {
    "user_id": "user_001",
    "voice_preference": "passive",
    "tense": {
      "background": "present",
      "methodology": "past",
      "results": "past",
      "discussion": "present"
    },
    "sentence_style": {
      "length": "medium",
      "clause_usage": "moderate",
      "list_preference": "inline"
    },
    "terminology": {
      "abbreviation_policy": "first_full_then_abbr",
      "latin_terms": true,
      "number_style": "numeric"
    },
    "citation": {
      "frequency": "per_paragraph",
      "position": "end_of_sentence",
      "multi_citation": "range"
    },
    "samples": [
      {
        "section": "introduction",
        "original": "...",
        "preferred": "..."
      }
    ]
  }
}
```

## 使用流程

1. 分析用户提供的样本文档
2. 提取风格特征
3. 生成风格配置文件
4. 存储在 `QA/style_profile.json`
5. 后续项目中加载并应用

## 风格一致性检查

翻译完成后，检查输出是否与用户风格偏好一致：

- 时态使用是否符合偏好
- 语气是否一致
- 句式是否符合偏好
- 术语使用是否一致

不一致项标记为风格警告。
