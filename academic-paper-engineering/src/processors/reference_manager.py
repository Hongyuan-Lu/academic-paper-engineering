"""参考文献管理器 - 管理引用和参考文献"""

import re
from typing import Dict, List, Optional
from pathlib import Path


class ReferenceManager:
    """管理 Document IR 中的引用和参考文献"""

    def __init__(self):
        self.citations = []
        self.references = []
        self.unresolved = []

    def load_from_ir(self, ir: Dict):
        """从 IR 加载引用和参考文献"""
        self.citations = ir.get("citations", [])
        self.references = ir.get("references", [])

    def generate_citation_key(self, author: str, year: str, title: str) -> str:
        """生成引用键"""
        # 提取第一作者姓
        first_author = author.split(',')[0].split('and')[0].strip()
        last_name = first_author.split()[-1].lower() if first_author else "unknown"
        last_name = re.sub(r'[^a-z]', '', last_name)

        # 提取关键词
        title_words = [w.lower() for w in title.split() if len(w) > 3]
        keyword = title_words[0] if title_words else "ref"

        key = f"{last_name}{year}{keyword}"
        return key

    def generate_bibtex(self, ref: Dict) -> str:
        """生成 BibTeX 条目"""
        ref_type = ref.get("type", "article")
        key = ref.get("key", "unknown")
        fields = ref.get("fields", {})

        lines = [f"@{ref_type}{{{key},"]
        for field_name, field_value in fields.items():
            lines.append(f"  {field_name} = {{{field_value}}},")
        lines.append("}")

        return '\n'.join(lines)

    def generate_bibliography(self, references: List[Dict] = None) -> str:
        """生成完整的 BibTeX 文件内容"""
        refs = references or self.references
        entries = []
        for ref in refs:
            entries.append(self.generate_bibtex(ref))
        return '\n\n'.join(entries)

    def resolve_citations(self) -> Dict:
        """解析引用，匹配参考文献"""
        ref_keys = {r["key"] for r in self.references if r.get("key")}
        resolved = []
        self.unresolved = []

        for cite in self.citations:
            if cite["key"] in ref_keys:
                resolved.append(cite)
            else:
                self.unresolved.append(cite)

        return {
            "total_citations": len(self.citations),
            "resolved": len(resolved),
            "unresolved": len(self.unresolved),
            "unresolved_list": self.unresolved
        }

    def check_duplicates(self) -> List[Dict]:
        """检查重复参考文献"""
        seen = {}
        duplicates = []
        for ref in self.references:
            key = ref.get("key", "")
            if key in seen:
                duplicates.append({
                    "key": key,
                    "first": seen[key]["id"],
                    "duplicate": ref["id"]
                })
            else:
                seen[key] = ref
        return duplicates

    def check_unused(self) -> List[Dict]:
        """检查未被引用的参考文献"""
        cited_keys = {c["key"] for c in self.citations}
        unused = [r for r in self.references if r.get("key") not in cited_keys]
        return unused

    def render_citation(self, key: str, style: str = "numeric") -> str:
        """根据引用风格渲染引用命令"""
        if style == "numeric":
            return f"\\cite{{{key}}}"
        elif style == "author-year":
            return f"\\citep{{{key}}}"
        elif style == "textual":
            return f"\\citet{{{key}}}"
        else:
            return f"\\cite{{{key}}}"

    def validate(self) -> Dict:
        """完整验证"""
        issues = []

        # 解析状态
        resolution = self.resolve_citations()
        for cite in self.unresolved:
            issues.append(f"未解析的引用: {cite['key']}")

        # 重复检查
        duplicates = self.check_duplicates()
        for dup in duplicates:
            issues.append(f"重复参考文献: {dup['key']}")

        # 键格式检查
        for ref in self.references:
            key = ref.get("key", "")
            if not key:
                issues.append(f"参考文献 {ref['id']} 缺少引用键")
            elif not re.match(r'^[a-z][a-z0-9_]*$', key):
                issues.append(f"引用键格式不规范: {key}")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "total_citations": len(self.citations),
                "total_references": len(self.references),
                "resolved": resolution["resolved"],
                "unresolved": resolution["unresolved"],
                "duplicates": len(duplicates),
                "unused": len(self.check_unused())
            }
        }

    def save_bibliography(self, file_path: str):
        """保存 BibTeX 文件"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.generate_bibliography())
