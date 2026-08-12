"""QA 报告生成器 - 生成质量检查报告"""

from pathlib import Path
from typing import Dict, List
from datetime import datetime


class QAReport:
    """生成质量检查报告"""

    def __init__(self):
        self.content = ""

    def generate(self, results: Dict, output_dir: str = "paper_project"):
        """生成质量报告文件"""
        self.content = self._build_report(results)

        output_path = Path(output_dir) / "QA" / "quality_report.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(self.content, encoding='utf-8')

    def _build_report(self, results: Dict) -> str:
        """构建报告内容"""
        # 确定总体状态
        all_valid = all(r.get("valid", True) for r in results.values())
        has_issues = any(r.get("issues") for r in results.values())

        if all_valid and not has_issues:
            status = "PASS"
        elif all_valid:
            status = "PASS_WITH_WARNINGS"
        else:
            status = "FAIL"

        lines = [
            "# 质量报告",
            "",
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## 总体状态",
            "",
            f"**{status}**",
            "",
            "## 检查摘要",
            ""
        ]

        # 内容检查
        if "content" in results:
            lines.append("### 内容检查")
            content = results["content"]
            lines.append(f"- 状态: {'PASS' if content['valid'] else 'FAIL'}")
            if content.get("issues"):
                for issue in content["issues"]:
                    lines.append(f"- 问题: {issue}")
            lines.append("")

        # 参考文献检查
        if "references" in results:
            lines.append("### 参考文献检查")
            refs = results["references"]
            lines.append(f"- 状态: {'PASS' if refs['valid'] else 'FAIL'}")
            stats = refs.get("statistics", {})
            lines.append(f"- 总引用数: {stats.get('total_citations', 0)}")
            lines.append(f"- 总参考文献数: {stats.get('total_references', 0)}")
            lines.append(f"- 已解析: {stats.get('resolved', 0)}")
            lines.append(f"- 未解析: {stats.get('unresolved', 0)}")
            lines.append(f"- 未引用: {stats.get('unused', 0)}")
            if refs.get("issues"):
                for issue in refs["issues"]:
                    lines.append(f"- 问题: {issue}")
            lines.append("")

        # 图片检查
        if "figures" in results:
            lines.append("### 图片检查")
            figs = results["figures"]
            lines.append(f"- 状态: {'PASS' if figs['valid'] else 'FAIL'}")
            stats = figs.get("statistics", {})
            lines.append(f"- 总图片数: {stats.get('total', 0)}")
            if figs.get("issues"):
                for issue in figs["issues"]:
                    lines.append(f"- 问题: {issue}")
            lines.append("")

        # 表格检查
        if "tables" in results:
            lines.append("### 表格检查")
            tabs = results["tables"]
            lines.append(f"- 状态: {'PASS' if tabs['valid'] else 'FAIL'}")
            stats = tabs.get("statistics", {})
            lines.append(f"- 总表格数: {stats.get('total', 0)}")
            if tabs.get("issues"):
                for issue in tabs["issues"]:
                    lines.append(f"- 问题: {issue}")
            lines.append("")

        # LaTeX 检查
        if "latex" in results:
            lines.append("### LaTeX 检查")
            latex = results["latex"]
            lines.append(f"- 状态: {'PASS' if latex['valid'] else 'FAIL'}")
            stats = latex.get("statistics", {})
            lines.append(f"- 编译错误: {stats.get('errors', 0)}")
            lines.append(f"- 编译警告: {stats.get('warnings', 0)}")
            lines.append(f"- Overfull hbox: {stats.get('overfull', 0)}")
            lines.append(f"- Underfull hbox: {stats.get('underfull', 0)}")
            if latex.get("issues"):
                for issue in latex["issues"]:
                    lines.append(f"- 问题: {issue}")
            lines.append("")

        # 汇总问题
        all_issues = []
        for category, result in results.items():
            for issue in result.get("issues", []):
                all_issues.append(f"[{category}] {issue}")

        if all_issues:
            lines.append("## 详细问题列表")
            lines.append("")
            for i, issue in enumerate(all_issues, 1):
                lines.append(f"{i}. {issue}")
            lines.append("")

        lines.append("## 未解决问题")
        lines.append("")
        if all_issues:
            for issue in all_issues:
                lines.append(f"- {issue}")
        else:
            lines.append("无")
        lines.append("")

        return '\n'.join(lines)

    def get_content(self) -> str:
        """获取报告内容"""
        return self.content
