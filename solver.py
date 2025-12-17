"""
数独求解器模块，实现回溯算法求解数独。
"""

from typing import List, Optional
from board import Board
from rules import Rule
from exception import SudokuError

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
        self.original_board = board
        self.board = board.copy()  # 使用副本进行求解
        self.rules = rules

        # 验证棋盘与规则的兼容性
        for rule in self.rules:
            rule.test(self.board)

    def _is_valid(self, row: int, col: int, digit: int) -> bool:
        """
        检查在指定位置放置指定数字是否有效

        Args:
            row: 行索引
            col: 列索引
            digit: 要放置的数字

        Returns:
            如果放置有效返回True，否则返回False
        """
        # 临时放置数字
        original_digit = self.board.grid[row][col]
        self.board.grid[row][col] = digit

        # 检查所有规则
        is_valid = all(rule.check(self.board) for rule in self.rules)

        # 恢复原始状态
        self.board.grid[row][col] = original_digit

        return is_valid

    def solve(self) -> bool:
        """
        使用回溯算法求解数独

        Returns:
            如果找到解返回True，否则返回False
        """
        # 找到第一个空格
        empty_pos = self.board.find_empty()

        # 如果没有空格，说明数独已解
        if not empty_pos:
            return True

        row, col = empty_pos

        # 尝试所有可能的数字
        for digit in range(1, self.board.size + 1):
            if self._is_valid(row, col, digit):
                # 放置数字
                self.board.place(row, col, digit)

                # 递归求解
                if self.solve():
                    return True

                # 如果当前数字导致无解，则回溯
                self.board.remove(row, col)

        # 所有数字都尝试过，无解
        return False

    def solution(self) -> Optional[Board]:
        """
        获取求解结果

        Returns:
            返回求解后的棋盘，如果无解则返回None
        """
        if self.solve():
            return self.board.copy()
        return None

    def reset(self) -> None:
        """重置求解器状态"""
        self.board = self.original_board.copy()