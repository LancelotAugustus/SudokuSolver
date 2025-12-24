# src/main.py
"""
数独求解器使用示例
"""

from sudoku import *
from utils import *


def main():
    board = Board(9)
    puzzle_str = ("000102070"
                  "034090100"
                  "009000508"
                  "020070340"
                  "800309026"
                  "070050090"
                  "008007010"
                  "340015087"
                  "000000000")

    # puzzle_str = ("000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000"
    #               "000000000")
    puzzle_data = parse_compact_puzzle(puzzle_str)

    print("\n初始局面:")
    board.load_puzzle(puzzle_data)
    print(board)

    row_rule = RowRule()
    col_rule = ColumnRule()
    block_rule = Normal9x9BlockRule()
    non_consecutive_rule = NonConsecutiveRule()
    thermometer_rule = ThermometerRule()
    killer_rule = KillerRule()
    killer_rule.set(30, [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 0)])
    killer_rule.set(6, [(0, 2), (0, 3)])
    killer_rule.set(3, [(0, 4)])
    killer_rule.set(6, [(0, 5), (0, 6)])
    killer_rule.set(16, [(0, 7), (0, 8)])
    killer_rule.set(20, [(1, 3), (1, 4), (2, 4)])
    killer_rule.set(18, [(1, 5), (1, 6), (2, 5), (2, 6)])
    killer_rule.set(9, [(1, 7), (2, 7)])
    killer_rule.set(10, [(1, 8), (2, 8)])
    killer_rule.set(10, [(2, 1), (2, 2)])
    killer_rule.set(15, [(2, 3), (3, 3)])
    killer_rule.set(30, [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1)])
    killer_rule.set(23, [(3, 4), (4, 3), (4, 4), (4, 5)])
    killer_rule.set(4, [(3, 5), (3, 6)])
    killer_rule.set(9, [(3, 7), (3, 8)])
    killer_rule.set(4, [(4, 2), (5, 2)])
    killer_rule.set(15, [(4, 6), (4, 7), (4, 8)])
    killer_rule.set(4, [(5, 0)])
    killer_rule.set(21, [(5, 1), (6, 1), (6, 2)])
    killer_rule.set(7, [(5, 3), (5, 4)])
    killer_rule.set(21, [(5, 5), (5, 6), (6, 5)])
    killer_rule.set(13, [(5, 7), (5, 8), (6, 8)])
    killer_rule.set(8, [(6, 0), (7, 0)])
    killer_rule.set(13, [(6, 3), (7, 3)])
    killer_rule.set(3, [(6, 4), (7, 4)])
    killer_rule.set(10, [(6, 6), (6, 7)])
    killer_rule.set(6, [(7, 1), (7, 2)])
    killer_rule.set(11, [(7, 5), (7, 6)])
    killer_rule.set(13, [(7, 7), (8, 7)])
    killer_rule.set(11, [(7, 8), (8, 8)])
    killer_rule.set(10, [(8, 0), (8, 1)])
    killer_rule.set(21, [(8, 2), (8, 3), (8, 4)])
    killer_rule.set(5, [(8, 5), (8, 6)])

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

    # solver = Solver(board, row_rule, col_rule, block_rule, non_consecutive_rule, thermometer_rule)
    solver = Solver(board, row_rule, col_rule, block_rule, killer_rule)
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
