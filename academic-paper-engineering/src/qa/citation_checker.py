"""引用检查器 - 检查引用和参考文献的完整性"""

from typing import Dict, List


class CitationChecker:
    """检查引用和参考文献"""

    def check(self, ir: Dict) -> Dict:
        """执行引用检查"""
        issues = []

        citations = ir.get("citations", [])
        references = ir.get("references", [])

        # 引用 -> 参考文献 映射检查
        ref_keys = {r.get("key") for r in references if r.get("key")}
        cite_keys = {c.get("key") for c in citations if c.get("key")}

        # 有引用但无参考文献
        unresolved = cite_keys - ref_keys
        for key in unresolved:
            issues.append(f"引用 '{key}' 无对应参考文献")

        # 有参考文献但无引用
        unused = ref_keys - cite_keys
        for key in unused:
            issues.append(f"参考文献 '{key}' 未被引用")

        # 重复参考文献
        seen = {}
        for ref in references:
            key = ref.get("key", "")
            if key in seen:
                issues.append(f"重复参考文献: {key}")
            else:
                seen[key] = True

        # 引用键格式检查
        import re
        for ref in references:
            key = ref.get("key", "")
            if key and not re.match(r'^[a-z][a-z0-9_]*$', key):
                issues.append(f"引用键格式不规范: {key}")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "total_citations": len(citations),
                "total_references": len(references),
                "resolved": len(cite_keys & ref_keys),
                "unresolved": len(unresolved),
                "unused": len(unused),
                "duplicates": len(issues) - len(unresolved) - len(unused)
            }
        }
