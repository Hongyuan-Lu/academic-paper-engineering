"""Document IR 管理器 - 构建、验证、操作文档中间表示"""

import json
from typing import Dict, List, Optional, Any
from pathlib import Path


class DocumentIRManager:
    """管理学术文档中间表示（Document IR）"""

    def __init__(self):
        self.ir = {
            "document_id": "",
            "metadata": {
                "source_format": "",
                "source_language": "",
                "target_language": ""
            },
            "title": {},
            "authors": [],
            "affiliations": [],
            "abstract": {},
            "keywords": {},
            "sections": [],
            "figures": [],
            "tables": [],
            "equations": [],
            "citations": [],
            "references": [],
            "footnotes": [],
            "assets": []
        }

    def create_ir(self, document_id: str = "paper_001") -> Dict:
        """创建空的 Document IR"""
        self.ir["document_id"] = document_id
        return self.ir

    def load_ir(self, ir_data: Dict) -> Dict:
        """从字典加载 IR"""
        self.ir = ir_data
        return self.ir

    def load_from_file(self, file_path: str) -> Dict:
        """从 JSON 文件加载 IR"""
        path = Path(file_path)
        with open(path, 'r', encoding='utf-8') as f:
            self.ir = json.load(f)
        return self.ir

    def save_to_file(self, file_path: str):
        """保存 IR 到 JSON 文件"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.ir, f, ensure_ascii=False, indent=2)

    def set_metadata(self, source_format: str, source_language: str,
                     target_language: str = ""):
        """设置元数据"""
        self.ir["metadata"]["source_format"] = source_format
        self.ir["metadata"]["source_language"] = source_language
        self.ir["metadata"]["target_language"] = target_language

    def set_title(self, text: str):
        """设置标题"""
        self.ir["title"] = {"id": "title_001", "text": text}

    def add_author(self, name: str, affiliation: str = "", email: str = ""):
        """添加作者"""
        author_id = f"author_{len(self.ir['authors']) + 1:03d}"
        aff_id = ""
        if affiliation:
            aff_id = f"affiliation_{len(self.ir['affiliations']) + 1:03d}"
            self.ir["affiliations"].append({
                "id": aff_id,
                "text": affiliation
            })
        self.ir["authors"].append({
            "id": author_id,
            "name": name,
            "affiliation_id": aff_id,
            "email": email
        })

    def set_abstract(self, text: str):
        """设置摘要"""
        self.ir["abstract"] = {"id": "abstract_001", "text": text}

    def set_keywords(self, keywords: List[str]):
        """设置关键词"""
        self.ir["keywords"] = {"id": "keywords_001", "items": keywords}

    def add_section(self, title: str, level: int = 1, number: str = "") -> str:
        """添加章节，返回章节ID"""
        section_id = f"section_{len(self.ir['sections']) + 1:03d}"
        section = {
            "id": section_id,
            "number": number or str(len(self.ir['sections']) + 1),
            "title": title,
            "level": level,
            "paragraphs": [],
            "subsections": []
        }
        self.ir["sections"].append(section)
        return section_id

    def add_paragraph(self, section_id: str, text: str):
        """向章节添加段落"""
        for section in self.ir["sections"]:
            if section["id"] == section_id:
                section["paragraphs"].append(text)
                return
        raise ValueError(f"章节不存在: {section_id}")

    def add_figure(self, number: int, caption: str, file_path: str = "",
                   label: str = "") -> str:
        """添加图片"""
        fig_id = f"figure_{len(self.ir['figures']) + 1:03d}"
        self.ir["figures"].append({
            "id": fig_id,
            "number": number,
            "caption": caption,
            "label": label or f"fig:{fig_id}",
            "file_path": file_path
        })
        return fig_id

    def add_table(self, number: int, caption: str, headers: List,
                  rows: List, label: str = "") -> str:
        """添加表格"""
        tab_id = f"table_{len(self.ir['tables']) + 1:03d}"
        self.ir["tables"].append({
            "id": tab_id,
            "number": number,
            "caption": caption,
            "label": label or f"tab:{tab_id}",
            "headers": headers,
            "rows": rows
        })
        return tab_id

    def add_equation(self, number: int, latex: str, label: str = "",
                     eq_type: str = "numbered") -> str:
        """添加公式"""
        eq_id = f"equation_{len(self.ir['equations']) + 1:03d}"
        self.ir["equations"].append({
            "id": eq_id,
            "number": number,
            "type": eq_type,
            "latex": latex,
            "label": label or f"eq:{eq_id}"
        })
        return eq_id

    def add_citation(self, key: str, text: str = "", location: str = "") -> str:
        """添加引用"""
        cite_id = f"citation_{len(self.ir['citations']) + 1:03d}"
        self.ir["citations"].append({
            "id": cite_id,
            "key": key,
            "text": text,
            "location": location
        })
        return cite_id

    def add_reference(self, key: str, ref_type: str, fields: Dict,
                      raw_text: str = "") -> str:
        """添加参考文献"""
        ref_id = f"reference_{len(self.ir['references']) + 1:03d}"
        self.ir["references"].append({
            "id": ref_id,
            "key": key,
            "type": ref_type,
            "fields": fields,
            "raw_text": raw_text,
            "status": "resolved"
        })
        return ref_id

    def validate(self) -> Dict:
        """验证 IR 完整性"""
        issues = []

        if not self.ir.get("title"):
            issues.append("缺少标题")
        if not self.ir.get("abstract"):
            issues.append("缺少摘要")
        if not self.ir.get("sections"):
            issues.append("缺少章节")

        # 检查引用是否有对应参考文献
        ref_keys = {r["key"] for r in self.ir["references"] if r.get("key")}
        for cite in self.ir["citations"]:
            if cite["key"] and cite["key"] not in ref_keys:
                issues.append(f"引用 {cite['key']} 无对应参考文献")

        # 检查标签唯一性
        labels = []
        for fig in self.ir["figures"]:
            if "label" in fig:
                labels.append(("figure", fig["id"], fig["label"]))
        for tab in self.ir["tables"]:
            if "label" in tab:
                labels.append(("table", tab["id"], tab["label"]))
        for eq in self.ir["equations"]:
            if "label" in eq:
                labels.append(("equation", eq["id"], eq["label"]))

        seen = {}
        for obj_type, obj_id, label in labels:
            if label in seen:
                issues.append(f"标签重复: {label} ({obj_id} 和 {seen[label]})")
            else:
                seen[label] = obj_id

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }

    def get_summary(self) -> Dict:
        """获取 IR 统计摘要"""
        return {
            "sections": len(self.ir["sections"]),
            "figures": len(self.ir["figures"]),
            "tables": len(self.ir["tables"]),
            "equations": len(self.ir["equations"]),
            "citations": len(self.ir["citations"]),
            "references": len(self.ir["references"])
        }
