# Sudoku-Solver v0.7.2 版本更新日志

## 新增特性
- 新增`KillerRule`杀手数独规则类，支持笼子内数字和约束及不重复规则
- 扩展公开接口，在`__init__.py`中导出新增的`KillerRule`类
- 扩展规则系统，支持更复杂的杀手数独变体求解

## 功能优化
- 更新示例程序，展示如何使用杀手数独规则求解复杂谜题

---

# Sudoku-Solver v0.7.1 版本更新日志

## 问题修复
- 修复代码格式问题，调整注释位置和内容以符合PEP8规范
- 移除重复的空行和多余注释，提升代码整洁度
- 修复示例中puzzle_str变量的重复赋值问题，清理测试代码

---

# Sudoku-Solver v0.7.0 版本更新日志

## 功能优化

- 重构核心模块命名，提升代码一致性和可读性：
    - 规则类命名简化（`NormalRowRule`→`RowRule`，`NormalColumnRule`→`ColumnRule`）
    - 方法命名规范化（`check`→`is_valid`，`test`→`validate_compatibility`，`trial`→`try_set_digit`）
    - 棋盘属性标准化（`grid`→`cells`，`find`→`find_empty_cell`）
- 统一术语使用（`clue`→`puzzle`，`solution`→`get_solution`）
- 重构工具模块结构，将`format.py`重命名为`parser.py`，明确其解析器功能定位
- 优化温度计规则配置方式，使用循环结构简化示例代码
- 修复模块导入路径，确保`exceptions.py`（原`exception.py`）能被正确引用
- 修正方法调用链，确保重构后的方法命名在模块间保持一致

---

# Sudoku-Solver v0.6.1 版本更新日志

## 新增特性

- 新增温度计坐标解析函数`parse_compact_thermometer()`和`parse_spaced_thermometer()`，提供更直观的温度计规则配置方式

## 功能优化

- 改进温度计规则示例代码，使用字母-数字坐标表示法（如"C1B1A1"）代替原始坐标元组，提高可读性和易用性

---

# Sudoku-Solver v0.6.0 版本更新日志

## 新增特性

- 新增`ThermometerRule`温度计规则类，支持数字沿温度计严格递增的特殊约束
- 新增`parse_compact_clue()`和`parse_spaced_clue()`函数，提供更灵活的棋盘初始化方式

## 功能优化

- `Board.configure()`方法现直接接受整数列表，简化输入验证逻辑
- 优化模块导入结构，使用`from .rules import *`提升代码可读性
- 扩展工具模块功能，支持紧凑格式和空格分隔格式的clue解析

## 问题修复

- 移除棋盘尺寸必须≤9的限制，支持任意尺寸的数独求解
- 删除字符串格式验证的冗余代码，提高配置效率

---

# Sudoku-Solver v0.5.0 版本更新日志

## 新增特性

- 新增`NonConsecutiveRule`规则类，支持正交相邻单元格不能包含连续数字的特殊数独规则

## 功能优化

- 简化规则类命名（如`NormalSudokuRowRule`→`NormalRowRule`），提升代码简洁性
- 更新示例程序，展示如何使用新增的非连续数独规则求解复杂数独

---

# Sudoku-Solver v0.4.0 版本更新日志

## 新增特性

- 引入`tqdm`进度条库，为求解过程添加可视化进度指示
- 新增`requirements.txt`依赖管理文件，明确项目运行环境要求
- 求解器现在会实时显示求解步数、计算速率和已用时间

---

# Sudoku-Solver v0.3.1 版本更新日志

## 功能优化

- 重构`Solver`类的初始化逻辑，将规则兼容性测试提取为独立的`test()`方法
- 新增`utils`工具模块，提供`separate()`格式化函数，支持向后兼容的clue字符串处理
- 改进项目代码结构，分离核心逻辑与辅助功能

---

# Sudoku-Solver v0.3.0 版本更新日志

## 新增特性

- 支持任意尺寸的数独棋盘，取消9×9的尺寸限制
- 改进初始局面配置方式，改为使用空格分隔的数字字符串格式

## 功能优化

- `Board.configure()`方法现支持两位数及以上的数字表示
- 增强棋盘配置的灵活性和可读性

---

# Sudoku-Solver v0.2.0 版本更新日志

## 功能优化

- 重构项目结构为Python包格式，将所有核心模块移至`sudoku`包内
- 添加`__init__.py`文件定义包公开接口，简化导入语句
- 改进模块间的相对导入方式，增强代码的可维护性

---

# Sudoku-Solver v0.1.0 版本更新日志

## 新增特性

- 实现数独求解器核心模块，包含棋盘管理、规则定义和回溯算法求解
- 添加自定义异常处理机制，支持棋盘与规则的兼容性检查
- 提供9×9标准数独的完整求解能力，支持行、列、宫规则验证

---