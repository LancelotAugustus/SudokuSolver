"""
数独求解器使用示例
"""

from board import Board
from rules import *
from solver import Solver

def main():
    """主函数示例"""
    print("=" * 50)
    print("数独求解器示例")
    print("=" * 50)

    # 创建一个9×9数独棋盘
    board = Board(9)

    # 设置初始局面
    clue = ("530070000"
            "600195000"
            "098000060"
            "800060003"
            "400803001"
            "700020006"
            "060000280"
            "000419005"
            "000080079")

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