"""翻译处理器 - 对 Document IR 执行学术翻译"""

from typing import Dict, List, Optional
from pathlib import Path
import json


class Translator:
    """学术翻译处理器，将中文 IR 转换为英文 IR"""

    def __init__(self):
        self.terminology = {}
        self.translation_memory = {}
        self.style_profile = {}

    def load_terminology(self, file_path: str):
        """加载术语词典"""
        path = Path(file_path)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '|' in line and not line.startswith('|') and not line.startswith('#'):
                        parts = line.strip().split('|')
                        if len(parts) >= 3:
                            zh = parts[0].strip()
                            en = parts[1].strip()
                            if zh and en:
                                self.terminology[zh] = en

    def load_translation_memory(self, file_path: str):
        """加载翻译记忆"""
        path = Path(file_path)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                self.translation_memory = json.load(f)

    def translate_ir(self, ir: Dict, section_prompts: Dict = None) -> Dict:
        """翻译整个 Document IR

        注意：实际翻译由 AI 根据 prompts/translation/ 中的提示词执行。
        此方法负责构建翻译任务并验证翻译结果。
        """
        translated_ir = ir.copy()
        translated_ir["metadata"]["source_language"] = ir["metadata"].get("source_language", "zh")
        translated_ir["metadata"]["target_language"] = "en"

        # 构建翻译任务列表
        tasks = self._build_translation_tasks(ir)

        # 应用翻译记忆
        for task in tasks:
            task["suggested"] = self._check_memory(task["source"])

        return {
            "translated_ir": translated_ir,
            "translation_tasks": tasks,
            "statistics": {
                "total_segments": len(tasks),
                "memory_hits": sum(1 for t in tasks if t["suggested"]),
                "terminology_count": len(self.terminology)
            }
        }

    def _build_translation_tasks(self, ir: Dict) -> List[Dict]:
        """构建翻译任务列表"""
        tasks = []

        # 标题
        if ir.get("title", {}).get("text"):
            tasks.append({
                "id": ir["title"]["id"],
                "type": "title",
                "source": ir["title"]["text"],
                "prompt_file": "prompts/translation/title.md"
            })

        # 摘要
        if ir.get("abstract", {}).get("text"):
            tasks.append({
                "id": ir["abstract"]["id"],
                "type": "abstract",
                "source": ir["abstract"]["text"],
                "prompt_file": "prompts/translation/abstract.md"
            })

        # 章节
        section_type_map = {
            "introduction": "introduction",
            "引言": "introduction",
            "related work": "literature_review",
            "文献综述": "literature_review",
            "method": "methodology",
            "方法": "methodology",
            "result": "results",
            "结果": "results",
            "discussion": "discussion",
            "讨论": "discussion",
            "conclusion": "conclusion",
            "结论": "conclusion"
        }

        for section in ir.get("sections", []):
            title_lower = section["title"].lower()
            section_type = "general"
            for key, val in section_type_map.items():
                if key in title_lower:
                    section_type = val
                    break

            for para in section.get("paragraphs", []):
                tasks.append({
                    "id": section["id"],
                    "type": section_type,
                    "source": para,
                    "prompt_file": f"prompts/translation/{section_type}.md"
                })

        return tasks

    def _check_memory(self, source: str) -> Optional[str]:
        """检查翻译记忆"""
        return self.translation_memory.get(source)

    def validate_translation(self, source_ir: Dict, translated_ir: Dict) -> Dict:
        """验证翻译质量"""
        issues = []

        # 检查结构一致性
        if len(source_ir.get("sections", [])) != len(translated_ir.get("sections", [])):
            issues.append("章节数量不一致")

        if len(source_ir.get("figures", [])) != len(translated_ir.get("figures", [])):
            issues.append("图片数量不一致")

        if len(source_ir.get("tables", [])) != len(translated_ir.get("tables", [])):
            issues.append("表格数量不一致")

        if len(source_ir.get("equations", [])) != len(translated_ir.get("equations", [])):
            issues.append("公式数量不一致")

        # 检查引用一致性
        source_citations = {c["key"] for c in source_ir.get("citations", [])}
        translated_citations = {c["key"] for c in translated_ir.get("citations", [])}
        if source_citations != translated_citations:
            issues.append("引用键不一致")

        # 检查公式未被修改
        for i, eq in enumerate(source_ir.get("equations", [])):
            if i < len(translated_ir.get("equations", [])):
                if eq["latex"] != translated_ir["equations"][i]["latex"]:
                    issues.append(f"公式 {eq['id']} 被修改")

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }

    def save_translation_memory(self, file_path: str):
        """保存翻译记忆"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.translation_memory, f, ensure_ascii=False, indent=2)
