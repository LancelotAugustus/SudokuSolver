# src/main.py
"""
数独求解器使用示例
"""

from sudoku import *
from utils import *


def main():
    board = Board(9)
    puzzle_str = (""
                  ""
                  ""
                  ""
                  ""
                  ""
                  ""
                  ""
                  "")

    puzzle_str = ("852914637"
                  "000000000"
                  "000000000"
                  "000000000"
                  "000000000"
                  "000000000"
                  "000000000"
                  "000000000"
                  "000000000")
    puzzle_data = parse_compact_puzzle(puzzle_str)

    print("\n初始局面:")
    board.load_puzzle(puzzle_data)
    print(board)

    row_rule = RowRule()
    col_rule = ColumnRule()
    block_rule = Normal9x9BlockRule()
    non_consecutive_rule = NonConsecutiveRule()
    thermometer_rule = ThermometerRule()

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
        thermometer_rule.set(parse_compact_thermometer(therm_str))

    solver = Solver(board, row_rule, col_rule, block_rule, non_consecutive_rule, thermometer_rule)
    print("\n开始求解...")

    solution = solver.get_solution()

    if solution:
        print(f"\n求解成功！使用步数：{solver.steps}")
        print("\n解为:")
        print(solution)
    else:
        print("\n无解")


if __name__ == "__main__":
    main()
