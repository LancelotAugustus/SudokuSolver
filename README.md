# Sudoku Solver

## 项目简介

Sudoku Solver 是一个基于回溯算法的数独求解器，采用模块化设计，支持可扩展的规则系统和任意尺寸的数独棋盘（1-9阶）。该项目提供了清晰的API接口和良好的错误处理机制，适合学习回溯算法、模块化设计以及数独规则验证。

## 快速开始

### 安装与使用

1. **克隆项目**：
```bash
git clone https://github.com/LancelotAugustus/SudokuSolver.git
cd SudokuSolver
```

2. **运行示例**：
```bash
python src/main.py
```

### 基本使用示例

```python
from sudoku import Board, Solver, NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule

# 创建9×9数独棋盘
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

# 创建规则实例
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 创建求解器并求解
solver = Solver(board, row_rule, col_rule, block_rule)
solution = solver.solution()

if solution:
    print(f"求解成功！使用步数：{solver.steps}")
    print(solution)
```

## 项目结构

```
SudokuSolver/
└── src/
    ├── sudoku/           # 数独求解器核心包
    │   ├── __init__.py   # 包初始化文件，定义公开接口
    │   ├── exception.py  # 自定义异常处理模块
    │   ├── board.py      # 棋盘管理模块
    │   ├── rules.py      # 规则定义模块
    │   └── solver.py     # 求解器模块
    └── main.py           # 使用示例和主程序
```

## 主要功能

### 1. 棋盘管理 (Board类)
- 支持1-9阶任意尺寸数独棋盘
- 提供棋盘的初始化、配置、获取和设置方法
- 支持棋盘状态的可视化输出
- 包含空格查找和棋盘深拷贝功能

### 2. 规则系统 (Rule类)
- **抽象规则基类**：定义了规则的通用接口
- **具体规则实现**：
  - `NormalSudokuRowRule`：行规则（1-n不重复）
  - `NormalSudokuColumnRule`：列规则（1-n不重复）
  - `Normal9x9SudokuBlockRule`：9×9宫规则（1-9不重复）
- **规则兼容性验证**：自动检查棋盘与规则的适配性

### 3. 求解器 (Solver类)
- **回溯算法**：使用经典的递归回溯算法求解数独
- **规则验证**：在每一步尝试后验证所有规则
- **步数统计**：记录求解过程中尝试的次数
- **错误恢复**：自动回溯到之前的状态

### 4. 错误处理
- **自定义异常**：`SudokuError`用于处理规则兼容性问题
- **输入验证**：对棋盘尺寸、初始局面字符串进行严格验证
- **规则测试**：在求解前检查规则与棋盘的兼容性

### 5. 扩展性
- 支持自定义规则（继承`Rule`基类）
- 支持任意尺寸的数独棋盘（1-9阶）
- 模块化设计，便于功能扩展和维护