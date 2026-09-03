"""图片管理器测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.processors.figure_manager import FigureManager


def test_match_figures_high_confidence():
    """测试高置信度图片匹配"""
    manager = FigureManager()
    manager.figures = [
        {"id": "figure_001", "number": 1, "caption": "网络架构图", "label": "fig:arch"}
    ]
    manager.assets = [
        {"id": "asset_001", "path": "fig1.png", "filename": "fig1.png", "format": "png"}
    ]

    matches = manager.match_figures(threshold=0.85)
    assert len(matches) == 1
    assert matches[0]["status"] == "auto_insert"


def test_match_figures_no_match():
    """测试无匹配图片"""
    manager = FigureManager()
    manager.figures = [
        {"id": "figure_001", "number": 1, "caption": "网络架构图", "label": "fig:arch"}
    ]
    manager.assets = [
        {"id": "asset_001", "path": "screenshot.png", "filename": "screenshot.png", "format": "png"}
    ]

    matches = manager.match_figures(threshold=0.85)
    assert len(matches) == 1
    assert matches[0]["status"] == "no_match"


def test_validate_missing_caption():
    """测试缺少标题说明的验证"""
    manager = FigureManager()
    manager.figures = [
        {"id": "figure_001", "number": 1, "caption": "", "label": "fig:arch"}
    ]

    result = manager.validate()
    assert result["valid"] is False
    assert any("缺少标题说明" in issue for issue in result["issues"])


def test_get_unmatched():
    """测试获取未匹配图片"""
    manager = FigureManager()
    manager.figures = [
        {"id": "figure_001", "number": 1, "caption": "图1", "label": "fig:1"}
    ]
    manager.assets = []

    manager.match_figures()
    unmatched = manager.get_unmatched()
    assert len(unmatched) == 1
