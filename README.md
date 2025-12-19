# Sudoku Solver v0.1.0

## 项目简介

Sudoku Solver 是一个基于 Python 的数独求解器，采用回溯算法实现。项目支持自定义数独规则，目前包含标准的行、列和宫格规则。该求解器能够处理不同尺寸的数独问题（目前支持1-9阶数独），并提供清晰的模块化架构。

## 快速开始

## 运行示例
运行项目中的`main.py`文件查看完整示例：
```bash
python main.py
```

### 基本使用
```python
from board import Board
from rules import NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule
from solver import Solver

# 创建9×9棋盘
board = Board(9)

# 配置初始局面（0表示空格）
clue = ("030007004"
        "602041000"
        "050030967"
        "040003006"
        "087000350"
        "900700020"
        "718020040"
        "000160809"
        "400500030")
board.configure(clue)

# 创建规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 创建求解器并求解
solver = Solver(board, row_rule, col_rule, block_rule)
solution = solver.solution()

if solution:
    print("找到解:")
    print(solution)
    print(f"求解步数: {solver.steps}")
else:
    print("无解")
```

## 项目结构

```
sudoku-solver/
├── board.py           # 棋盘类，管理数独棋盘状态
├── rules.py           # 规则模块，定义数独约束规则
├── solver.py          # 求解器模块，实现回溯算法
├── exception.py       # 自定义异常处理
└── main.py            # 使用示例和主程序
```

## 主要功能

### 1. 棋盘管理 (board.py)
- **Board类**: 提供数独棋盘的基础数据结构
- **配置功能**: 支持通过字符串配置初始局面
- **操作接口**: 提供设置、获取、移除数字的方法
- **状态查询**: 查找空格、复制棋盘、可视化输出

### 2. 规则系统 (rules.py)
- **Rule抽象基类**: 定义规则接口规范
- **行规则 (NormalSudokuRowRule)**: 确保每行数字不重复
- **列规则 (NormalSudokuColumnRule)**: 确保每列数字不重复
- **宫规则 (Normal9x9SudokuBlockRule)**: 确保9×9数独的3×3宫内数字不重复
- **兼容性检查**: 验证棋盘与规则的适配性

### 3. 求解引擎 (solver.py)
- **回溯算法**: 使用深度优先搜索和剪枝策略
- **试错机制**: 支持尝试放置数字并验证
- **步数统计**: 记录求解过程中的尝试次数
- **多规则支持**: 可同时应用多个约束规则

### 4. 异常处理 (exception.py)
- **SudokuError**: 自定义异常类，处理棋盘与规则不兼容的情况
- **错误信息**: 提供详细的规则名称和错误描述