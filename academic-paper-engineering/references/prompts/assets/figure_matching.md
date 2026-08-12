# 图片匹配代理

将外部图片资产与文档中描述的图片进行匹配。

图片匹配独立为 Figure Asset Manager，不由翻译模型决定图片放置。

## 三级匹配策略

### Level 1：文件名匹配

直接通过文件名中的图号匹配。

识别文件名中的图号模式：

```
Fig1.png / Figure_1.png / fig_01.png / 图1.png
```

直接匹配到文档中的：

```
Figure 1 / 图1
```

置信度：>= 0.90

### Level 2：语义匹配

当文件名包含描述性文字时，分析文件名 + caption + 周围正文。

例如文件名：

```
station_clustering_result.png
```

分析步骤：
1. 提取文件名关键词：station, clustering, result
2. 匹配文档中所有图片的 caption
3. 匹配引用图片的周围段落文本
4. 计算语义相似度

例如匹配到：

```
Figure 3: Clustering results of charging stations
```

置信度：0.60 - 0.90

### Level 3：视觉匹配

当文件名无意义（如 image_001.png）时，使用多模态模型进行视觉理解。

流程：

```
Image Understanding（多模态模型识别图片内容）
        ↓
Visual Description（生成图片描述）
        ↓
Semantic Embedding（计算语义嵌入）
        ↓
Paragraph / Figure Reference Matching（与论文文本匹配）
```

例如图片识别结果：

```
Six charging station clusters with distinct daily utilization patterns
```

然后与论文文本匹配：

```
Figure 3 illustrates six representative utilization patterns...
```

置信度：0.60 - 0.95

## 匹配结果

为每个匹配返回：

```json
{
  "figure": "image_003.png",
  "matched_to": "Figure 4",
  "confidence": 0.93,
  "reason": "filename + caption + semantic similarity",
  "level": 2
}
```

## 置信度阈值

| 置信度范围 | 操作 |
|---|---|
| >= 0.85 | 自动插入 |
| 0.60 - 0.85 | 插入但发出 QA warning |
| < 0.60 | 不自动插入 |

阈值配置见 `references/config/thresholds.yaml`。

## 未匹配图片处理

绝对不能随便插入未匹配的图片。

应生成警告报告：

```
⚠ Unmatched image assets

The following images could not be reliably matched:
- image_07.png
- image_08.png

Please rename them according to:
Fig1.png
Fig2.png
...
```

这样比"猜一个位置"更加专业。

## 位置锚点

匹配成功后，记录图片在原文中的位置锚点（Position Anchor）：

```json
{
  "type": "figure",
  "id": "fig_03",
  "after_paragraph": "para_127"
}
```

渲染时根据锚点位置插入，而非简单按 Figure 1, 2, 3 顺序排列。

## 注意事项

- 禁止编造图片关系
- 未匹配的资产必须报告并建议重命名
- 多个资产匹配同一目标时，选择置信度最高的
- 一个资产匹配多个目标时，全部报告
- 图片匹配不由翻译模型决定，由独立的 Figure Asset Manager 处理
