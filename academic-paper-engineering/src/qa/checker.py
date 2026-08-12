"""QA 检查器 - 执行全面质量检查"""

from typing import Dict, List
from .citation_checker import CitationChecker
from .asset_checker import AssetChecker
from .report import QAReport


class QAChecker:
    """执行最终质量检查"""

    def __init__(self):
        self.citation_checker = CitationChecker()
        self.asset_checker = AssetChecker()
        self.report = QAReport()

    def check_all(self, ir: Dict, compile_result: Dict = None,
                  source_ir: Dict = None) -> Dict:
        """执行全部质量检查"""
        results = {}

        # 内容检查
        results["content"] = self._check_content(ir, source_ir)

        # 参考文献检查
        results["references"] = self.citation_checker.check(ir)

        # 图片检查
        results["figures"] = self.asset_checker.check_figures(ir)

        # 表格检查
        results["tables"] = self.asset_checker.check_tables(ir)

        # LaTeX 编译检查
        if compile_result:
            results["latex"] = self._check_latex(compile_result)

        # 生成报告
        self.report.generate(results)

        # 确定总体状态
        all_valid = all(r.get("valid", True) for r in results.values())
        has_warnings = any(r.get("warnings") for r in results.values())

        if all_valid and not has_warnings:
            status = "PASS"
        elif all_valid and has_warnings:
            status = "PASS_WITH_WARNINGS"
        else:
            status = "FAIL"

        return {
            "status": status,
            "results": results,
            "report_file": "QA/quality_report.md"
        }

    def _check_content(self, ir: Dict, source_ir: Dict = None) -> Dict:
        """检查内容完整性"""
        issues = []

        if not ir.get("title", {}).get("text"):
            issues.append("缺少标题")
        if not ir.get("abstract", {}).get("text"):
            issues.append("缺少摘要")
        if not ir.get("sections"):
            issues.append("缺少章节内容")

        # 检查重复段落
        all_paragraphs = []
        for section in ir.get("sections", []):
            all_paragraphs.extend(section.get("paragraphs", []))

        seen = {}
        for i, para in enumerate(all_paragraphs):
            if para in seen:
                issues.append(f"重复段落: 位置 {seen[para]} 和 {i}")
            else:
                seen[para] = i

        # 与源文档对比
        if source_ir:
            if len(source_ir.get("sections", [])) != len(ir.get("sections", [])):
                issues.append("章节数量与源文档不一致")

            source_nums = [s.get("number") for s in source_ir.get("sections", [])]
            ir_nums = [s.get("number") for s in ir.get("sections", [])]
            if source_nums != ir_nums:
                issues.append("章节编号与源文档不一致")

        return {"valid": len(issues) == 0, "issues": issues}

    def _check_latex(self, compile_result: Dict) -> Dict:
        """检查 LaTeX 编译结果"""
        issues = []

        if not compile_result.get("success"):
            issues.append("编译失败")
            issues.extend(compile_result.get("errors", []))
        else:
            overfull = compile_result.get("overfull_hbox", [])
            if len(overfull) > 5:
                issues.append(f"Overfull hbox 过多: {len(overfull)}")

            underfull = compile_result.get("underfull_hbox", [])
            if len(underfull) > 10:
                issues.append(f"Underfull hbox 过多: {len(underfull)}")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "errors": len(compile_result.get("errors", [])),
                "warnings": len(compile_result.get("warnings", [])),
                "overfull": len(compile_result.get("overfull_hbox", [])),
                "underfull": len(compile_result.get("underfull_hbox", []))
            }
        }
