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

    clue = ("300001008"
            "090005040"
            "000070000"
            "240000000"
            "008352100"
            "000000095"
            "000060000"
            "070500060"
            "500400001")
    clue = separate(clue)

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
