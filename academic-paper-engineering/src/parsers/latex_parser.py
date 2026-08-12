"""LaTeX 文档解析器 - 将已有 LaTeX 工程解析为 Document IR"""

import re
from pathlib import Path
from typing import Dict, List, Optional


class LatexParser:
    """解析 .tex 格式的学术文档"""

    def __init__(self):
        self.ir = {
            "document_id": "",
            "metadata": {"source_format": "tex", "source_language": ""},
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
            "footnotes": []
        }
        self._template_spec = {}

    def parse(self, file_path: str) -> Dict:
        """解析 LaTeX 文件，返回 Document IR"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        self.ir["document_id"] = path.stem
        text = path.read_text(encoding='utf-8')

        self._extract_document_class(text)
        self._extract_title(text)
        self._extract_authors(text)
        self._extract_abstract(text)
        self._extract_sections(text)
        self._extract_figures(text)
        self._extract_tables(text)
        self._extract_equations(text)
        self._extract_citations(text)
        self._extract_input_files(text, path.parent)

        return self.ir

    def get_template_spec(self) -> Dict:
        """返回模板规格说明"""
        return self._template_spec

    def _extract_document_class(self, text: str):
        """提取文档类和选项"""
        match = re.search(r'\\documentclass\s*(?:\[([^\]]*)\])?\s*\{([^}]+)\}', text)
        if match:
            options = match.group(1) or ""
            doc_class = match.group(2).strip()
            self._template_spec["document_class"] = doc_class
            self._template_spec["class_options"] = [o.strip() for o in options.split(',') if o.strip()]

        # 提取宏包
        packages = re.findall(r'\\usepackage\s*(?:\[([^\]]*)\])?\s*\{([^}]+)\}', text)
        self._template_spec["required_packages"] = [p[1].strip() for p in packages]

        # 提取引用样式
        match = re.search(r'\\bibliographystyle\s*\{([^}]+)\}', text)
        if match:
            self._template_spec["bibliography_bst"] = match.group(1).strip()

    def _extract_title(self, text: str):
        """提取标题"""
        match = re.search(r'\\title\s*\{([^}]+)\}', text)
        if match:
            self.ir["title"] = {
                "id": "title_001",
                "text": match.group(1).strip()
            }

    def _extract_authors(self, text: str):
        """提取作者"""
        match = re.search(r'\\author\s*\{([^}]+)\}', text, re.DOTALL)
        if match:
            author_text = match.group(1).strip()
            # 简单分割作者
            authors = re.split(r'\\and|,', author_text)
            for i, author in enumerate(authors):
                author = author.strip()
                if author:
                    self.ir["authors"].append({
                        "id": f"author_{i+1:03d}",
                        "name": author,
                        "affiliation_id": ""
                    })

    def _extract_abstract(self, text: str):
        """提取摘要"""
        match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', text, re.DOTALL)
        if match:
            self.ir["abstract"] = {
                "id": "abstract_001",
                "text": match.group(1).strip()
            }

    def _extract_sections(self, text: str):
        """提取章节结构"""
        patterns = [
            (r'\\section\s*\{([^}]+)\}', 1),
            (r'\\subsection\s*\{([^}]+)\}', 2),
            (r'\\subsubsection\s*\{([^}]+)\}', 3),
            (r'\\paragraph\s*\{([^}]+)\}', 4),
        ]

        all_sections = []
        for pattern, level in patterns:
            for match in re.finditer(pattern, text):
                all_sections.append((match.start(), level, match.group(1).strip()))

        all_sections.sort(key=lambda x: x[0])

        for i, (pos, level, title) in enumerate(all_sections):
            self.ir["sections"].append({
                "id": f"section_{i+1:03d}",
                "number": str(i + 1),
                "title": title,
                "level": level,
                "paragraphs": [],
                "subsections": []
            })

    def _extract_figures(self, text: str):
        """提取图片"""
        pattern = r'\\begin\{figure\}.*?\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}.*?\\caption\s*\{([^}]+)\}.*?\\label\s*\{([^}]+)\}.*?\\end\{figure\}'
        for i, match in enumerate(re.finditer(pattern, text, re.DOTALL)):
            self.ir["figures"].append({
                "id": f"figure_{i+1:03d}",
                "number": i + 1,
                "caption": match.group(2).strip(),
                "label": match.group(3).strip(),
                "file_path": match.group(1).strip()
            })

    def _extract_tables(self, text: str):
        """提取表格"""
        pattern = r'\\begin\{table\}.*?(?:\\caption\s*\{([^}]+)\})?.*?\\begin\{(?:tabular|tabularx)\*?\}(?:\{[^}]*\})?\{([^}]+)\}(.*?)\\end\{(?:tabular|tabularx)\*?\}.*?\\end\{table\}'
        for i, match in enumerate(re.finditer(pattern, text, re.DOTALL)):
            caption = match.group(1) or ""
            col_spec = match.group(2)
            body = match.group(3)
            rows = []
            for row_idx, line in enumerate(body.split('\\\\')):
                cells = [c.strip() for c in line.split('&') if c.strip()]
                if cells:
                    rows.append({
                        "row": row_idx,
                        "cells": [{"text": c} for c in cells]
                    })

            self.ir["tables"].append({
                "id": f"table_{i+1:03d}",
                "number": i + 1,
                "caption": caption.strip(),
                "label": "",
                "headers": [rows[0]] if rows else [],
                "rows": rows[1:] if len(rows) > 1 else []
            })

    def _extract_equations(self, text: str):
        """提取公式"""
        pattern = r'\\begin\{equation\}(.*?)\\label\s*\{([^}]+)\}?(.*?)\\end\{equation\}'
        for i, match in enumerate(re.finditer(pattern, text, re.DOTALL)):
            latex = (match.group(1) + match.group(3)).strip()
            label = match.group(2).strip() if match.group(2) else ""
            self.ir["equations"].append({
                "id": f"equation_{i+1:03d}",
                "number": i + 1,
                "type": "numbered",
                "latex": latex,
                "label": label
            })

    def _extract_citations(self, text: str):
        """提取引用"""
        pattern = r'\\cite[a-z]*\s*\{([^}]+)\}'
        for i, match in enumerate(re.finditer(pattern, text)):
            keys = [k.strip() for k in match.group(1).split(',')]
            for key in keys:
                self.ir["citations"].append({
                    "id": f"citation_{i+1:03d}",
                    "key": key,
                    "text": ""
                })

    def _extract_input_files(self, text: str, base_dir: Path):
        """提取 \\input 和 \\include 引用的文件"""
        pattern = r'\\(?:input|include)\s*\{([^}]+)\}'
        for match in re.finditer(pattern, text):
            file_name = match.group(1).strip()
            if not file_name.endswith('.tex'):
                file_name += '.tex'
            file_path = base_dir / file_name
            if file_path.exists():
                sub_text = file_path.read_text(encoding='utf-8')
                self._extract_sections(sub_text)
                self._extract_figures(sub_text)
                self._extract_tables(sub_text)
                self._extract_equations(sub_text)
                self._extract_citations(sub_text)
