"""Markdown 文档解析器 - 将 Markdown 文档解析为 Document IR"""

import re
from pathlib import Path
from typing import Dict, List


class MarkdownParser:
    """解析 .md 格式的学术文档"""

    def __init__(self):
        self.ir = {
            "document_id": "",
            "metadata": {"source_format": "md", "source_language": ""},
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

    def parse(self, file_path: str) -> Dict:
        """解析 Markdown 文件，返回 Document IR"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        self.ir["document_id"] = path.stem
        text = path.read_text(encoding='utf-8')

        # 先提取公式和表格，避免被段落处理干扰
        self._extract_equations(text)
        self._extract_tables(text)
        self._extract_figures(text)
        
        self._extract_title(text)
        self._extract_sections(text)

        return self.ir

    def _extract_title(self, text: str):
        """提取标题（# 开头的第一行）"""
        # 更鲁棒的标题匹配，允许 # 前后有空格，并处理不规范间距，允许 # 后无空格
        match = re.search(r'^\s*#\s*(.+)$', text, re.MULTILINE)
        if match:
            self.ir["title"] = {
                "id": "title_001",
                "text": match.group(1).strip()
            }

    def _extract_sections(self, text: str):
        """提取章节结构"""
        lines = text.split('\n')
        current_section = None
        section_counter = 0
        para_buffer = []

        for line in lines:
            # 更加鲁棒的标题匹配：
            # 1. 允许 # 后无空格 (##2. Methodology)
            # 2. 允许标题和文字粘连 (### 2.2Training)
            # 3. 允许不规范的空格
            match = re.match(r'^\s*(#{2,6})\s*(\d+\.?\d*)?\s*(.+)$', line)
            if match:
                # 保存之前的段落
                if current_section and para_buffer:
                    current_section["paragraphs"].append('\n'.join(para_buffer))
                    para_buffer = []

                level = len(match.group(1))
                title = match.group(3).strip()
                
                # 如果标题包含 "References"，专门处理
                if "References" in title:
                    self._extract_references_from_text(lines[lines.index(line):])
                    break

                section_counter += 1
                new_section = {
                    "id": f"section_{section_counter:03d}",
                    "number": match.group(2).rstrip('.') if match.group(2) else str(section_counter),
                    "title": title,
                    "level": level - 1,
                    "paragraphs": [],
                    "subsections": []
                }
                
                # 处理层级结构
                if level - 1 == 1:
                    self.ir["sections"].append(new_section)
                    current_section = new_section
                else:
                    # 寻找父章节
                    parent = None
                    for s in reversed(self.ir["sections"]):
                        if s["level"] < level - 1:
                            parent = s
                            break
                    if parent:
                        parent["subsections"].append(new_section)
                        current_section = new_section
                    else:
                        # 如果找不到父章节，作为一级章节
                        self.ir["sections"].append(new_section)
                        current_section = new_section
            elif current_section is not None and line.strip():
                if line.strip().startswith('![') or line.strip().startswith('|'):
                    continue  # 跳过图片和表格行
                # 处理句号粘连 (32.Learning)
                clean_line = re.sub(r'(\d+)\.([A-Z])', r'\1. \2', line.strip())
                # 处理不规范间距
                clean_line = re.sub(r'\s+', ' ', clean_line).strip()
                para_buffer.append(clean_line)
            elif not line.strip() and para_buffer and current_section:
                current_section["paragraphs"].append('\n'.join(para_buffer))
                para_buffer = []

        if current_section and para_buffer:
            current_section["paragraphs"].append('\n'.join(para_buffer))

    def _extract_references_from_text(self, lines: List[str]):
        """从文本中提取参考文献列表"""
        ref_idx = 0
        for line in lines:
            match = re.match(r'^\s*(\d+)\.\s*(.+)$', line)
            if match:
                ref_idx += 1
                raw_text = match.group(2).strip()
                # 简单解析参考文献
                author_match = re.match(r'^([^,(]+)', raw_text)
                year_match = re.search(r'\((\d{4})\)', raw_text)
                title_match = re.search(r'\)\.\s*([^.]+)\.', raw_text)
                
                author = author_match.group(1).strip() if author_match else "Unknown"
                year = year_match.group(1) if year_match else "2024"
                title = title_match.group(1).strip() if title_match else "Untitled"
                
                # 生成 key
                first_name = author.split(',')[0].strip().lower()
                key = f"{first_name}{year}"
                
                self.ir["references"].append({
                    "id": f"reference_{ref_idx:03d}",
                    "key": key,
                    "type": "article",
                    "fields": {
                        "author": author,
                        "year": year,
                        "title": title
                    },
                    "raw_text": raw_text
                })

    def _extract_figures(self, text: str):
        """提取图片"""
        pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        for i, match in enumerate(re.finditer(pattern, text)):
            caption = match.group(1)
            path = match.group(2)
            self.ir["figures"].append({
                "id": f"figure_{i+1:03d}",
                "number": i + 1,
                "caption": caption,
                "label": "",
                "file_path": path
            })

    def _extract_tables(self, text: str):
        """提取 Markdown 表格"""
        lines = text.split('\n')
        i = 0
        table_idx = 0
        while i < len(lines):
            if '|' in lines[i] and i + 1 < len(lines) and '---' in lines[i + 1]:
                table_idx += 1
                headers = [h.strip() for h in lines[i].split('|') if h.strip()]
                rows = []
                i += 2  # 跳过分隔行
                while i < len(lines) and '|' in lines[i]:
                    cells = [c.strip() for c in lines[i].split('|') if c.strip()]
                    rows.append({
                        "row": len(rows),
                        "cells": [{"text": c} for c in cells]
                    })
                    i += 1

                self.ir["tables"].append({
                    "id": f"table_{table_idx:03d}",
                    "number": table_idx,
                    "caption": "",
                    "label": "",
                    "headers": [{"row": 0, "cells": [{"text": h} for h in headers]}],
                    "rows": rows
                })
            else:
                i += 1

    def _extract_equations(self, text: str):
        """提取公式"""
        # 块级公式 $$...$$
        pattern_block = r'\$\$(.+?)\$\$'
        for i, match in enumerate(re.finditer(pattern_block, text, re.DOTALL)):
            self.ir["equations"].append({
                "id": f"equation_{i+1:03d}",
                "number": i + 1,
                "type": "display",
                "latex": match.group(1).strip(),
                "label": ""
            })
        
        # 提取行内公式或特定格式的公式 L = -sum(y * log(p))
        # 使用贪婪匹配以包含嵌套括号，但限制在行内
        pattern_simple = r'(L\s*=\s*-?\s*sum\(.+\))'
        for match in re.finditer(pattern_simple, text):
            latex = match.group(1)
            self.ir["equations"].append({
                "id": f"equation_simple_{len(self.ir['equations'])+1:03d}",
                "number": len(self.ir['equations']) + 1,
                "type": "inline",
                "latex": latex.strip(),
                "label": ""
            })
