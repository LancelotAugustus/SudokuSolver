"""
数独棋盘模块，定义Board类用于管理棋盘状态。
"""

from typing import List, Optional

class Board:
    """数独棋盘类"""

    def __init__(self, size: int = 9):
        """
        初始化数独棋盘

        Args:
            size: 棋盘尺寸，默认为9（9×9数独）
        """
        if size <= 0:
            raise ValueError("棋盘尺寸必须大于0")

        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def set(self, clue: str) -> None:
        """
        设置棋盘的初始局面

        Args:
            clue: 表示初始局面的字符串，使用0表示空格

        Raises:
            ValueError: 如果clue长度不等于棋盘格子总数
        """
        expected_length = self.size * self.size

        if len(clue) != expected_length:
            raise ValueError(
                f"clue长度必须为{expected_length} (当前: {len(clue)})"
            )

        # 将字符串转换为二维列表
        for i in range(self.size):
            for j in range(self.size):
                digit = int(clue[i * self.size + j])
                if digit < 0 or digit > self.size:
                    raise ValueError(f"数字{digit}超出有效范围(0-{self.size})")
                self.grid[i][j] = digit

    def place(self, row: int, col: int, digit: int) -> None:
        """
        在指定位置放置数字

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）
            digit: 要放置的数字

        Raises:
            IndexError: 如果行或列索引超出范围
            ValueError: 如果数字超出有效范围
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError(f"位置({row}, {col})超出棋盘范围(0-{self.size-1})")

        if not (0 <= digit <= self.size):
            raise ValueError(f"数字{digit}超出有效范围(0-{self.size})")

        self.grid[row][col] = digit

    def remove(self, row: int, col: int) -> None:
        """
        移除指定位置的数字（设置为0）

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）

        Raises:
            IndexError: 如果行或列索引超出范围
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError(f"位置({row}, {col})超出棋盘范围(0-{self.size-1})")

        self.grid[row][col] = 0

    def find_empty(self) -> Optional[tuple]:
        """
        找到棋盘上的第一个空格

        Returns:
            返回(row, col)元组，如果找不到空格则返回None
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def copy(self) -> 'Board':
        """
        创建当前棋盘的深拷贝

        Returns:
            返回一个新的Board实例
        """
        new_board = Board(self.size)
        for i in range(self.size):
            new_board.grid[i] = self.grid[i].copy()
        return new_board

    def __str__(self) -> str:
        """可视化棋盘状态"""
        result = []
        horizontal_line = "+".join(["-" * (self.size // 3)] * 3)

        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                result.append(horizontal_line)

            row_str = []
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    row_str.append("|")
                digit = self.grid[i][j]
                row_str.append(str(digit) if digit != 0 else ".")

            result.append(" ".join(row_str))

        return "\n".join(result)

    def __repr__(self) -> str:
        return f"Board(size={self.size})"