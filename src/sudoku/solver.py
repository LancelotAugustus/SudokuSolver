# src/sudoku/solver.py
"""
数独求解器模块，实现回溯算法求解数独。
"""

from typing import Optional
from tqdm import tqdm
from .board import Board
from .rules import Rule


class Solver:
    """数独求解器"""

    def __init__(self, board: Board, *rules: Rule):
        """
        初始化求解器

        Args:
            board: 要求解的数独棋盘
            *rules: 要应用的规则列表

        Raises:
            SudokuError: 如果棋盘与任何规则不兼容
        """
        self.board = board.copy()
        self.rules = rules
        self.steps = 0
        self.pbar = None

        self.validate_compatibility()

    def validate_compatibility(self) -> None:
        """
        一次性调用所有rule实例的validate_compatibility方法

        Raises:
            SudokuError: 如果棋盘与任何规则不兼容
        """
        for rule in self.rules:
            rule.validate_compatibility(self.board)

    def is_valid(self) -> bool:
        """
        检查当前棋盘是否满足所有规则

        Returns:
            如果满足所有规则返回True，否则返回False
        """
        for rule in self.rules:
            if not rule.is_valid(self.board):
                return False
        return True

    def try_set_digit(self, row: int, col: int, digit: int) -> bool:
        """
        尝试在指定位置放置数字

        Args:
            row: 行索引
            col: 列索引
            digit: 要放置的数字

        Returns:
            如果放置后棋盘有效则返回True，否则返回False
        """
        # 增加步数计数
        self.steps += 1
        self.pbar.update(1)

        # 记录原始数字
        original_digit = self.board.get_digit(row, col)

        # 放置数字
        self.board.set_digit(row, col, digit)

        # 检查是否满足所有规则
        is_valid = self.is_valid()

        # 如果不满足规则，则恢复原始状态
        if not is_valid:
            self.board.set_digit(row, col, original_digit)

        return is_valid

    def solve(self) -> bool:
        """
        使用回溯算法求解数独

        Returns:
            如果找到解返回True，否则返回False
        """
        # 找到第一个空格
        empty_pos = self.board.find_empty_cell()

        # 如果没有空格，检查棋盘是否完全满足规则
        if not empty_pos:
            return self.is_valid()

        row, col = empty_pos

        # 尝试所有可能的数字
        for digit in range(1, self.board.size + 1):
            if self.try_set_digit(row, col, digit):
                # 递归求解
                if self.solve():
                    return True

                # 如果当前数字导致无解，则回溯
                self.board.remove_digit(row, col)

        # 所有数字都尝试过，无解
        return False

    def get_solution(self) -> Optional[Board]:
        """
        获取求解结果

        Returns:
            返回求解后的棋盘，如果无解则返回None
        """
        self.pbar = tqdm(
            desc="求解进度",
            unit="步",
            bar_format="{desc}: {n}步 - 速率: {rate_fmt} - 已用: {elapsed}",
        )

        if self.solve():
            return self.board.copy()

        return None
