"""表格管理器测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.processors.table_manager import TableManager


def test_validate_valid_table():
    """测试有效表格验证"""
    manager = TableManager()
    manager.tables = [
        {
            "id": "table_001",
            "number": 1,
            "caption": "实验结果",
            "label": "tab:results",
            "headers": [{"row": 0, "cells": [{"text": "方法"}, {"text": "准确率"}]}],
            "rows": [
                {"row": 1, "cells": [{"text": "A", "type": "text"}, {"text": "95.3%", "type": "number"}]}
            ]
        }
    ]

    result = manager.validate_all()
    assert result["valid"] is True


def test_validate_missing_caption():
    """测试缺少标题说明"""
    manager = TableManager()
    manager.tables = [
        {
            "id": "table_001",
            "number": 1,
            "caption": "",
            "label": "tab:results",
            "headers": [{"row": 0, "cells": [{"text": "方法"}]}],
            "rows": []
        }
    ]

    result = manager.validate_all()
    assert result["valid"] is False


def test_validate_column_mismatch():
    """测试列数不一致"""
    manager = TableManager()
    manager.tables = [
        {
            "id": "table_001",
            "number": 1,
            "caption": "测试",
            "label": "tab:test",
            "headers": [{"row": 0, "cells": [{"text": "A"}, {"text": "B"}, {"text": "C"}]}],
            "rows": [
                {"row": 1, "cells": [{"text": "1"}, {"text": "2"}]}
            ]
        }
    ]

    result = manager.validate_all()
    assert result["valid"] is False
    assert any("列数" in issue for issue in result["issues"])


def test_generate_latex():
    """测试 LaTeX 表格生成"""
    manager = TableManager()
    table = {
        "id": "table_001",
        "number": 1,
        "caption": "测试表格",
        "label": "tab:test",
        "headers": [{"row": 0, "cells": [{"text": "方法"}, {"text": "准确率"}]}],
        "rows": [
            {"row": 1, "cells": [{"text": "A"}, {"text": "95.3%"}]}
        ]
    }

    latex = manager.generate_latex(table)
    assert "\\begin{table}" in latex
    assert "\\end{table}" in latex
    assert "测试表格" in latex
    assert "\\toprule" in latex
    assert "\\bottomrule" in latex
