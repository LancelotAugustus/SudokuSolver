# src/main.py
"""
数独求解器使用示例
"""

from sudoku import *
from utils import *


def main():
    # 创建一个9×9数独棋盘
    board = Board(9)

    # 设置初始局面
    clue = (""
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "")

    clue = ("852914637"
            "000000000"
            "000000000"
            "000000000"
            "000000000"
            "000000000"
            "000000000"
            "000000000"
            "000000000")

    clue = parse_compact_clue(clue)

    print("\n初始局面:")
    board.configure(clue)
    print(board)

    # 创建规则
    rule1 = NormalRowRule()
    rule2 = NormalColumnRule()
    rule3 = Normal9x9BlockRule()
    rule4 = NonConsecutiveRule()
    rule5 = ThermometerRule()

    thermometer_strings = [
        "C1B1A1",
        "C2B2A2",
        "B8A8A9B9",
        "C9D9E9F9",
        "D4E4F4",
        "D5E5F5",
        "E7D7D8E8",
        "I8H8G8",
        "I9H9G9",
        "I3I2I1",
        "H4H3H2",
        "G3G2G1",
        "G3G4G5G6",
        "H4H5H6H7"
    ]

    for therm_str in thermometer_strings:
        rule5.set(parse_compact_thermometer(therm_str))

    # 创建求解器
    solver = Solver(board, rule1, rule2, rule3, rule4, rule5)
    print("\n开始求解...")

    # 求解数独
    solution = solver.solution()

    if solution:
        print(f"\n求解成功！使用步数：{solver.steps}")
        print("\n解为:")
        print(solution)
    else:
        print("\n无解")


if __name__ == "__main__":
    main()
