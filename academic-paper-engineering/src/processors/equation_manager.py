"""公式管理器 - 管理数学公式的处理和验证"""

import re
from typing import Dict, List, Optional


class EquationManager:
    """管理 Document IR 中的数学公式"""

    def __init__(self):
        self.equations = []

    def load_from_ir(self, ir: Dict):
        """从 IR 加载公式"""
        self.equations = ir.get("equations", [])

    def validate_equation(self, eq: Dict) -> Dict:
        """验证单个公式"""
        issues = []

        latex = eq.get("latex", "")
        label = eq.get("label", "")
        eq_type = eq.get("type", "numbered")

        # 检查 LaTeX 语法基本正确性
        brace_count = 0
        for char in latex:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
        if brace_count != 0:
            issues.append(f"大括号不匹配: 差值 {brace_count}")

        # 检查环境闭合
        env_patterns = re.findall(r'\\begin\{(\w+)\}', latex)
        end_patterns = re.findall(r'\\end\{(\w+)\}', latex)
        for env in env_patterns:
            if env not in end_patterns:
                issues.append(f"环境未闭合: {env}")

        # 检查标签
        if eq_type == "numbered" and not label:
            issues.append("编号公式缺少标签")

        # 检查标签唯一性
        # (在 validate_all 中检查)

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "equation_id": eq.get("id", "")
        }

    def validate_all(self) -> Dict:
        """验证所有公式"""
        all_issues = []
        labels = {}

        for eq in self.equations:
            result = self.validate_equation(eq)
            all_issues.extend(result["issues"])

            label = eq.get("label", "")
            if label:
                if label in labels:
                    all_issues.append(f"标签重复: {label} ({eq['id']} 和 {labels[label]})")
                else:
                    labels[label] = eq["id"]

        # 检查编号连续性
        numbers = [eq.get("number", 0) for eq in self.equations if eq.get("number")]
        for i, num in enumerate(numbers):
            if num != i + 1:
                all_issues.append(f"公式编号不连续: 期望 {i+1}, 实际 {num}")
                break

        return {
            "valid": len(all_issues) == 0,
            "issues": all_issues,
            "statistics": {
                "total_equations": len(self.equations),
                "valid_equations": sum(1 for eq in self.equations if self.validate_equation(eq)["valid"]),
                "invalid_equations": sum(1 for eq in self.equations if not self.validate_equation(eq)["valid"])
            }
        }

    def generate_latex(self, eq: Dict) -> str:
        """生成公式的 LaTeX 代码"""
        eq_type = eq.get("type", "numbered")
        latex = eq.get("latex", "")
        label = eq.get("label", "")

        if eq_type == "inline":
            return f"${latex}$"
        elif eq_type == "display":
            return f"\\[{latex}\\]"
        elif eq_type == "numbered":
            if label:
                return f"\\begin{{equation}}\n  {latex}\n  \\label{{{label}}}\n\\end{{equation}}"
            else:
                return f"\\begin{{equation}}\n  {latex}\n\\end{{equation}}"
        elif eq_type == "align":
            if label:
                return f"\\begin{{align}}\n  {latex}\n  \\label{{{label}}}\n\\end{{align}}"
            else:
                return f"\\begin{{align}}\n  {latex}\n\\end{{align}}"
        else:
            return f"\\begin{{equation}}\n  {latex}\n\\end{{equation}}"

    def check_references(self, ir: Dict) -> Dict:
        """检查公式交叉引用"""
        eq_labels = {eq.get("label", "") for eq in self.equations if eq.get("label")}

        # 在文本中搜索 \ref{eq:...} 引用
        ref_pattern = r'\\ref\{(eq:[^}]+)\}'
        referenced = set()

        for section in ir.get("sections", []):
            for para in section.get("paragraphs", []):
                for match in re.finditer(ref_pattern, para):
                    referenced.add(match.group(1))

        unreferenced = eq_labels - referenced
        undefined_refs = referenced - eq_labels

        return {
            "total_equations": len(self.equations),
            "total_labels": len(eq_labels),
            "referenced": len(referenced),
            "unreferenced": len(unreferenced),
            "undefined_references": len(undefined_refs),
            "unreferenced_labels": list(unreferenced),
            "undefined_reference_labels": list(undefined_refs)
        }
