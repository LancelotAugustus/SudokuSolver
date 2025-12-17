"""
数独求解器模块，实现回溯算法求解数独。
"""

from typing import Optional
from board import Board
from rules import Rule

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

        # 验证棋盘与规则的兼容性
        for rule in self.rules:
            rule.test(self.board)

    def check(self) -> bool:
        """
        检查当前棋盘是否满足所有规则

        Returns:
            如果满足所有规则返回True，否则返回False
        """
        for rule in self.rules:
            if not rule.check(self.board):
                return False
        return True

    def trial(self, row: int, col: int, digit: int) -> bool:
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

        # 记录原始数字
        original_digit = self.board.get(row, col)

        # 放置数字
        self.board.set(row, col, digit)

        # 检查是否满足所有规则
        is_valid = self.check()

        # 如果不满足规则，则恢复原始状态
        if not is_valid:
            self.board.set(row, col, original_digit)

        return is_valid

    def solve(self) -> bool:
        """
        使用回溯算法求解数独

        Returns:
            如果找到解返回True，否则返回False
        """
        # 找到第一个空格
        empty_pos = self.board.find()

        # 如果没有空格，检查棋盘是否完全满足规则
        if not empty_pos:
            return self.check()

        row, col = empty_pos

        # 尝试所有可能的数字
        for digit in range(1, self.board.size + 1):
            if self.trial(row, col, digit):
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