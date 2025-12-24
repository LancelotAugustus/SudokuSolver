# Sudoku Solver (v0.7.0)

## 项目整体结构

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
    │   └── parser.py      # 数独棋盘解析工具
    └── main.py            # 使用示例和主程序
```

## 模块详细说明

### 1. 异常处理模块 (exceptions.py)

**功能**：自定义异常处理模块，处理数独求解过程中的异常情况
**核心组件**：`SudokuError` 异常类

**特点**：

- 继承自Python标准异常类`Exception`
- 专门用于处理数独棋盘与规则的兼容性问题
- 构造函数接收规则名称和可选的错误信息，自动生成格式化的错误消息
- 提供 `rule_name` 属性获取引发异常的规则名称
- 错误信息格式为："错误信息 (规则: 规则名称)"

### 2. 棋盘数据管理模块 (board.py)

**功能**：棋盘数据管理模块，定义Board类用于管理棋盘状态
**核心组件**：`Board` 类

**属性**：

- `size`: 棋盘尺寸（n×n），必须是正整数
- `cells`: 二维整数列表，存储棋盘数字状态，0表示空格

**方法**：

- `__init__(size)`: 初始化数独棋盘，创建指定尺寸的空棋盘
- `__str__()`: 返回棋盘的可视化字符串表示，用"."表示空格，用空格分隔每个数字
- `load_puzzle(puzzle_data)`: 根据整数列表配置初始棋盘状态，列表长度必须等于棋盘格子总数
- `get_digit(row, col)`: 获取指定位置的数字
- `set_digit(row, col, digit)`: 在指定位置放置数字
- `remove_digit(row, col)`: 移除指定位置的数字（设置为0）
- `find_empty_cell()`: 查找第一个空格位置，返回`Optional[tuple[int, int]]`
- `copy()`: 创建棋盘的深拷贝，返回类型使用字符串字面量`'Board'`

### 3. 数独规则定义模块 (rules.py)

**功能**：数独规则定义模块，定义抽象规则类和具体规则实现
**核心组件**：

- `Rule` 抽象基类
- `RowRule` 类（行规则）
- `ColumnRule` 类（列规则）
- `Normal9x9BlockRule` 类（9×9宫规则）
- `NonConsecutiveRule` 类（非连续规则）
- `ThermometerRule` 类（温度计规则）

**Rule抽象基类**：

- 提供`__init__()`方法，自动设置`rule_name`为类名
- 提供`__str__()`方法，返回规则名称
- 提供`is_valid(board)`抽象方法，检查规则满足情况
- 提供`validate_compatibility(board)`默认方法，不进行任何检查（子类可重写）

**具体规则类**：

1. **行规则** (`RowRule`)：
    - 检查每行数字1-n不重复（n为棋盘尺寸）
    - 支持任意尺寸棋盘
    - 使用`board.get_digit(row, col)`获取数字
    - 使用基类默认`validate_compatibility()`方法

2. **列规则** (`ColumnRule`)：
    - 检查每列数字1-n不重复（n为棋盘尺寸）
    - 支持任意尺寸棋盘
    - 使用`board.get_digit(row, col)`获取数字
    - 使用基类默认`validate_compatibility()`方法

3. **宫规则** (`Normal9x9BlockRule`)：
    - 检查每个3×3宫内数字1-9不重复
    - **仅适用于9×9棋盘**
    - 重写`validate_compatibility()`方法，检查棋盘尺寸是否为9，不符合时抛出`SudokuError`
    - 实现`is_valid()`方法，检查9个3×3宫的规则满足情况

4. **非连续规则** (`NonConsecutiveRule`)：
    - 检查正交相邻的单元格不能包含连续的数字
    - 支持任意尺寸棋盘
    - 使用基类默认`validate_compatibility()`方法
    - 实现`is_valid()`方法，检查上下左右四个方向的相邻单元格
    - 只检查非空单元格（值为0的单元格跳过）
    - 使用`abs(current_digit - neighbor_digit) == 1`判断是否连续

5. **温度计规则** (`ThermometerRule`)：
    - 检查沿着每个温度计的数字必须从灯泡端开始严格递增
    - 支持任意尺寸棋盘
    - 提供`set(thermometer)`方法添加温度计坐标
    - 重写`validate_compatibility()`方法，检查温度计坐标是否在棋盘范围内，超出范围时抛出`SudokuError`
    - 实现`is_valid()`方法，检查每个温度计上的数字是否严格递增

### 4. 求解器核心模块 (solver.py)

**功能**：数独求解器模块，实现回溯算法求解数独
**核心组件**：`Solver` 类

**属性**：

- `board`: 棋盘副本（用于求解操作，不修改原始棋盘）
- `rules`: 规则元组（保存所有应用的规则）
- `steps`: 求解步数计数器（包括尝试和回溯操作）
- `pbar`: tqdm进度条实例（用于显示求解进度）

**方法**：

- `__init__(board, *rules)`: 初始化求解器，复制棋盘，调用`validate_compatibility()`验证所有规则兼容性，初始化步数计数器
- `validate_compatibility()`: 调用所有规则实例的validate_compatibility方法验证棋盘与规则的兼容性
- `is_valid()`: 检查当前棋盘是否满足所有规则，遍历所有规则调用`rule.is_valid(board)`
- `try_set_digit(row, col, digit)`: 尝试在指定位置放置数字，记录原始数字，放置新数字，验证规则，如果不满足则恢复原始状态。每次尝试都会增加步数计数并更新进度条
- `solve()`: 递归回溯求解算法，查找空格，尝试所有可能的数字（1到board.size），递归调用自身求解剩余棋盘
- `get_solution()`: 获取求解结果，初始化tqdm进度条，调用`solve()`方法，如果成功返回棋盘的深拷贝，否则返回None。进度条会自动显示求解步数、速率和耗时

### 5. 解析器工具模块 (utils/parser.py)

**功能**：数独棋盘和温度计坐标解析工具模块
**核心组件**：四个解析函数

**函数说明**：

1. `parse_compact_puzzle(puzzle_str)`:
    - 参数：`puzzle_str` - 无空格分隔的puzzle字符串，如"030007004..."
    - 返回值：整数列表，每个元素对应一个数字
    - 用途：将紧凑格式的字符串转换为整数列表

2. `parse_spaced_puzzle(puzzle_str)`:
    - 参数：`puzzle_str` - 有空格分隔的puzzle字符串，如"0 3 0 0 0 7 0 0 4 6 0 2 ..."
    - 返回值：整数列表，每个元素对应一个数字
    - 用途：将分隔格式的字符串转换为整数列表

3. `parse_compact_thermometer(thermometer_str)`:
    - 参数：`thermometer_str` - 无空格分隔的温度计字符串，形如"A1B1B2"
    - 返回值：坐标列表，格式为[(row1, col1), (row2, col2), ...]
    - 用途：将紧凑格式的温度计字符串转换为坐标列表

4. `parse_spaced_thermometer(thermometer_str)`:
    - 参数：`thermometer_str` - 有空格分隔的温度计字符串，形如"B7 B8 B9 B10"
    - 返回值：坐标列表，格式为[(row1, col1), (row2, col2), ...]
    - 用途：将分隔格式的温度计字符串转换为坐标列表

### 6. 应用程序入口 (main.py)

**功能**：数独求解器使用示例和主程序

**使用流程**：

1. 创建9×9数独棋盘实例
2. 使用`parse_compact_puzzle`函数解析无空格的初始局面字符串
3. 使用`board.load_puzzle`设置数独初始局面
4. 创建五种规则实例（行规则、列规则、宫规则、非连续规则、温度计规则）
5. 使用`parse_compact_thermometer`解析温度计字符串并添加到温度计规则
6. 初始化求解器并求解
7. 显示初始局面、求解步数和最终解

## 代码执行流程

### 初始化阶段

1. 创建`Board`实例，指定尺寸为9
2. 使用`parse_compact_puzzle()`函数解析无空格的puzzle字符串
3. 调用`board.load_puzzle(puzzle_data)`加载初始局面
4. 创建五个规则实例（行规则、列规则、宫规则、非连续规则、温度计规则）
5. 对每个温度计字符串使用`parse_compact_thermometer()`解析，并调用`thermometer_rule.set()`添加温度计
6. 创建`Solver`实例，传入棋盘和所有规则，自动调用`validate_compatibility()`验证所有规则兼容性

### 求解阶段

1. 调用`solver.get_solution()`
2. 创建tqdm进度条实例，显示求解进度
3. 调用内部`solve()`方法开始递归求解：
    - 调用`board.find_empty_cell()`查找第一个空格
    - 如果没有空格，调用`is_valid()`验证棋盘是否完全满足所有规则
    - 如果有空格，获取位置(row, col)
    - 循环尝试数字1到board.size（即9）
    - 对每个数字调用`try_set_digit(row, col, digit)`方法：
        - 增加步数计数
        - 更新进度条
        - 记录原始数字
        - 放置新数字
        - 调用`is_valid()`验证所有规则
        - 如果验证失败，恢复原始数字
        - 返回验证结果
    - 如果`try_set_digit()`成功，递归调用`solve()`处理下一个空格
    - 如果递归成功，返回True
    - 如果递归失败或所有数字尝试失败，调用`board.remove_digit(row, col)`回溯
    - 返回False表示当前分支无解
4. 如果`solve()`返回True，返回棋盘的深拷贝，否则返回None

### 结果展示阶段

1. 打印初始棋盘状态（使用"."表示空格）
2. 显示求解成功状态和使用的步数
3. 打印最终解（如果存在）
