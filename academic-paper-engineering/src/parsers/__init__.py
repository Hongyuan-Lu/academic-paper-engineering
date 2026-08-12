"""
文档解析器模块
将各种格式的文档解析为学术文档中间表示（Document IR）
"""

from .docx_parser import DocxParser
from .pdf_parser import PdfParser
from .markdown_parser import MarkdownParser
from .latex_parser import LatexParser
from .pptx_parser import PptxParser
from .xlsx_parser import XlsxParser

__all__ = [
    'DocxParser', 'PdfParser', 'MarkdownParser',
    'LatexParser', 'PptxParser', 'XlsxParser'
]
