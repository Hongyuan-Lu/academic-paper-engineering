"""端到端工作流测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.parsers.markdown_parser import MarkdownParser
from src.processors.document_ir import DocumentIRManager
from src.latex.renderer import LatexRenderer
from src.latex.validator import LatexValidator
from src.qa.checker import QAChecker


def test_markdown_to_latex():
    """测试 Markdown -> LaTeX 完整流程"""
    # 1. 解析
    parser = MarkdownParser()
    ir = parser.parse(str(Path(__file__).parent / "data" / "sample.md"))

    # 2. 验证 IR
    ir_manager = DocumentIRManager()
    ir_manager.load_ir(ir)
    validation = ir_manager.validate()

    # 3. 渲染
    renderer = LatexRenderer()
    render_result = renderer.render(ir, output_dir="e2e_output")

    # 4. 验证 LaTeX
    validator = LatexValidator()
    latex_validation = validator.validate_project("e2e_output")

    # 5. QA
    checker = QAChecker()
    qa_result = checker.check_all(ir)

    assert render_result["sections"] > 0
    assert Path("e2e_output/main.tex").exists()
