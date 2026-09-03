"""Markdown 解析器测试"""

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.parsers.markdown_parser import MarkdownParser


def test_parse_title():
    """测试标题解析"""
    parser = MarkdownParser()
    ir = parser.parse(str(Path(__file__).parent / "data" / "test.md"))
    assert ir["title"]["text"] == "Test Paper Title"


def test_parse_sections():
    """测试章节解析"""
    parser = MarkdownParser()
    ir = parser.parse(str(Path(__file__).parent / "data" / "test.md"))
    assert len(ir["sections"]) > 0
    assert ir["sections"][0]["title"] == "Introduction"


def test_parse_figures():
    """测试图片解析"""
    parser = MarkdownParser()
    ir = parser.parse(str(Path(__file__).parent / "data" / "test.md"))
    # 根据测试数据验证


def test_parse_tables():
    """测试表格解析"""
    parser = MarkdownParser()
    ir = parser.parse(str(Path(__file__).parent / "data" / "test.md"))
    # 根据测试数据验证
