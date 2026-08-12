"""
文档处理器模块
对 Document IR 执行各种处理操作
"""

from .document_ir import DocumentIRManager
from .translator import Translator
from .reference_manager import ReferenceManager
from .figure_manager import FigureManager
from .table_manager import TableManager
from .equation_manager import EquationManager

__all__ = [
    'DocumentIRManager', 'Translator', 'ReferenceManager',
    'FigureManager', 'TableManager', 'EquationManager'
]
