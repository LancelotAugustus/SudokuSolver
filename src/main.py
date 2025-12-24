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

    rule5.set([(2, 0), (1, 0), (0, 0)])
    rule5.set([(2, 1), (1, 1), (0, 1)])
    rule5.set([(1, 7), (0, 7), (0, 8), (1, 8)])
    rule5.set([(2, 8), (3, 8), (4, 8), (5, 8)])
    rule5.set([(3, 3), (4, 3), (5, 3)])
    rule5.set([(3, 4), (4, 4), (5, 4)])
    rule5.set([(4, 6), (3, 6), (3, 7), (4, 7)])
    rule5.set([(8, 7), (7, 7), (6, 7)])
    rule5.set([(8, 8), (7, 8), (6, 8)])
    rule5.set([(8, 2), (8, 1), (8, 0)])
    rule5.set([(7, 3), (7, 2), (7, 1)])
    rule5.set([(6, 2), (6, 1), (6, 0)])
    rule5.set([(6, 2), (6, 3), (6, 4), (6, 5)])
    rule5.set([(7, 3), (7, 4), (7, 5), (7, 6)])

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
