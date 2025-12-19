# file: main.py
"""
数独求解器使用示例
"""

from sudoku import *


def main():
    # 创建一个9×9数独棋盘
    board = Board(9)

    # 设置初始局面
    clue = ("0 3 0 0 0 7 0 0 4 "
            "6 0 2 0 4 1 0 0 0 "
            "0 5 0 0 3 0 9 6 7 "
            "0 4 0 0 0 3 0 0 6 "
            "0 8 7 0 0 0 3 5 0 "
            "9 0 0 7 0 0 0 2 0 "
            "7 1 8 0 2 0 0 4 0 "
            "0 0 0 1 6 0 8 0 9 "
            "4 0 0 5 0 0 0 3 0")

    print("\n初始局面:")
    board.configure(clue)
    print(board)

    # 创建规则
    row_rule = NormalSudokuRowRule()
    col_rule = NormalSudokuColumnRule()
    block_rule = Normal9x9SudokuBlockRule()

    # 创建求解器
    solver = Solver(board, row_rule, col_rule, block_rule)
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
