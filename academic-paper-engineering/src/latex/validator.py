"""LaTeX 验证器 - 验证 LaTeX 工程结构和内容"""

import re
from pathlib import Path
from typing import Dict, List


class LatexValidator:
    """验证 LaTeX 工程的完整性和正确性"""

    def __init__(self):
        self.issues = []

    def validate_project(self, project_dir: str) -> Dict:
        """验证完整 LaTeX 工程"""
        self.issues = []
        project_path = Path(project_dir)

        main_tex = project_path / "main.tex"
        if not main_tex.exists():
            return {
                "valid": False,
                "issues": ["主文件 main.tex 不存在"]
            }

        content = main_tex.read_text(encoding='utf-8', errors='ignore')

        self._check_document_structure(content)
        self._check_packages(content)
        self._check_labels(content)
        self._check_citations(content)
        self._check_cross_references(content)
        self._check_input_files(content, project_path)

        return {
            "valid": len(self.issues) == 0,
            "issues": self.issues
        }

    def _check_document_structure(self, content: str):
        """检查文档结构"""
        if '\\documentclass' not in content:
            self.issues.append("缺少 \\documentclass 声明")
        if '\\begin{document}' not in content:
            self.issues.append("缺少 \\begin{document}")
        if '\\end{document}' not in content:
            self.issues.append("缺少 \\end{document}")

    def _check_packages(self, content: str):
        """检查宏包"""
        required = {
            'graphicx': '图片插入',
            'amsmath': '数学公式',
            'booktabs': '表格排版'
        }
        for pkg, desc in required.items():
            if f'\\usepackage{{{pkg}' not in content and f'\\usepackage{{{pkg}}}' not in content:
                self.issues.append(f"可能缺少必需宏包: {pkg} ({desc})")

    def _check_labels(self, content: str):
        """检查标签唯一性"""
        labels = re.findall(r'\\label\{([^}]+)\}', content)
        seen = {}
        for label in labels:
            if label in seen:
                self.issues.append(f"标签重复: {label}")
            else:
                seen[label] = True

    def _check_citations(self, content: str):
        """检查引用"""
        citations = re.findall(r'\\cite[a-z]*\{([^}]+)\}', content)
        all_keys = set()
        for cite_group in citations:
            for key in cite_group.split(','):
                all_keys.add(key.strip())

        # 检查是否有对应的 \bibliography
        if all_keys and '\\bibliography' not in content:
            self.issues.append("存在引用但缺少 \\bibliography 声明")

        return all_keys

    def _check_cross_references(self, content: str):
        """检查交叉引用"""
        labels = set(re.findall(r'\\label\{([^}]+)\}', content))
        refs = set(re.findall(r'\\(?:ref|eqref|cref)\{([^}]+)\}', content))

        undefined = refs - labels
        for ref in undefined:
            self.issues.append(f"交叉引用未定义: {ref}")

    def _check_input_files(self, content: str, project_path: Path):
        """检查 \\input 引用的文件是否存在"""
        inputs = re.findall(r'\\(?:input|include)\{([^}]+)\}', content)
        for input_file in inputs:
            if not input_file.endswith('.tex'):
                input_file += '.tex'
            file_path = project_path / input_file
            if not file_path.exists():
                self.issues.append(f"引用的文件不存在: {input_file}")

    def validate_compilation_result(self, compile_result: Dict) -> Dict:
        """验证编译结果"""
        issues = []

        if not compile_result.get("success"):
            issues.append("编译失败")
            issues.extend(compile_result.get("errors", []))

        overfull = compile_result.get("overfull_hbox", [])
        if len(overfull) > 5:
            issues.append(f"Overfull hbox 过多: {len(overfull)} 个")

        underfull = compile_result.get("underfull_hbox", [])
        if len(underfull) > 10:
            issues.append(f"Underfull hbox 过多: {len(underfull)} 个")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "errors": len(compile_result.get("errors", [])),
                "warnings": len(compile_result.get("warnings", [])),
                "overfull_hbox": len(overfull),
                "underfull_hbox": len(underfull)
            }
        }
