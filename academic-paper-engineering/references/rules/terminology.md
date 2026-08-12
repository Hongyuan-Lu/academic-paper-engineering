# 术语规则

## 术语翻译原则

1. 技术术语首次出现时提供中英文对照
2. 全文保持术语翻译一致
3. 广泛接受的术语使用标准翻译
4. 新兴术语保留英文原文
5. **一旦确定术语翻译，全文禁止使用替代翻译**

## 禁止规则（核心）

术语管理器确定标准翻译后，生成禁止列表。

例如：
- "充电需求" -> "charging demand"（标准）
- 禁止使用：charging requirement, charging need, charging request

**全文任何位置出现禁止的替代翻译，必须替换为标准翻译。**

除非存在明确的语义区别（需在 QA 报告中说明）。

## 术语词典格式

术语词典使用 JSON 格式存储：

```json
{
  "terminology_dictionary": {
    "中文术语": {
      "english": "标准英文翻译",
      "alternatives_forbidden": ["禁止翻译1", "禁止翻译2"],
      "domain": "领域",
      "confirmed": true
    }
  }
}
```

项目词典保存在 `QA/terminology_dictionary.json`。

## 用户自定义术语

用户可以显式指定术语翻译：

```
用户："本文统一将 prediction 翻译为 forecasting"
```

系统记录并全文执行。

## 预置术语对照表

### 人工智能领域

| 中文 | 英文 | 禁止替代 |
|---|---|---|
| 深度学习 | deep learning | deep studying |
| 神经网络 | neural network | nerve network |
| 卷积神经网络 | convolutional neural network (CNN) | convoluted neural network |
| 循环神经网络 | recurrent neural network (RNN) | recursive neural network（注意区分） |
| 注意力机制 | attention mechanism | attention method |
| Transformer | Transformer | 变压器（禁止翻译） |
| 预训练模型 | pre-trained model | pre-training model |
| 微调 | fine-tuning | fine-adjustment |
| 迁移学习 | transfer learning | transition learning |
| 强化学习 | reinforcement learning | enhancement learning |
| 生成对抗网络 | generative adversarial network (GAN) | generation adversarial network |
| 自然语言处理 | natural language processing (NLP) | natural language processing |
| 计算机视觉 | computer vision (CV) | computer visual |
| 目标检测 | object detection | target detection |
| 图像分割 | image segmentation | image division |
| 语义分割 | semantic segmentation | meaning segmentation |
| 实例分割 | instance segmentation | example segmentation |
| 损失函数 | loss function | lost function |
| 梯度下降 | gradient descent | gradient decline |
| 反向传播 | backpropagation | backward propagation |
| 学习率 | learning rate | learning speed |
| 过拟合 | overfitting | over-fitting（连字符变体允许） |
| 欠拟合 | underfitting | under-fitting（连字符变体允许） |
| 正则化 | regularization | regularisation（英式拼写允许） |
| 交叉验证 | cross-validation | cross validation |
| 特征提取 | feature extraction | feature mining |
| 池化 | pooling | gathering |
| 感受野 | receptive field | perception field |

### 通用学术术语

| 中文 | 英文 | 禁止替代 |
|---|---|---|
| 方法论 | methodology | method theory |
| 实验设置 | experimental setup | experiment setting |
| 数据集 | dataset | data set（允许） |
| 评价指标 | evaluation metrics | evaluation index |
| 基线 | baseline | base line |
| 消融实验 | ablation study | ablation experiment |
| 对比实验 | comparative experiment | comparison experiment |
| 定量分析 | quantitative analysis | quantity analysis |
| 定性分析 | qualitative analysis | quality analysis |
| 鲁棒性 | robustness | robustness |
| 泛化能力 | generalization ability | generalization capability |
| 收敛 | convergence | convergency |
| 精度 | accuracy | preciseness（注意与 precision 区分） |
| 精确率 | precision | accuracy（注意区分） |
| 召回率 | recall | retrieval rate |

### 电动车辆领域（示例）

| 中文 | 英文 | 禁止替代 |
|---|---|---|
| 快速充电站 | fast charging station | quick charging station |
| 充电需求 | charging demand | charging requirement, charging need |
| 充电利用率 | charging utilization | charging usage rate |
| 时空 | spatiotemporal | spatial-temporal |
| 动态网络 | dynamic network | dynamic graph（注意区分） |
| 预测 | forecasting | prediction（用户偏好） |

## 术语管理器

详细的术语管理流程见 `references/prompts/translation/terminology_manager.md`。
