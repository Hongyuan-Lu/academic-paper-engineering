"""参考文献管理器测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.processors.reference_manager import ReferenceManager


def test_generate_citation_key():
    """测试引用键生成"""
    manager = ReferenceManager()
    key = manager.generate_citation_key("Smith, John", "2020", "Deep Learning for Segmentation")
    assert key == "smith2020deep"


def test_generate_bibtex():
    """测试 BibTeX 生成"""
    manager = ReferenceManager()
    ref = {
        "type": "article",
        "key": "smith2020deep",
        "fields": {
            "title": "Deep Learning for Segmentation",
            "author": "Smith, John",
            "journal": "Nature",
            "year": "2020"
        }
    }

    bibtex = manager.generate_bibtex(ref)
    assert "@article{smith2020deep," in bibtex
    assert "Deep Learning for Segmentation" in bibtex
    assert "Nature" in bibtex


def test_resolve_citations():
    """测试引用解析"""
    manager = ReferenceManager()
    manager.citations = [
        {"id": "c1", "key": "smith2020"},
        {"id": "c2", "key": "jones2021"},
        {"id": "c3", "key": "unknown2025"}
    ]
    manager.references = [
        {"id": "r1", "key": "smith2020"},
        {"id": "r2", "key": "jones2021"}
    ]

    result = manager.resolve_citations()
    assert result["total_citations"] == 3
    assert result["resolved"] == 2
    assert result["unresolved"] == 1


def test_check_duplicates():
    """测试重复检查"""
    manager = ReferenceManager()
    manager.references = [
        {"id": "r1", "key": "smith2020"},
        {"id": "r2", "key": "smith2020"}
    ]

    duplicates = manager.check_duplicates()
    assert len(duplicates) == 1
    assert duplicates[0]["key"] == "smith2020"


def test_check_unused():
    """测试未引用检查"""
    manager = ReferenceManager()
    manager.citations = [
        {"id": "c1", "key": "smith2020"}
    ]
    manager.references = [
        {"id": "r1", "key": "smith2020"},
        {"id": "r2", "key": "jones2021"}
    ]

    unused = manager.check_unused()
    assert len(unused) == 1
    assert unused[0]["key"] == "jones2021"


def test_render_citation():
    """测试引用渲染"""
    manager = ReferenceManager()

    assert manager.render_citation("key", "numeric") == "\\cite{key}"
    assert manager.render_citation("key", "author-year") == "\\citep{key}"
    assert manager.render_citation("key", "textual") == "\\citet{key}"


def test_validate():
    """测试完整验证"""
    manager = ReferenceManager()
    manager.citations = [
        {"id": "c1", "key": "smith2020"},
        {"id": "c2", "key": "unknown"}
    ]
    manager.references = [
        {"id": "r1", "key": "smith2020", "type": "article", "fields": {}}
    ]

    result = manager.validate()
    assert result["valid"] is False
    assert result["statistics"]["unresolved"] == 1
