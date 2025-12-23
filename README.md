# Sudoku Solver v0.5.0

一个基于回溯算法的数独求解器，支持多种数独规则和自定义棋盘尺寸。

## 📦 项目概述

SudokuSolver 是一个灵活的数独求解框架，使用回溯算法实现。它支持经典的数独规则，并可以扩展自定义规则，适合数独爱好者、教育研究和个人项目使用。

## ✨ 功能特性

- ✅ **多规则支持**：内置经典数独规则（行、列、宫）和非连续规则
- ✅ **任意尺寸**：支持任意正整数尺寸的棋盘（不仅仅是9×9）
- ✅ **可扩展架构**：通过继承Rule类轻松添加新规则
- ✅ **进度显示**：使用tqdm显示求解进度
- ✅ **错误处理**：完善的异常处理机制
- ✅ **棋盘复制**：支持棋盘的深拷贝操作

## 📁 项目结构

```
SudokuSolver/
└── src/
    ├── sudoku/           # 数独求解器核心包
    │   ├── __init__.py   # 包初始化文件，定义公开接口
    │   ├── exception.py  # 自定义异常处理模块
    │   ├── board.py      # 棋盘管理模块
    │   ├── rules.py      # 规则定义模块
    │   └── solver.py     # 求解器模块
    ├── utils/            # 实用工具目录
    │   ├── __init__.py   # 工具包初始化文件
    │   └── format.py     # 数独棋盘格式化工具
    └── main.py           # 使用示例和主程序
```

## 🔧 安装指南

### 前置要求

- Python 3.6+
- pip（Python包管理器）

### 安装依赖

```bash
# 安装核心依赖
pip install tqdm

# 或者从requirements.txt安装（如果存在）
pip install -r requirements.txt
```

### 设置项目

由于项目使用src布局，可以通过以下方式之一使用：

1. **安装为可编辑包**：
   ```bash
   pip install -e .
   ```

2. **设置PYTHONPATH**：
   ```bash
   # 在Linux/macOS上
   export PYTHONPATH="/path/to/SudokuSolver/src:$PYTHONPATH"
   
   # 在Windows上
   set PYTHONPATH=C:\path\to\SudokuSolver\src;%PYTHONPATH%
   ```

## 🚀 快速开始

### 基本使用示例

```python
from sudoku import Board, Solver
from sudoku import NormalRowRule, NormalColumnRule, Normal9x9BlockRule, NonConsecutiveRule
from utils import separate

# 创建9×9棋盘
board = Board(9)

# 配置初始局面（0表示空格）
clue = "000000700060000000000500400500000007000060000800000001007002000000000040004000000"
clue = separate(clue)  # 转换为空格分隔格式

board.configure(clue)
print("初始局面:")
print(board)

# 创建规则
rules = [
    NormalRowRule(),
    NormalColumnRule(),
    Normal9x9BlockRule(),
    NonConsecutiveRule()
]

# 创建求解器并求解
solver = Solver(board, *rules)
solution = solver.solution()

if solution:
    print(f"求解成功！使用步数：{solver.steps}")
    print("解为:")
    print(solution)
else:
    print("无解")
```

## 📖 详细使用说明

### 1. 棋盘（Board）类

`Board` 类用于管理数独棋盘的状态。

```python
# 创建棋盘
board = Board(9)  # 9×9棋盘
board = Board(6)  # 6×6棋盘（支持任意尺寸）

# 配置初始局面
clue = "1 0 0 0 0 0 0 0 9 0 2 0 ..."  # 空格分隔的字符串
board.configure(clue)

# 操作棋盘
board.set(0, 0, 5)      # 在(0,0)位置放置数字5
digit = board.get(0, 0) # 获取(0,0)位置的数字
board.remove(0, 0)      # 移除(0,0)位置的数字

# 查找空格
empty_pos = board.find()  # 返回第一个空格位置(row, col)，无空格返回None

# 复制棋盘
board_copy = board.copy()
```

### 2. 规则（Rule）类

内置规则：

- **NormalRowRule**：检查每行数字1-n不重复
- **NormalColumnRule**：检查每列数字1-n不重复
- **Normal9x9BlockRule**：检查每个3×3宫数字1-9不重复（仅适用于9×9棋盘）
- **NonConsecutiveRule**：正交相邻单元格不能包含连续数字

#### 创建自定义规则

```python
from sudoku import Rule, Board
from sudoku.exception import SudokuError

class MyCustomRule(Rule):
    """自定义规则示例"""
    
    def test(self, board: Board) -> None:
        """检查棋盘与规则是否适配"""
        # 可在此进行规则适用性检查
        if board.size % 2 != 0:
            raise SudokuError(
                self.rule_name,
                f"规则仅适用于偶数尺寸棋盘，当前尺寸为{board.size}"
            )
    
    def check(self, board: Board) -> bool:
        """检查棋盘是否满足规则"""
        for i in range(board.size):
            for j in range(board.size):
                # 自定义检查逻辑
                pass
        return True
```

### 3. 求解器（Solver）类

```python
# 创建求解器
solver = Solver(board, rule1, rule2, rule3)

# 自动检查规则适配性
try:
    solver.test()  # 检查所有规则与棋盘的兼容性
except SudokuError as e:
    print(f"规则不兼容: {e}")

# 求解数独
solution = solver.solution()  # 返回Board对象或None

# 获取求解统计
print(f"求解步数: {solver.steps}")
```

### 4. 工具函数

```python
from utils import separate

# 格式化clue字符串
compact_clue = "000000700060000000..."
formatted_clue = separate(compact_clue)  # 转换为"0 0 0 0 0 0 7 0 0 ..."
```

## 🔍 示例

### 示例1：经典数独求解

```python
from sudoku import *

# 创建棋盘并配置
board = Board(9)
clue = separate("530070000600195000098000060800060003400803001700020006060000280000419005000080079")
board.configure(clue)

# 使用经典规则
solver = Solver(
    board,
    NormalRowRule(),
    NormalColumnRule(),
    Normal9x9BlockRule()
)

solution = solver.solution()
if solution:
    print("找到解！")
    print(solution)
```

### 示例2：添加非连续规则

```python
from sudoku import *

board = Board(9)
clue = separate("000000700060000000000500400500000007000060000800000001007002000000000040004000000")
board.configure(clue)

# 添加非连续规则
solver = Solver(
    board,
    NormalRowRule(),
    NormalColumnRule(),
    Normal9x9BlockRule(),
    NonConsecutiveRule()  # 额外约束：相邻单元格数字不能连续
)

solution = solver.solution()
```

### 示例3：自定义尺寸数独

```python
from sudoku import *

# 创建4×4数独
board = Board(4)
clue = separate("1 0 0 4 0 2 0 0 0 0 3 0 4 0 0 2")
board.configure(clue)

# 只使用行和列规则（4×4没有宫规则）
solver = Solver(
    board,
    NormalRowRule(),
    NormalColumnRule()
)

solution = solver.solution()
```

## ⚠️ 错误处理

```python
from sudoku import *
from sudoku.exception import SudokuError

try:
    board = Board(6)  # 6×6棋盘
    board.configure(separate("0" * 36))
    
    # 错误：尝试将9×9专用规则用于6×6棋盘
    solver = Solver(board, Normal9x9BlockRule())
    
except SudokuError as e:
    print(f"规则错误: {e}")
except ValueError as e:
    print(f"配置错误: {e}")
```

---

**Happy Sudoku Solving!** 🎯