# src/utils/format.py
"""
数独棋盘格式化工具模块
"""


def separate(clue: str) -> str:
    """
    将无空格分隔的clue字符串转换为空格分隔格式

    Args:
        clue: 无空格分隔的clue字符串，如"030007004..."

    Returns:
        空格分隔的clue字符串，如"0 3 0 0 0 7 0 0 4 ..."
    """
    return " ".join(clue).strip()
