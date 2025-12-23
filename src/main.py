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

    clue = ("000000700"
            "060000000"
            "000500400"
            "500000007"
            "000060000"
            "800000001"
            "007002000"
            "000000040"
            "004000000")

    clue = separate(clue)

    print("\n初始局面:")
    board.configure(clue)
    print(board)

    # 创建规则
    rule1 = NormalRowRule()
    rule2 = NormalColumnRule()
    rule3 = Normal9x9BlockRule()
    rule4 = NonConsecutiveRule()

    # 创建求解器
    solver = Solver(board, rule1, rule2, rule3, rule4)
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
