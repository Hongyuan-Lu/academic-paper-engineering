"""资产检查器 - 检查图片和表格的完整性"""

from pathlib import Path
from typing import Dict, List


class AssetChecker:
    """检查图片和表格资产"""

    def check_figures(self, ir: Dict) -> Dict:
        """检查图片"""
        issues = []
        figures = ir.get("figures", [])

        seen_numbers = {}
        for fig in figures:
            # 缺失标题说明
            if not fig.get("caption"):
                issues.append(f"图片 {fig.get('id', '')} 缺少标题说明")

            # 缺失标签
            if not fig.get("label"):
                issues.append(f"图片 {fig.get('id', '')} 缺少标签")

            # 编号检查
            num = fig.get("number", 0)
            if num in seen_numbers:
                issues.append(f"图片编号重复: {num}")
            else:
                seen_numbers[num] = fig.get("id", "")

            # 文件路径检查
            file_path = fig.get("file_path", "")
            if file_path:
                path = Path(file_path)
                if not path.exists():
                    issues.append(f"图片文件不存在: {file_path}")

        # 编号连续性
        numbers = sorted(fig.get("number", 0) for fig in figures)
        for i, num in enumerate(numbers):
            if num != i + 1:
                issues.append(f"图片编号不连续: 期望 {i+1}, 实际 {num}")
                break

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "total": len(figures),
                "with_caption": sum(1 for f in figures if f.get("caption")),
                "with_label": sum(1 for f in figures if f.get("label")),
                "missing_file": sum(1 for f in figures if f.get("file_path") and not Path(f["file_path"]).exists())
            }
        }

    def check_tables(self, ir: Dict) -> Dict:
        """检查表格"""
        issues = []
        tables = ir.get("tables", [])

        for table in tables:
            # 缺失标题说明
            if not table.get("caption"):
                issues.append(f"表格 {table.get('id', '')} 缺少标题说明")

            # 缺失标签
            if not table.get("label"):
                issues.append(f"表格 {table.get('id', '')} 缺少标签")

            # 列数一致性
            headers = table.get("headers", [])
            rows = table.get("rows", [])

            header_cols = 0
            if headers:
                header_cols = len(headers[0].get("cells", []))

            for i, row in enumerate(rows):
                row_cols = len(row.get("cells", []))
                if header_cols > 0 and row_cols != header_cols:
                    issues.append(f"表格 {table.get('id', '')} 行 {i} 列数({row_cols})与表头({header_cols})不一致")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "total": len(tables),
                "valid": sum(1 for t in tables if self._is_table_valid(t)),
                "invalid": sum(1 for t in tables if not self._is_table_valid(t))
            }
        }

    def _is_table_valid(self, table: Dict) -> bool:
        """检查单个表格是否有效"""
        if not table.get("caption"):
            return False
        if not table.get("label"):
            return False
        return True
