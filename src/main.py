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
    killer_strings = [
        "30:A1A2B1B2B3C1",
        "6:A3A4",
        "3:A5",
        "6:A6A7",
        "16:A8A9",
        "20:B4B5C5",
        "18:B6B7C6C7",
        "9:B8C8",
        "10:B9C9",
        "10:C2C3",
        "15:C4D4",
        "30:D1D2D3E1E2",
        "23:D5E4E5E6",
        "4:D6D7",
        "9:D8D9",
        "4:E3F3",
        "15:E7E8E9",
        "4:F1",
        "21:F2G2G3",
        "7:F4F5",
        "21:F6F7G6",
        "13:F8F9G9",
        "8:G1H1",
        "13:G4H4",
        "3:G5H5",
        "10:G7G8",
        "6:H2H3",
        "11:H6H7",
        "13:H8I8",
        "11:H9I9",
        "10:I1I2",
        "21:I3I4I5",
        "5:I6I7"
    ]

    for killer_str in killer_strings:
        sum_value, coords_str = killer_str.split(':')
        killer_rule.set(int(sum_value), parse_compact_coordinates(coords_str))

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
        thermometer_rule.set(parse_compact_coordinates(therm_str))

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
