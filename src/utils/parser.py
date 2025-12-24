# src/utils/parser.py
"""
数独棋盘解析器模块
"""


def parse_compact_puzzle(puzzle_str: str) -> list[int]:
    """
    将无空格分隔的紧凑字符串转换为整数列表

    Args:
        puzzle_str: 无空格分隔的puzzle字符串，如"030007004..."

    Returns:
        整数列表，每个元素对应一个数字
    """
    return [int(char) for char in puzzle_str]


def parse_spaced_puzzle(puzzle_str: str) -> list[int]:
    """
    将有空格分隔的字符串转换为整数列表

    Args:
        puzzle_str: 有空格分隔的puzzle字符串，如"0 3 0 0 0 7 0 0 4 6 0 2 ..."

    Returns:
        整数列表，每个元素对应一个数字
    """
    return [int(token) for token in puzzle_str.split() if token]


def parse_compact_thermometer(thermometer_str: str) -> list[tuple[int, int]]:
    """
    将无空格分隔的温度计字符串转换为坐标列表

    Args:
        thermometer_str: 无空格分隔的温度计字符串，形如"A1B1B2"

    Returns:
        坐标列表，格式为[(row1, col1), (row2, col2), ...]
    """
    coordinates = []

    for i in range(0, len(thermometer_str), 2):
        row_char = thermometer_str[i]
        col_char = thermometer_str[i + 1]
        row = ord(row_char) - ord('A')
        col = int(col_char) - 1
        coordinates.append((row, col))

    return coordinates


def parse_spaced_thermometer(thermometer_str: str) -> list[tuple[int, int]]:
    """
    将有空格分隔的温度计字符串转换为坐标列表

    Args:
        thermometer_str: 有空格分隔的温度计字符串，形如"B7 B8 B9 B10"

    Returns:
        坐标列表，格式为[(row1, col1), (row2, col2), ...]
    """
    coordinates = []
    tokens = thermometer_str.split()

    for token in tokens:
        row_char = token[0]
        col_str = token[1:]
        row = ord(row_char) - ord('A')
        col = int(col_str) - 1
        coordinates.append((row, col))

    return coordinates
