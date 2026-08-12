"""PDF 文档解析器 - 将 PDF 文档解析为 Document IR"""

import re
from pathlib import Path
from typing import Dict, List, Optional


class PdfParser:
    """解析 .pdf 格式的学术文档"""

    def __init__(self):
        self.ir = {
            "document_id": "",
            "metadata": {"source_format": "pdf", "source_language": ""},
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
        self._text = ""

    def parse(self, file_path: str) -> Dict:
        """解析 PDF 文件，返回 Document IR"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        self.ir["document_id"] = path.stem
        self._extract_text(path)
        self._extract_metadata(path)
        self._extract_title()
        self._extract_abstract()
        self._extract_sections()
        self._extract_references()

        return self.ir

    def _extract_text(self, path: Path):
        """提取 PDF 全文"""
        try:
            import fitz  # PyMuPDF
            doc = fitz.open(str(path))
            self.ir["metadata"]["page_count"] = len(doc)
            self._text = ""
            for page in doc:
                self._text += page.get_text()
            doc.close()
        except ImportError:
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(str(path))
                self.ir["metadata"]["page_count"] = len(reader.pages)
                self._text = ""
                for page in reader.pages:
                    self._text += page.extract_text() or ""
            except ImportError:
                raise ImportError("需要安装 PyMuPDF 或 PyPDF2: pip install pymupdf 或 pip install PyPDF2")

    def _extract_metadata(self, path: Path):
        """提取 PDF 元数据"""
        try:
            import fitz
            doc = fitz.open(str(path))
            meta = doc.metadata
            if meta.get("title"):
                self.ir["title"]["text"] = meta["title"]
            if meta.get("author"):
                self.ir["authors"].append({
                    "id": "author_001",
                    "name": meta["author"],
                    "affiliation_id": ""
                })
            doc.close()
        except Exception:
            pass

    def _extract_title(self):
        """从文本提取标题（通常是第一行非空文本）"""
        if "text" in self.ir["title"]:
            return
        lines = [l.strip() for l in self._text.split('\n') if l.strip()]
        if lines:
            self.ir["title"] = {
                "id": "title_001",
                "text": lines[0]
            }

    def _extract_abstract(self):
        """提取摘要"""
        patterns = [
            r'Abstract[:\s]*(.*?)(?:\n\n|\nKeywords|\n1\.\s)',
            r'摘要[:\s]*(.*?)(?:\n\n|\n关键词|\n1\.\s)'
        ]
        for pattern in patterns:
            match = re.search(pattern, self._text, re.DOTALL | re.IGNORECASE)
            if match:
                self.ir["abstract"] = {
                    "id": "abstract_001",
                    "text": match.group(1).strip()
                }
                return

    def _extract_sections(self):
        """提取章节结构"""
        patterns = [
            r'^(\d+)\.\s+(.+)$',
            r'^(\d+\.\d+)\s+(.+)$'
        ]
        lines = self._text.split('\n')
        current_section = None
        section_counter = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            matched = False
            for pattern in patterns:
                match = re.match(pattern, line)
                if match:
                    number = match.group(1)
                    title = match.group(2).strip()
                    level = number.count('.') + 1

                    section_counter += 1
                    current_section = {
                        "id": f"section_{section_counter:03d}",
                        "number": number,
                        "title": title,
                        "level": level,
                        "paragraphs": [],
                        "subsections": []
                    }
                    self.ir["sections"].append(current_section)
                    matched = True
                    break
            if not matched and current_section and len(line) > 20:
                current_section["paragraphs"].append(line)

    def _extract_references(self):
        """提取参考文献"""
        ref_patterns = [
            r'References\s*\n(.*)',
            r'参考文献\s*\n(.*)'
        ]
        for pattern in ref_patterns:
            match = re.search(pattern, self._text, re.DOTALL)
            if match:
                ref_text = match.group(1).strip()
                ref_lines = [l.strip() for l in ref_text.split('\n') if l.strip()]
                for i, line in enumerate(ref_lines):
                    if len(line) > 10:
                        self.ir["references"].append({
                            "id": f"reference_{i+1:03d}",
                            "key": "",
                            "raw_text": line
                        })
                return
