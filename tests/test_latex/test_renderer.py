"""LaTeX 渲染器测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.latex.renderer import LatexRenderer
from src.processors.document_ir import DocumentIRManager


def test_render_basic():
    """测试基础渲染"""
    ir_manager = DocumentIRManager()
    ir_manager.create_ir("test_001")
    ir_manager.set_title("Test Title")
    ir_manager.set_abstract("Test abstract.")
    ir_manager.add_section("Introduction", level=1)
    ir_manager.add_paragraph("section_001", "This is a test paragraph.")

    renderer = LatexRenderer()
    result = renderer.render(ir_manager.ir, output_dir="test_output")

    assert Path("test_output/main.tex").exists()
    assert Path("test_output/references.bib").exists()


def test_render_with_template():
    """测试带模板规格的渲染"""
    template_spec = {
        "document_class": "elsarticle",
        "class_options": ["preprint", "review"],
        "required_packages": ["graphicx", "amsmath"],
        "bibliography_bst": "elsarticle-num"
    }

    ir_manager = DocumentIRManager()
    ir_manager.create_ir("test_002")
    ir_manager.set_title("Template Test")

    renderer = LatexRenderer(template_spec)
    result = renderer.render(ir_manager.ir, output_dir="test_output_template")

    main_tex = Path("test_output_template/main.tex").read_text()
    assert "elsarticle" in main_tex
    assert "elsarticle-num" in main_tex
