# 文档结构分析器

分析所提供的学术文档。

识别以下结构元素：

- 标题（title）
- 作者（authors）
- 所属机构（affiliations）
- 摘要（abstract）
- 关键词（keywords）
- 章节（sections）
- 小节（subsections）
- 段落（paragraphs）
- 列表（lists）
- 公式（equations）
- 图片（figures）
- 图片标题说明（figure captions）
- 表格（tables）
- 表格标题说明（table captions）
- 引用（citations）
- 参考文献（references）
- 脚注（footnotes）
- 附录（appendices）
- 致谢（acknowledgements）

## 对象 ID 分配

为每个对象分配稳定的 ID。

示例：

```
section_001
paragraph_001
figure_001
table_001
equation_001
citation_001
reference_001
```

## 输出格式

输出结构化元数据，不修改原始内容。

```json
{
  "document_id": "paper_001",
  "metadata": {
    "source_format": "...",
    "source_language": "...",
    "page_count": 0
  },
  "title": {
    "id": "title_001",
    "text": "..."
  },
  "authors": [
    {
      "id": "author_001",
      "name": "...",
      "affiliation_id": "affiliation_001"
    }
  ],
  "affiliations": [
    {
      "id": "affiliation_001",
      "text": "..."
    }
  ],
  "abstract": {
    "id": "abstract_001",
    "text": "..."
  },
  "keywords": {
    "id": "keywords_001",
    "items": []
  },
  "sections": [
    {
      "id": "section_001",
      "number": "1",
      "title": "...",
      "level": 1,
      "paragraphs": [],
      "subsections": []
    }
  ],
  "figures": [
    {
      "id": "figure_001",
      "number": 1,
      "caption": "...",
      "label": "..."
    }
  ],
  "tables": [
    {
      "id": "table_001",
      "number": 1,
      "caption": "...",
      "label": "..."
    }
  ],
  "equations": [
    {
      "id": "equation_001",
      "number": 1,
      "latex": "...",
      "label": "..."
    }
  ],
  "citations": [
    {
      "id": "citation_001",
      "key": "...",
      "text": "..."
    }
  ],
  "references": [
    {
      "id": "reference_001",
      "key": "...",
      "raw_text": "..."
    }
  ]
}
```

## 注意事项

- 不修改原始内容
- 输出仅为结构化元数据
- 保持文档原始顺序
- 正确识别章节层级
- 标记不确定的结构元素
