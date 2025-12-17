"""
数独规则模块，定义抽象规则类和具体规则实现。
"""

from abc import ABC, abstractmethod
from typing import List
from exception import SudokuError
from board import Board

class Rule(ABC):
    """数独规则抽象基类"""

    def __init__(self, rule_name: str):
        """
        初始化规则

        Args:
            rule_name: 规则名称
        """
        self.rule_name = rule_name

    @abstractmethod
    def check(self, board: Board) -> bool:
        """
        检查棋盘是否满足当前规则

        Args:
            board: 要检查的棋盘

        Returns:
            如果满足规则返回True，否则返回False
        """
        pass

    @abstractmethod
    def test(self, board: Board) -> None:
        """
        检查棋盘与规则是否适配

        Args:
            board: 要检查的棋盘

        Raises:
            SudokuError: 如果棋盘与规则不兼容
        """
        pass

    def __str__(self) -> str:
        """返回规则名称"""
        return self.rule_name


class Normal9x9SudokuRowRule(Rule):
    """9×9数独行规则"""

    def __init__(self):
        super().__init__("9×9数独行规则")

    def test(self, board: Board) -> None:
        """
        检查棋盘是否为9×9

        Args:
            board: 要检查的棋盘

        Raises:
            SudokuError: 如果棋盘不是9×9
        """
        if board.size != 9:
            raise SudokuError(
                self.rule_name,
                f"规则仅适用于9×9数独，当前棋盘尺寸为{board.size}×{board.size}"
            )

    def check(self, board: Board) -> bool:
        """
        检查每一行是否满足数独规则（1-9不重复）

        Args:
            board: 要检查的棋盘

        Returns:
            如果所有行都满足规则返回True，否则返回False
        """
        for row in range(9):
            seen = set()
            for col in range(9):
                digit = board.grid[row][col]
                if digit != 0:
                    if digit in seen:
                        return False
                    seen.add(digit)
        return True


class Normal9x9SudokuColumnRule(Rule):
    """9×9数独列规则"""

    def __init__(self):
        super().__init__("9×9数独列规则")

    def test(self, board: Board) -> None:
        """
        检查棋盘是否为9×9

        Args:
            board: 要检查的棋盘

        Raises:
            SudokuError: 如果棋盘不是9×9
        """
        if board.size != 9:
            raise SudokuError(
                self.rule_name,
                f"规则仅适用于9×9数独，当前棋盘尺寸为{board.size}×{board.size}"
            )

    def check(self, board: Board) -> bool:
        """
        检查每一列是否满足数独规则（1-9不重复）

        Args:
            board: 要检查的棋盘

        Returns:
            如果所有列都满足规则返回True，否则返回False
        """
        for col in range(9):
            seen = set()
            for row in range(9):
                digit = board.grid[row][col]
                if digit != 0:
                    if digit in seen:
                        return False
                    seen.add(digit)
        return True


class Normal9x9SudokuBlockRule(Rule):
    """9×9数独宫规则"""

    def __init__(self):
        super().__init__("9×9数独宫规则")

    def test(self, board: Board) -> None:
        """
        检查棋盘是否为9×9

        Args:
            board: 要检查的棋盘

        Raises:
            SudokuError: 如果棋盘不是9×9
        """
        if board.size != 9:
            raise SudokuError(
                self.rule_name,
                f"规则仅适用于9×9数独，当前棋盘尺寸为{board.size}×{board.size}"
            )

    def check(self, board: Board) -> bool:
        """
        检查每一个3×3宫是否满足数独规则（1-9不重复）

        Args:
            board: 要检查的棋盘

        Returns:
            如果所有宫都满足规则返回True，否则返回False
        """
        for block_row in range(3):
            for block_col in range(3):
                seen = set()
                # 检查每个3×3宫
                for i in range(3):
                    for j in range(3):
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        digit = board.grid[row][col]
                        if digit != 0:
                            if digit in seen:
                                return False
                            seen.add(digit)
        return True