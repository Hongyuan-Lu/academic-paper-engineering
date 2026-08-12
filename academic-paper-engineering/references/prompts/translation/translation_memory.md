# 翻译记忆

## 概述

翻译记忆（Translation Memory）用于在多次翻译中保持一致性和提高效率。

## 功能

### 1. 句对记忆

存储已翻译的句对（中文-英文），在后续翻译中复用：

```json
{
  "translation_memory": [
    {
      "source": "本文提出了一种新的深度学习方法",
      "target": "In this paper, we propose a novel deep learning method",
      "source_hash": "sha256...",
      "context": "introduction",
      "created_at": "2026-01-01T00:00:00Z",
      "usage_count": 3
    }
  ]
}
```

### 2. 术语记忆

存储已确认的术语翻译：

```json
{
  "terminology_memory": [
    {
      "source": "卷积神经网络",
      "target": "convolutional neural network",
      "abbreviation": "CNN",
      "domain": "deep_learning",
      "confirmed": true
    }
  ]
}
```

### 3. 风格记忆

存储用户的学术写作风格偏好：

```json
{
  "style_memory": {
    "voice_preference": "passive",
    "tense_for_methodology": "past",
    "tense_for_background": "present",
    "citation_style": "author-year",
    "first_person": false,
    "sentence_length": "medium"
  }
}
```

## 使用流程

1. 翻译前查询翻译记忆
2. 精确匹配：直接复用
3. 模糊匹配（相似度 >= 0.85）：提供参考
4. 无匹配：执行新翻译
5. 翻译完成后存入记忆

## 记忆管理

- 记忆文件存储在输出工程的 `QA/translation_memory.json`
- 可在后续项目中导入复用
- 支持记忆合并和冲突解决
- 过时条目自动标记
