# src/sudoku/__init__.py
"""
Sudoku Solver - 一个基于回溯算法的数独求解器
"""

from .exceptions import SudokuError
from .board import Board
from .rules import *
from .solver import Solver

__all__ = [
    'SudokuError',
    'Board',
    'Rule',
    'Solver',
    'RowRule',
    'ColumnRule',
    'Normal9x9BlockRule',
    'NonConsecutiveRule',
    'ThermometerRule',
    'KillerRule',
]