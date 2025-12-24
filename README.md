# Sudoku Solver v0.7.0

一个基于回溯算法的数独求解器，支持多种数独变体规则。

## 📋 功能特性

- **多种数独变体支持**
    - 标准9×9数独（行、列、宫规则）
    - 非连续数独（相邻单元格不能包含连续数字）
    - 温度计数独（温度计单元格必须递增）
    - 支持任意尺寸的数独棋盘

- **灵活的规则系统**
    - 模块化规则设计，易于扩展新规则
    - 自动规则兼容性检查
    - 规则组合使用

- **智能求解器**
    - 基于回溯算法实现
    - 实时求解进度显示
    - 详细的求解统计信息

## 🏗️ 项目结构

```
SudokuSolver/
└── src/
    ├── sudoku/            # 数独求解器核心包
    │   ├── __init__.py    # 包初始化文件，定义公开接口
    │   ├── exceptions.py  # 自定义异常处理模块
    │   ├── board.py       # 棋盘管理模块
    │   ├── rules.py       # 规则定义模块
    │   └── solver.py      # 求解器模块
    ├── utils/             # 实用工具目录
    │   ├── __init__.py    # 工具包初始化文件
    │   └── parser.py      # 数独棋盘格式化工具
    └── main.py            # 使用示例和主程序
```

## 🔧 安装与运行

### 环境要求

- Python 3.7+
- tqdm 库（用于显示进度条）

### 安装依赖

```bash
pip install tqdm
```

### 运行示例

```bash
# 从项目根目录运行
python src/main.py
```

## 📖 使用指南

### 基本使用

#### 1. 创建棋盘

```python
from sudoku import Board

# 创建9×9数独棋盘
board = Board(9)
```

#### 2. 加载数独谜题

```python
from utils import parse_compact_puzzle

# 使用紧凑格式字符串（0表示空格）
puzzle_str = "852914637000000000000000000000000000000000000000000000000000000000000000000000000"
puzzle_data = parse_compact_puzzle(puzzle_str)
board.load_puzzle(puzzle_data)
```

#### 3. 定义规则

```python
from sudoku import RowRule, ColumnRule, Normal9x9BlockRule, NonConsecutiveRule, ThermometerRule

# 标准数独规则
row_rule = RowRule()
col_rule = ColumnRule()
block_rule = Normal9x9BlockRule()

# 非连续规则
non_consecutive_rule = NonConsecutiveRule()

# 温度计规则
thermometer_rule = ThermometerRule()

# 设置温度计坐标
thermometer_strings = [
    "C1B1A1",  # 从C1到A1的温度计
    "C2B2A2",  # 从C2到A2的温度计
    # ... 更多温度计
]
for therm_str in thermometer_strings:
    thermometer_rule.set(parse_compact_thermometer(therm_str))
```

#### 4. 求解数独

```python
from sudoku import Solver

# 创建求解器（传入棋盘和所有规则）
solver = Solver(board, row_rule, col_rule, block_rule, non_consecutive_rule, thermometer_rule)

# 求解并获取结果
solution = solver.get_solution()

if solution:
    print(f"求解成功！使用步数：{solver.steps}")
    print(solution)
else:
    print("无解")
```

### 输入格式说明

#### 棋盘格式

支持两种输入格式：

1. **紧凑格式**（无空格）
   ```
   "030007004602000000..."
   ```
   使用 `parse_compact_puzzle()` 解析

2. **分隔格式**（空格分隔）
   ```
   "0 3 0 0 0 7 0 0 4 6 0 2 ..."
   ```
   使用 `parse_spaced_puzzle()` 解析

#### 温度计格式

支持两种坐标格式：

1. **紧凑坐标格式**
   ```
   "A1B1C1"  # 表示三个单元格：(0,0), (1,0), (2,0)
   ```
   使用 `parse_compact_thermometer()` 解析

2. **分隔坐标格式**
   ```
   "A1 B1 C1"  # 空格分隔的坐标
   ```
   使用 `parse_spaced_thermometer()` 解析

### 棋盘坐标系统

- 行：使用字母 A-I 表示（对应0-8）
- 列：使用数字 1-9 表示（对应0-8）
- 示例：A1 = (0,0), B2 = (1,1), I9 = (8,8)

## 📊 支持的规则

### 内置规则

| 规则类                  | 描述            | 适用范围 |
|----------------------|---------------|------|
| `RowRule`            | 每行数字1-n不重复    | 任意尺寸 |
| `ColumnRule`         | 每列数字1-n不重复    | 任意尺寸 |
| `Normal9x9BlockRule` | 3×3宫内数字1-9不重复 | 仅9×9 |
| `NonConsecutiveRule` | 相邻单元格数字不能连续   | 任意尺寸 |
| `ThermometerRule`    | 温度计上数字必须递增    | 任意尺寸 |

### 创建自定义规则

继承 `Rule` 基类并实现以下方法：

```python
from sudoku import Rule, Board


class CustomRule(Rule):
    def is_valid(self, board: Board) -> bool:
        """检查棋盘是否满足此规则"""
        # 实现规则检查逻辑
        pass

    def validate_compatibility(self, board: Board) -> None:
        """检查棋盘是否与此规则兼容"""
        # 可选：实现兼容性检查
        pass
```

## 🐛 错误处理

程序使用自定义异常 `SudokuError` 处理错误：

```python
from sudoku import SudokuError

try:
    # 创建求解器
    solver = Solver(board, row_rule, col_rule, block_rule)
except SudokuError as e:
    print(f"规则兼容性错误: {e.message}")
```

常见错误：

- 规则与棋盘尺寸不兼容
- 温度计坐标超出棋盘范围
- 规则冲突

## 📈 性能说明

- 使用回溯算法，适合大多数标准数独谜题
- 对于复杂变体数独，求解时间可能较长
- 实时显示求解进度和步数统计
- 建议用于求解步数在百万级别以下的谜题

## 📝 示例程序

项目包含完整的示例程序 `src/main.py`，演示了如何：

1. 创建和初始化棋盘
2. 设置多种规则组合
3. 求解复杂变体数独
4. 处理求解结果

## 🚀 未来计划

- [ ] 添加更多数独变体规则（杀手数独、箭头数独等）
- [ ] 实现更高效的求解算法
- [ ] 添加图形用户界面
- [ ] 支持导入/导出多种数独格式
- [ ] 添加谜题生成功能
