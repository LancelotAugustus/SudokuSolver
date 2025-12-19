# Sudoku Solver v0.3.0

一个基于回溯算法的数独求解器库，提供灵活的棋盘管理、规则定义和高效求解功能。

## 功能特性

- 🧩 支持任意尺寸的标准数独棋盘
- 🔧 模块化规则系统，支持自定义规则
- 🔍 高效回溯算法求解
- 🎯 完整的错误处理和验证机制
- 📊 步数计数和求解过程追踪

## 安装

### 方法一：直接使用源码
1. 克隆或下载项目到本地
2. 确保Python 3.7或更高版本已安装
3. 将`sudoku`目录添加到您的Python路径中

### 方法二：作为包安装
```bash
# 在项目根目录执行
pip install -e .
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

## 快速开始

### 基本用法

```python
from sudoku import Board, Solver, NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule

# 创建9×9数独棋盘
board = Board(9)

# 设置初始局面（0表示空格）
clue = ("0 3 0 0 0 7 0 0 4 "
        "6 0 2 0 4 1 0 0 0 "
        "0 5 0 0 3 0 9 6 7 "
        "0 4 0 0 0 3 0 0 6 "
        "0 8 7 0 0 0 3 5 0 "
        "9 0 0 7 0 0 0 2 0 "
        "7 1 8 0 2 0 0 4 0 "
        "0 0 0 1 6 0 8 0 9 "
        "4 0 0 5 0 0 0 3 0")

board.configure(clue)

# 创建规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 创建求解器并求解
solver = Solver(board, row_rule, col_rule, block_rule)
solution = solver.solution()

if solution:
    print("求解成功！")
    print(f"使用步数：{solver.steps}")
    print(solution)
else:
    print("无解")
```

### 运行示例

```bash
# 从项目根目录运行
python src/main.py
```

## API 文档

### Board 类

数独棋盘管理类，负责棋盘状态的管理和操作。

#### 构造函数
```python
Board(size: int)
```
- `size`: 棋盘尺寸（必须是正整数）

#### 主要方法
- `configure(clue: str)`: 配置棋盘的初始局面
- `get(row: int, col: int) -> int`: 获取指定位置的数字
- `set(row: int, col: int, digit: int)`: 在指定位置放置数字
- `remove(row: int, col: int)`: 移除指定位置的数字
- `find() -> Optional[tuple[int, int]]`: 找到第一个空格
- `copy() -> Board`: 创建当前棋盘的深拷贝
- `__str__()`: 返回棋盘的字符串表示

### Rule 类

数独规则抽象基类，所有具体规则必须继承此类。

#### 内置规则
- `NormalSudokuRowRule`: 标准数独行规则
- `NormalSudokuColumnRule`: 标准数独列规则
- `Normal9x9SudokuBlockRule`: 9×9数独宫规则（仅适用于9×9棋盘）

#### 自定义规则
```python
from sudoku import Rule, Board

class CustomRule(Rule):
    def check(self, board: Board) -> bool:
        """检查棋盘是否满足自定义规则"""
        # 实现你的规则检查逻辑
        pass
    
    def test(self, board: Board) -> None:
        """检查棋盘与规则是否适配"""
        # 实现棋盘兼容性检查
        pass
```

### Solver 类

数独求解器，使用回溯算法求解数独。

#### 构造函数
```python
Solver(board: Board, *rules: Rule)
```
- `board`: 要求解的数独棋盘
- `*rules`: 要应用的规则列表

#### 主要方法
- `check() -> bool`: 检查当前棋盘是否满足所有规则
- `trial(row: int, col: int, digit: int) -> bool`: 尝试在指定位置放置数字
- `solve() -> bool`: 使用回溯算法求解数独
- `solution() -> Optional[Board]`: 获取求解结果

## 高级用法

### 创建自定义尺寸的数独

```python
# 创建6×6数独
board = Board(6)
clue = "1 0 0 0 0 2 " \
       "0 2 0 0 3 0 " \
       "0 0 3 4 0 0 " \
       "0 0 4 3 0 0 " \
       "0 4 0 0 2 0 " \
       "5 0 0 0 0 1"
board.configure(clue)

# 对于非9×9数独，只需使用行规则和列规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()

solver = Solver(board, row_rule, col_rule)
solution = solver.solution()
```

### 添加多个规则

```python
from sudoku import Board, Solver, Rule

# 定义多个规则
rules = [
    NormalSudokuRowRule(),
    NormalSudokuColumnRule(),
    Normal9x9SudokuBlockRule(),
    # 可以添加更多自定义规则
]

board = Board(9)
# ... 配置棋盘

solver = Solver(board, *rules)
```