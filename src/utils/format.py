# src/utils/format.py
"""
数独棋盘格式化工具模块
"""

def parse_compact_clue(clue_str: str) -> list[int]:
    """
    将无空格分隔的紧凑字符串转换为整数列表

    Args:
        clue_str: 无空格分隔的clue字符串，如"030007004..."

    Returns:
        整数列表，每个元素对应一个数字
    """
    return [int(char) for char in clue_str]


def parse_spaced_clue(clue_str: str) -> list[int]:
    """
    将有空格分隔的字符串转换为整数列表

    Args:
        clue_str: 有空格分隔的clue字符串，如"0 3 0 0 0 7 0 0 4 6 0 2 ..."

    Returns:
        整数列表，每个元素对应一个数字
    """
    # 按空格分割，过滤空字符串，然后转换为整数
    return [int(token) for token in clue_str.split() if token]
