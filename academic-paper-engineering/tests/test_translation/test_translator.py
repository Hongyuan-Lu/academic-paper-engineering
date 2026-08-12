"""翻译处理器测试"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.processors.translator import Translator


def test_load_terminology():
    """测试术语词典加载"""
    translator = Translator()
    # 测试空初始化
    assert translator.terminology == {}
    assert translator.translation_memory == {}


def test_build_translation_tasks():
    """测试翻译任务构建"""
    translator = Translator()

    ir = {
        "title": {"id": "title_001", "text": "测试标题"},
        "abstract": {"id": "abstract_001", "text": "测试摘要"},
        "sections": [
            {
                "id": "section_001",
                "title": "引言",
                "level": 1,
                "paragraphs": ["这是引言段落。"]
            },
            {
                "id": "section_002",
                "title": "方法",
                "level": 1,
                "paragraphs": ["这是方法段落。"]
            }
        ]
    }

    tasks = translator._build_translation_tasks(ir)
    assert len(tasks) > 0
    assert tasks[0]["type"] == "title"


def test_validate_translation():
    """测试翻译验证"""
    translator = Translator()

    source_ir = {
        "sections": [{"id": "s1", "paragraphs": ["段落1"]}],
        "figures": [{"id": "f1"}],
        "tables": [{"id": "t1"}],
        "equations": [{"id": "e1", "latex": "E=mc^2"}],
        "citations": [{"key": "ref1"}]
    }

    translated_ir = {
        "sections": [{"id": "s1", "paragraphs": ["Paragraph 1"]}],
        "figures": [{"id": "f1"}],
        "tables": [{"id": "t1"}],
        "equations": [{"id": "e1", "latex": "E=mc^2"}],
        "citations": [{"key": "ref1"}]
    }

    result = translator.validate_translation(source_ir, translated_ir)
    assert result["valid"] is True


def test_validate_translation_structure_mismatch():
    """测试翻译验证 - 结构不一致"""
    translator = Translator()

    source_ir = {
        "sections": [{"id": "s1"}, {"id": "s2"}],
        "figures": [],
        "tables": [],
        "equations": [],
        "citations": []
    }

    translated_ir = {
        "sections": [{"id": "s1"}],
        "figures": [],
        "tables": [],
        "equations": [],
        "citations": []
    }

    result = translator.validate_translation(source_ir, translated_ir)
    assert result["valid"] is False
