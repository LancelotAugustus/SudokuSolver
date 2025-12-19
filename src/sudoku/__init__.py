# __init__.py
"""
Sudoku Solver - 一个基于回溯算法的数独求解器
"""

from .exception import SudokuError
from .board import Board
from .rules import (
    Rule,
    NormalSudokuRowRule,
    NormalSudokuColumnRule,
    Normal9x9SudokuBlockRule
)
from .solver import Solver

__all__ = [
    'SudokuError',
    'Board',
    'Rule',
    'NormalSudokuRowRule',
    'NormalSudokuColumnRule',
    'Normal9x9SudokuBlockRule',
    'Solver',
]

__version__ = '0.2.0'
