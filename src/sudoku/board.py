# src/sudoku/board.py
"""
数独棋盘模块，定义Board类用于管理棋盘状态。
"""

from typing import Optional


class Board:
    """数独棋盘类"""

    def __init__(self, size: int):
        """
        初始化数独棋盘

        Args:
            size: 棋盘尺寸（必须指定），必须是正整数
        """
        self.size = size
        self.cells = [[0 for _ in range(size)] for _ in range(size)]

    def __str__(self):
        """可视化棋盘状态"""
        result = []
        for i in range(self.size):
            row_str = []
            for j in range(self.size):
                digit = self.cells[i][j]
                row_str.append(str(digit) if digit != 0 else ".")
            result.append(" ".join(row_str))
        return "\n".join(result)

    def load_puzzle(self, puzzle_data: list[int]) -> None:
        """
        加载棋盘的初始局面

        Args:
            puzzle_data: 表示初始局面的整数列表，使用0表示空格
        """
        # 将整数列表转换为二维列表
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j] = puzzle_data[i * self.size + j]

    def get_digit(self, row: int, col: int) -> int:
        """
        获取指定位置的数字

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）

        Returns:
            指定位置的数字
        """
        return self.cells[row][col]

    def set_digit(self, row: int, col: int, digit: int) -> None:
        """
        在指定位置放置数字

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）
            digit: 要放置的数字
        """
        self.cells[row][col] = digit

    def remove_digit(self, row: int, col: int) -> None:
        """
        移除指定位置的数字（设置为0）

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）
        """
        self.cells[row][col] = 0

    def find_empty_cell(self) -> Optional[tuple[int, int]]:
        """
        找到棋盘上的第一个空格

        Returns:
            返回(row, col)元组，如果找不到空格则返回None
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    return i, j
        return None

    def copy(self) -> 'Board':
        """
        创建当前棋盘的深拷贝

        Returns:
            返回一个新的Board实例
        """
        new_board = Board(self.size)
        for i in range(self.size):
            new_board.cells[i] = self.cells[i].copy()
        return new_board
