# Sudoku Solver 术语表 (v0.6.1)

## 核心术语

| 术语 | 描述 |
|------|------|
| **cell** | 棋盘上的单个格子 |
| **cells** | 棋盘上所有格子的二维列表 |
| **digit** | 填入单元格的数字 |
| **puzzle** | 数独的初始局面 |
| **row** | 棋盘的行（0-based索引） |
| **col** | 棋盘的列（0-based索引） |
| **size** | 棋盘的尺寸 |
| **rule** | 数独规则 |
| **board** | 数独棋盘对象 |

## 方法术语

| 术语 | 描述 |
|------|------|
| **load_puzzle** | 加载棋盘的初始局面 |
| **get_digit** | 获取指定位置的数字 |
| **set_digit** | 在指定位置放置数字 |
| **remove_digit** | 移除指定位置的数字 |
| **find_empty_cell** | 查找第一个空格 |
| **copy** | 创建对象副本 |
| **is_valid** | 检查是否满足规则 |
| **validate_compatibility** | 检查兼容性 |
| **try_set_digit** | 尝试在指定位置放置数字 |
| **solve** | 使用回溯算法求解数独 |
| **get_solution** | 获取求解结果 |
| **set** | 添加温度计或设置规则 |

## 解析相关术语

| 术语 | 描述 |
|------|------|
| **parse_compact_puzzle** | 解析紧凑型棋盘字符串 |
| **parse_spaced_puzzle** | 解析空格分隔棋盘字符串 |
| **parse_compact_thermometer** | 解析紧凑型温度计字符串 |
| **parse_spaced_thermometer** | 解析空格分隔温度计字符串 |

## 规则相关术语

| 术语 | 描述 |
|------|------|
| **RowRule** | 行规则 |
| **ColumnRule** | 列规则 |
| **Normal9x9BlockRule** | 9×9宫规则 |
| **NonConsecutiveRule** | 非连续规则 |
| **ThermometerRule** | 温度计规则 |
| **thermometer** | 温度计坐标列表 |

## 变量和属性术语

| 术语 | 描述 |
|------|------|
| **steps** | 求解步数 |
| **pbar** | 进度条 |
| **rule_name** | 规则名称 |
| **thermometers** | 温度计列表 |

## 其他术语

| 术语 | 描述 |
|------|------|
| **empty_cell** | 空格，未填入数字的单元格 |
| **compatibility** | 兼容性 |
| **solution** | 解决方案 |
| **recursion** | 递归 |
| **backtracking** | 回溯算法 |
| **progress_bar** | 进度条 |

- **单元格**：统一使用 `cell` 和 `cells`
- **数字**：统一使用 `digit`
- **棋盘初始情形**：统一使用 `puzzle`
- **放置操作**：统一使用 `set` 相关术语
- **检查操作**：统一使用 `is_valid` 和 `validate` 相关术语