# Sudoku Solver v0.3.1

一个基于回溯算法的数独求解器，采用模块化设计，支持自定义规则和任意尺寸数独。

## 项目概述

这是一个用Python实现的数独求解器，采用面向对象的设计思想，将棋盘管理、规则定义和求解算法分离，提供了高度可扩展的架构。

### 主要特性

- 🎯 **灵活的架构**：支持任意尺寸的数独棋盘
- 🔧 **规则系统**：可扩展的规则定义，支持自定义约束条件
- ⚡ **高效求解**：基于回溯算法，快速求解数独谜题
- 🧩 **模块化设计**：各组件职责明确，易于维护和扩展
- 🛡️ **完善的错误处理**：提供详细的错误信息和兼容性检查

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
    ├── utils/            # 实用工具目录
    │   ├── __init__.py   # 工具包初始化文件
    │   └── format.py     # 数独棋盘格式化工具
    └── main.py           # 使用示例和主程序
```

## 安装与使用

### 环境要求

- Python 3.7+

### 基本用法

```python
from sudoku import Board, Solver
from sudoku.rules import NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule
from utils.format import separate

# 创建9×9数独棋盘
board = Board(9)

# 设置初始局面（可以使用separate工具格式化字符串）
clue = "030007004602041000050030967040003006087000350900700020718020040000160809400500030"
clue = separate(clue)

board.configure(clue)

# 创建规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 创建求解器
solver = Solver(board, row_rule, col_rule, block_rule)

# 求解数独
solution = solver.solution()

if solution:
    print("求解成功！")
    print(f"使用步数：{solver.steps}")
    print(solution)
else:
    print("无解")
```

## 核心模块说明

### 1. Board（棋盘管理）

`Board` 类负责管理数独棋盘的状态，提供以下功能：

- **初始化**：支持任意正整数尺寸的棋盘
- **配置**：通过字符串配置初始局面
- **操作**：获取、设置、移除数字
- **查找**：找到第一个空格位置
- **复制**：创建棋盘的深拷贝

### 2. Rule（规则系统）

规则系统采用抽象基类设计，支持扩展：

#### 内置规则：

- `NormalSudokuRowRule`：标准数独行规则（1-n不重复）
- `NormalSudokuColumnRule`：标准数独列规则（1-n不重复）
- `Normal9x9SudokuBlockRule`：标准9×9数独宫规则

#### 自定义规则：

继承 `Rule` 抽象基类，实现 `check()` 和可选的 `test()` 方法：

```python
from sudoku.rules import Rule
from sudoku.board import Board


class CustomRule(Rule):
    def check(self, board: Board) -> bool:
        """检查是否满足自定义规则"""
        # 实现检查逻辑
        pass

    def test(self, board: Board) -> None:
        """检查棋盘与规则的兼容性"""
        # 实现兼容性检查
        pass
```

### 3. Solver（求解器）

`Solver` 类实现了回溯算法：

- **初始化**：接受棋盘和规则列表
- **兼容性检查**：验证棋盘与规则的兼容性
- **求解**：使用深度优先搜索回溯算法
- **状态跟踪**：记录求解步数

### 4. 异常处理

`SudokuError` 异常用于处理规则与棋盘不兼容的情况，提供详细的错误信息。

### 5. 工具函数

`separate()` 函数：将无空格分隔的数独字符串转换为空格分隔格式。

## API参考

### Board类

```python
class Board:
    def __init__(self, size: int)

        def configure(self, clue: str) -> None

        def get(self, row: int, col: int) -> int

        def set(self, row: int, col: int, digit: int) -> None

        def remove(self, row: int, col: int) -> None

        def find(self) -> Optional[tuple[int, int]]

        def copy(self) -> 'Board'
```

### Rule抽象基类

```python
class Rule(ABC):
    @abstractmethod
    def check(self, board: Board) -> bool

        def test(self, board: Board) -> None
```

### Solver类

```python
class Solver:
    def __init__(self, board: Board, *rules: Rule)

        def test(self) -> None

        def check(self) -> bool

        def trial(self, row: int, col: int, digit: int) -> bool

        def solve(self) -> bool

        def solution(self) -> Optional[Board]
```

## 示例

### 示例1：标准9×9数独求解

```python
from sudoku import Board, Solver
from sudoku.rules import NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule

# 创建棋盘并配置
board = Board(9)
board.configure("""
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
""".strip())

# 创建求解器并求解
solver = Solver(
    board,
    NormalSudokuRowRule(),
    NormalSudokuColumnRule(),
    Normal9x9SudokuBlockRule()
)

solution = solver.solution()
if solution:
    print("找到解！")
    print(solution)
```

### 示例2：自定义尺寸数独（仅行列规则）

```python
# 创建4×4数独棋盘
board = Board(4)
board.configure("""
1 0 3 4
3 4 1 0
0 1 4 3
4 3 0 1
""".strip())

# 仅使用行列规则
solver = Solver(
    board,
    NormalSudokuRowRule(),
    NormalSudokuColumnRule()
)

solution = solver.solution()
```

## 错误处理

程序会检查以下错误情况：

1. **棋盘尺寸无效**：尺寸必须为正整数
2. **配置字符串无效**：长度不匹配或包含非法字符
3. **数字超出范围**：数字必须在0到棋盘尺寸之间
4. **规则兼容性**：规则与棋盘尺寸不匹配（如9宫规则用于非9×9棋盘）
