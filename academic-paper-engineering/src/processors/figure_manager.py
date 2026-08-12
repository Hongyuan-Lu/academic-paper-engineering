"""图片管理器 - 管理图片匹配和插入"""

from typing import Dict, List, Optional
from pathlib import Path
import re


class FigureManager:
    """管理 Document IR 中的图片"""

    def __init__(self):
        self.figures = []
        self.assets = []
        self.matches = []

    def load_from_ir(self, ir: Dict):
        """从 IR 加载图片"""
        self.figures = ir.get("figures", [])
        self.assets = ir.get("assets", [])

    def load_assets(self, asset_dir: str):
        """从目录加载图片资产"""
        path = Path(asset_dir)
        extensions = {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.svg', '.webp', '.pdf', '.eps'}
        for file_path in path.iterdir():
            if file_path.suffix.lower() in extensions:
                self.assets.append({
                    "id": f"asset_{len(self.assets) + 1:03d}",
                    "path": str(file_path),
                    "filename": file_path.name,
                    "format": file_path.suffix[1:].lower()
                })

    def match_figures(self, threshold: float = 0.85) -> List[Dict]:
        """匹配图片与资产"""
        self.matches = []
        for fig in self.figures:
            best_match = None
            best_confidence = 0.0

            for asset in self.assets:
                confidence = self._calculate_confidence(fig, asset)
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_match = asset

            if best_match and best_confidence >= threshold:
                status = "auto_insert"
            elif best_match and best_confidence >= 0.60:
                status = "insert_with_warning"
            else:
                status = "no_match"

            self.matches.append({
                "figure_id": fig["id"],
                "asset": best_match["path"] if best_match else "",
                "confidence": best_confidence,
                "status": status,
                "reason": self._explain_match(fig, best_match, best_confidence)
            })

        return self.matches

    def _calculate_confidence(self, figure: Dict, asset: Dict) -> float:
        """计算匹配置信度"""
        confidence = 0.0
        fig_num = figure.get("number", 0)
        filename = asset.get("filename", "").lower()
        caption = figure.get("caption", "").lower()

        # 1. 显式图号匹配
        num_patterns = [f"fig{fig_num}", f"figure{fig_num}", f"图{fig_num}", f"f{fig_num}"]
        for pattern in num_patterns:
            if pattern in filename:
                confidence = max(confidence, 0.95)

        # 2. 文件名关键词匹配
        caption_words = [w for w in caption.split() if len(w) > 3]
        for word in caption_words:
            if word in filename:
                confidence = max(confidence, confidence + 0.15)

        confidence = min(confidence, 0.90)

        # 3. 格式匹配
        if asset.get("format") in ['pdf', 'eps']:
            confidence = min(confidence + 0.05, 1.0)

        return confidence

    def _explain_match(self, figure: Dict, asset: Optional[Dict], confidence: float) -> str:
        """解释匹配原因"""
        if not asset:
            return "无匹配资产"
        if confidence >= 0.85:
            return f"高置信度匹配: {asset['filename']} ({confidence:.2f})"
        elif confidence >= 0.60:
            return f"中等置信度匹配: {asset['filename']} ({confidence:.2f})"
        else:
            return f"低置信度匹配: {asset['filename']} ({confidence:.2f})"

    def get_unmatched(self) -> List[Dict]:
        """获取未匹配的图片"""
        return [m for m in self.matches if m["status"] == "no_match"]

    def validate(self) -> Dict:
        """验证图片完整性"""
        issues = []

        for fig in self.figures:
            if not fig.get("caption"):
                issues.append(f"图片 {fig['id']} 缺少标题说明")
            if not fig.get("label"):
                issues.append(f"图片 {fig['id']} 缺少标签")

        for match in self.matches:
            if match["status"] == "no_match":
                issues.append(f"图片 {match['figure_id']} 未匹配到资产")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "statistics": {
                "total_figures": len(self.figures),
                "matched": sum(1 for m in self.matches if m["status"] != "no_match"),
                "unmatched": sum(1 for m in self.matches if m["status"] == "no_match")
            }
        }
