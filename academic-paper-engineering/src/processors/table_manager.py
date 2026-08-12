"""表格管理器 - 管理表格结构和验证"""

from typing import Dict, List, Optional
import re


class TableManager:
    """管理 Document IR 中的表格"""

    def __init__(self):
        self.tables = []

    def load_from_ir(self, ir: Dict):
        """从 IR 加载表格"""
        self.tables = ir.get("tables", [])

    def validate_table(self, table: Dict) -> Dict:
        """验证单个表格结构"""
        issues = []

        headers = table.get("headers", [])
        rows = table.get("rows", [])

        # 检查列数一致性
        header_col_count = 0
        if headers:
            for h_row in headers:
                count = sum(c.get("colspan", 1) for c in h_row.get("cells", []))
                header_col_count = max(header_col_count, count)

        for i, row in enumerate(rows):
            row_col_count = sum(c.get("colspan", 1) for c in row.get("cells", []))
            if header_col_count > 0 and row_col_count != header_col_count:
                issues.append(f"行 {row.get('row', i)} 列数({row_col_count})与表头({header_col_count})不一致")

        # 检查标题说明
        if not table.get("caption"):
            issues.append("缺少标题说明")

        # 检查标签
        if not table.get("label"):
            issues.append("缺少标签")

        # 检查数值格式
        for row in rows:
            for cell in row.get("cells", []):
                if cell.get("type") == "number":
                    text = cell.get("text", "")
                    if text and not self._is_valid_number(text):
                        issues.append(f"数值格式异常: {text}")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "table_id": table.get("id", "")
        }

    def _is_valid_number(self, text: str) -> bool:
        """检查是否为有效数值"""
        cleaned = re.sub(r'[%±<>=~\[\](){}]', '', text.strip())
        cleaned = cleaned.replace(',', '')
        try:
            float(cleaned)
            return True
        except ValueError:
            return False

    def generate_latex(self, table: Dict) -> str:
        """生成表格的 LaTeX 代码"""
        caption = table.get("caption", "")
        label = table.get("label", "")
        headers = table.get("headers", [])
        rows = table.get("rows", [])

        # 确定列数
        col_count = 0
        if headers:
            col_count = len(headers[0].get("cells", []))
        elif rows:
            col_count = len(rows[0].get("cells", []))

        col_spec = 'l' + 'c' * (col_count - 1) if col_count > 0 else 'l'

        lines = [
            "\\begin{table}[htbp]",
            "  \\centering",
            f"  \\caption{{{caption}}}",
            f"  \\label{{{label}}}",
            f"  \\begin{{tabular}}{{{col_spec}}}",
            "    \\toprule"
        ]

        # 表头
        if headers:
            for h_row in headers:
                cells = h_row.get("cells", [])
                cell_texts = [c.get("text", "") for c in cells]
                lines.append("    " + " & ".join(cell_texts) + " \\\\")
            lines.append("    \\midrule")

        # 数据行
        for row in rows:
            cells = row.get("cells", [])
            cell_texts = [c.get("text", "") for c in cells]
            lines.append("    " + " & ".join(cell_texts) + " \\\\")

        lines.extend([
            "    \\bottomrule",
            "  \\end{tabular}",
            "\\end{table}"
        ])

        return '\n'.join(lines)

    def validate_all(self) -> Dict:
        """验证所有表格"""
        all_issues = []
        for table in self.tables:
            result = self.validate_table(table)
            all_issues.extend(result["issues"])

        return {
            "valid": len(all_issues) == 0,
            "issues": all_issues,
            "statistics": {
                "total_tables": len(self.tables),
                "valid_tables": sum(1 for t in self.tables if self.validate_table(t)["valid"]),
                "invalid_tables": sum(1 for t in self.tables if not self.validate_table(t)["valid"])
            }
        }
