# file: exception.py
"""
自定义异常模块，用于处理数独求解过程中的异常情况。
"""


class SudokuError(Exception):
    """数独异常基类，用于处理棋盘与规则不兼容的情况"""

    def __init__(self, rule_name: str, message: str = "棋盘与规则存在兼容性问题"):
        """
        初始化SudokuError异常

        Args:
            rule_name: 引发异常的规则名称
            message: 异常信息，默认为"棋盘与规则存在兼容性问题"
        """
        self.rule_name = rule_name
        self.message = f"{message} (规则: {rule_name})"
        super().__init__(self.message)
