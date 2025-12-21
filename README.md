# Sudoku Solver v0.4.0

一个基于Python的数独求解器，使用回溯算法实现，支持自定义规则和多种棋盘尺寸。

## 功能特性

- ✅ 支持任意尺寸的数独棋盘（N×N）
- ✅ 使用回溯算法进行高效求解
- ✅ 模块化规则系统，易于扩展
- ✅ 内置三种标准数独规则：
    - 行规则（1-n数字不重复）
    - 列规则（1-n数字不重复）
    - 9×9宫规则（3×3子区域）
- ✅ 实时求解进度显示
- ✅ 详细的错误处理和兼容性检查
- ✅ 简洁易用的API接口

## 安装要求

### 系统要求

- Python 3.7 或更高版本
- pip 包管理器

### 安装步骤

1. 克隆或下载项目：

```bash
git clone <repository-url>
cd SudokuSolver
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

**requirements.txt 内容：**

```
tqdm>=4.65.0
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
    ├── utils/            # 实用工具目录
    │   ├── __init__.py   # 工具包初始化文件
    │   └── format.py     # 数独棋盘格式化工具
    └── main.py           # 使用示例和主程序
```

## 快速开始

### 基本用法

```python
from sudoku import Board, Solver
from sudoku.rules import NormalSudokuRowRule, NormalSudokuColumnRule, Normal9x9SudokuBlockRule
from utils.format import separate

# 1. 创建棋盘
board = Board(9)

# 2. 配置初始局面
clue = ("030007004"
        "602041000"
        "050030967"
        "040003006"
        "087000350"
        "900700020"
        "718020040"
        "000160809"
        "400500030")

clue = separate(clue)  # 格式化字符串
board.configure(clue)

# 3. 创建规则
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()
block_rule = Normal9x9SudokuBlockRule()

# 4. 创建求解器
solver = Solver(board, row_rule, col_rule, block_rule)

# 5. 求解
solution = solver.solution()

if solution:
    print("求解成功！")
    print(f"使用步数：{solver.steps}")
    print(solution)
else:
    print("无解")
```

### 自定义棋盘尺寸

```python
# 创建4×4数独
board = Board(4)
clue = "1 0 3 0 0 2 0 4 3 0 0 1 0 4 0 2"
board.configure(clue)

# 使用行规则和列规则（4×4没有宫规则）
row_rule = NormalSudokuRowRule()
col_rule = NormalSudokuColumnRule()

solver = Solver(board, row_rule, col_rule)
solution = solver.solution()
```

## API 文档

### Board 类

`Board` 类用于管理数独棋盘的状态。

#### 构造函数

```python
Board(size: int)
```

- `size`: 棋盘尺寸（必须是正整数）

#### 主要方法

- `configure(clue: str) -> None`：配置棋盘的初始局面
- `get(row: int, col: int) -> int`：获取指定位置的数字
- `set(row: int, col: int, digit: int) -> None`：在指定位置放置数字
- `remove(row: int, col: int) -> None`：移除指定位置的数字
- `find() -> Optional[tuple[int, int]]`：找到第一个空格
- `copy() -> Board`：创建当前棋盘的深拷贝

### Rule 抽象类

所有数独规则的基类。

#### 内置规则

1. **NormalSudokuRowRule**
    - 检查每一行是否满足数独规则（1-n不重复）
    - 支持任意尺寸

2. **NormalSudokuColumnRule**
    - 检查每一列是否满足数独规则（1-n不重复）
    - 支持任意尺寸

3. **Normal9x9SudokuBlockRule**
    - 检查每一个3×3宫是否满足数独规则
    - 仅适用于9×9棋盘

#### 自定义规则

继承 `Rule` 类并实现 `check()` 方法：

```python
from sudoku.rules import Rule
from sudoku.board import Board


class MyCustomRule(Rule):
    def check(self, board: Board) -> bool:
        # 实现自定义规则检查逻辑
        pass

    def test(self, board: Board) -> None:
        # 可选：检查棋盘与规则的兼容性
        pass
```

### Solver 类

数独求解器，使用回溯算法。

#### 构造函数

```python
Solver(board: Board, *rules: Rule)
```

- `board`: 要求解的数独棋盘
- `*rules`: 要应用的规则列表

#### 主要方法

- `solve() -> bool`：使用回溯算法求解数独
- `solution() -> Optional[Board]`：获取求解结果
- `check() -> bool`：检查当前棋盘是否满足所有规则
- `trial(row: int, col: int, digit: int) -> bool`：尝试在指定位置放置数字

### 工具函数

- `separate(clue: str) -> str`：将无空格分隔的字符串转换为空格分隔格式

## 输入格式

### 棋盘初始化字符串

使用空格分隔的数字字符串表示棋盘状态：

- `0` 表示空格
- 数字范围：0 到棋盘尺寸
- 长度必须等于棋盘格子总数

**示例（9×9）：**

```
"0 3 0 0 0 7 0 0 4 6 0 2 0 4 1 0 0 0 0 5 0 0 3 0 9 6 7 ..."
```

### 便捷格式转换

如果输入是无空格的字符串，可以使用 `separate()` 函数转换：

```python
from utils.format import separate

clue = "030007004602041000..."
formatted_clue = separate(clue)  # 转换为空格分隔格式
```

## 错误处理

### 异常类型

- `SudokuError`: 数独异常基类，用于处理棋盘与规则不兼容的情况

### 常见错误

1. **棋盘尺寸错误**
   ```python
   # 错误的尺寸
   board = Board(-1)  # 抛出 ValueError
   ```

2. **初始化字符串格式错误**
   ```python
   board = Board(9)
   board.configure("1 2 3")  # 长度不足，抛出 ValueError
   ```

3. **规则兼容性错误**
   ```python
   board = Board(4)  # 4×4棋盘
   block_rule = Normal9x9SudokuBlockRule()
   solver = Solver(board, block_rule)  # 抛出 SudokuError
   ```

## 性能特性

- 使用优化的回溯算法
- 实时进度显示（使用 tqdm 进度条）
- 步数统计
- 内存高效的棋盘复制

## 示例输出

运行 `main.py` 的示例输出：

```
初始局面:
. 3 . . . 7 . . 4
6 . 2 . 4 1 . . .
. 5 . . 3 . 9 6 7
. 4 . . . 3 . . 6
. 8 7 . . . 3 5 .
9 . . 7 . . . 2 .
7 1 8 . 2 . . 4 .
. . . 1 6 . 8 . 9
4 . . 5 . . . 3 .

开始求解...
求解进度: 1000步 - 速率: 1000步/s - 已用: 00:01

求解成功！使用步数：1000

解为:
1 3 5 6 9 7 2 8 4
6 7 2 8 4 1 5 9 3
8 5 4 2 3 9 1 6 7
2 4 9 1 5 3 7 6 8
5 8 7 4 2 6 3 1 9
9 6 3 7 8 5 4 2 1
7 1 8 3 2 9 6 4 5
3 2 6 1 7 4 8 5 9
4 9 1 5 6 8 7 3 2
```

**提示**：本项目仍在积极开发中，API 可能在未来版本中发生变化。