# board.py
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
            size: 棋盘尺寸（必须指定），必须是1-9的正整数

        Raises:
            ValueError: 如果size不是1-9的正整数
        """

        if size <= 0:
            raise ValueError(f"棋盘尺寸必须为正整数，当前尺寸为{size}")

        if size > 9:
            raise ValueError(f"当前版本棋盘尺寸不能超过9，当前尺寸为{size}")

        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def __str__(self):
        """可视化棋盘状态"""
        result = []
        for i in range(self.size):
            row_str = []
            for j in range(self.size):
                digit = self.grid[i][j]
                row_str.append(str(digit) if digit != 0 else ".")
            result.append(" ".join(row_str))

        return "\n".join(result)

    def configure(self, clue: str) -> None:
        """
        配置棋盘的初始局面

        Args:
            clue: 表示初始局面的字符串，使用0表示空格，只能包含0-9的数字字符

        Raises:
            ValueError: 如果clue长度不等于棋盘格子总数，或包含无效字符
        """
        expected_length = self.size * self.size

        if len(clue) != expected_length:
            raise ValueError(
                f"clue长度必须为{expected_length} (当前: {len(clue)})"
            )

        # 将字符串转换为二维列表
        for i in range(self.size):
            for j in range(self.size):
                char = clue[i * self.size + j]

                # 验证字符是否为数字字符
                if not char.isdigit():
                    raise ValueError(
                        f"clue包含非法字符: '{char}' (位置 {i * self.size + j})"
                    )

                digit = int(char)

                # 验证数字是否在有效范围内
                if digit < 0 or digit > self.size:
                    raise ValueError(
                        f"数字{digit}超出有效范围(0-{self.size}) (位置 {i},{j})"
                    )

                self.grid[i][j] = digit

    def get(self, row: int, col: int) -> int:
        """
        获取指定位置的数字

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）

        Returns:
            指定位置的数字
        """
        return self.grid[row][col]

    def set(self, row: int, col: int, digit: int) -> None:
        """
        在指定位置放置数字

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）
            digit: 要放置的数字
        """
        self.grid[row][col] = digit

    def remove(self, row: int, col: int) -> None:
        """
        移除指定位置的数字（设置为0）

        Args:
            row: 行索引（0-based）
            col: 列索引（0-based）
        """
        self.grid[row][col] = 0

    def find(self) -> Optional[tuple[int, int]]:
        """
        找到棋盘上的第一个空格

        Returns:
            返回(row, col)元组，如果找不到空格则返回None
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
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
            new_board.grid[i] = self.grid[i].copy()
        return new_board
