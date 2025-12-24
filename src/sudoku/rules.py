# src/sudoku/rules.py
"""
数独规则模块，定义抽象规则类和具体规则实现。
"""

from abc import ABC, abstractmethod
from .exception import SudokuError
from .board import Board


class Rule(ABC):
    """数独规则抽象基类"""

    def __init__(self):
        """初始化规则，规则名称自动设置为类名"""
        self.rule_name = self.__class__.__name__

    def __str__(self):
        """返回规则名称"""
        return self.rule_name

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

    def test(self, board: Board) -> None:
        """
        检查棋盘与规则是否适配（默认实现不进行任何检查）

        Args:
            board: 要检查的棋盘
        """
        pass


class NormalRowRule(Rule):
    """数独行规则（支持任意尺寸）"""

    def check(self, board: Board) -> bool:
        """
        检查每一行是否满足数独规则（1-n不重复）

        Args:
            board: 要检查的棋盘

        Returns:
            如果所有行都满足规则返回True，否则返回False
        """
        for row in range(board.size):
            seen = set()
            for col in range(board.size):
                digit = board.get(row, col)
                if digit != 0:
                    if digit in seen:
                        return False
                    seen.add(digit)
        return True


class NormalColumnRule(Rule):
    """数独列规则（支持任意尺寸）"""

    def check(self, board: Board) -> bool:
        """
        检查每一列是否满足数独规则（1-n不重复）

        Args:
            board: 要检查的棋盘

        Returns:
            如果所有列都满足规则返回True，否则返回False
        """
        for col in range(board.size):
            seen = set()
            for row in range(board.size):
                digit = board.get(row, col)
                if digit != 0:
                    if digit in seen:
                        return False
                    seen.add(digit)
        return True


class Normal9x9BlockRule(Rule):
    """9×9数独宫规则"""

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
                        digit = board.get(row, col)
                        if digit != 0:
                            if digit in seen:
                                return False
                            seen.add(digit)
        return True


class NonConsecutiveRule(Rule):
    """非连续规则：正交相邻的单元格不能包含连续的数字"""

    def check(self, board: Board) -> bool:
        """
        检查棋盘是否满足非连续规则

        Args:
            board: 要检查的棋盘

        Returns:
            如果满足规则返回True，否则返回False
        """
        size = board.size

        for i in range(size):
            for j in range(size):
                current_digit = board.get(i, j)

                # 只检查非空单元格
                if current_digit == 0:
                    continue

                # 检查上方相邻单元格
                if i > 0:
                    up_digit = board.get(i - 1, j)
                    if up_digit != 0 and abs(current_digit - up_digit) == 1:
                        return False

                # 检查下方相邻单元格
                if i < size - 1:
                    down_digit = board.get(i + 1, j)
                    if down_digit != 0 and abs(current_digit - down_digit) == 1:
                        return False

                # 检查左方相邻单元格
                if j > 0:
                    left_digit = board.get(i, j - 1)
                    if left_digit != 0 and abs(current_digit - left_digit) == 1:
                        return False

                # 检查右方相邻单元格
                if j < size - 1:
                    right_digit = board.get(i, j + 1)
                    if right_digit != 0 and abs(current_digit - right_digit) == 1:
                        return False

        return True


class ThermometerRule(Rule):
    """温度计规则：沿着每个温度计的数字必须从灯泡端开始递增"""

    def __init__(self):
        """初始化温度计规则"""
        super().__init__()
        self.thermometers = []

    def set(self, thermometer:list[tuple[int, int]]) -> None:
        """
        添加一个温度计

        Args:
            thermometer: 一个温度计的坐标列表，例如[(0,0), (0,1), (1,1)]
        """
        self.thermometers.append(thermometer)

    def test(self, board: Board) -> None:
        """
        检查温度计坐标是否在棋盘范围内

        Args:
            board: 要检查的棋盘

        Raises:
            SudokuError: 如果温度计坐标超出棋盘范围
        """
        size = board.size

        for i, thermometer in enumerate(self.thermometers):
            for row, col in thermometer:
                if row < 0 or row >= size or col < 0 or col >= size:
                    raise SudokuError(
                        self.rule_name,
                        f"温度计{i}坐标({row},{col})超出棋盘范围(0-{size - 1})"
                    )

    def check(self, board: Board) -> bool:
        """
        检查棋盘是否满足温度计规则

        Args:
            board: 要检查的棋盘

        Returns:
            如果满足规则返回True，否则返回False
        """
        for thermometer in self.thermometers:
            # 提取温度计上的数字（过滤掉0）
            digits = []
            for row, col in thermometer:
                digit = board.get(row, col)
                if digit != 0:
                    digits.append(digit)

            # 检查数字是否严格递增
            for i in range(1, len(digits)):
                if digits[i] <= digits[i - 1]:
                    return False

        return True
