# Sudoku Solver

## 项目简介
这是一个模块化的数独求解器，采用回溯算法实现，支持自定义数独规则。

## 安装要求
- Python 3.6 或更高版本
- 无额外依赖库

## 快速开始

### 基本用法

```python
from board import Board
from rules import NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule
from solver import Solver

# 1. 创建9×9数独棋盘
board = Board(9)

# 2. 配置初始局面（0表示空格）
clue = "030007004602041000050030967040003006087000350900700020718020040000160809400500030"
board.configure(clue)

print("初始局面:")
print(board)

# 3. 创建规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 4. 创建求解器
solver = Solver(board, row_rule, col_rule, block_rule)

# 5. 求解数独
solution = solver.solution()

if solution:
    print(f"\n求解成功！使用步数：{solver.steps}")
    print("\n解为:")
    print(solution)
else:
    print("无解")
```

### 使用其他尺寸的数独

```python
from board import Board
from rules import NormalSudokuRowRule, NormalSudokuColumnRule
from solver import Solver

# 创建4×4数独（仅使用行规则和列规则）
board = Board(4)
board.configure("0030204001000000")

row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()

solver = Solver(board, row_rule, col_rule)
```

## 项目结构
- `board.py` - 棋盘管理类
- `rules.py` - 规则抽象类和具体规则实现
- `solver.py` - 回溯算法求解器
- `exception.py` - 自定义异常类
- `main.py` - 使用示例

## 主要功能

### 1. 棋盘管理 (Board类)
- 创建任意尺寸的数独棋盘（1-9）
- 通过字符串配置初始局面
- 获取、设置和移除数字
- 查找空格位置
- 创建棋盘副本

### 2. 规则系统 (Rule类)
**内置规则：**
- `NormalSudokuRowRule` - 行规则（任意尺寸）
- `NormalSudokuColumnRule` - 列规则（任意尺寸）
- `Normal9x9SudokuBlockRule` - 9×9宫规则

**自定义规则：**
继承`Rule`类并实现`check()`方法。

### 3. 求解器 (Solver类)
- 回溯算法求解
- 支持多规则组合
- 自动验证规则兼容性
- 记录求解步数

## 注意事项
1. 棋盘尺寸最大支持9×9
2. 9×9宫规则仅适用于9×9数独
3. 初始局面字符串长度必须等于棋盘格子总数
4. 数字0表示空格，有效数字范围为1到棋盘尺寸

## 运行示例
运行项目中的`main.py`文件查看完整示例：
```bash
python main.py
```

---
