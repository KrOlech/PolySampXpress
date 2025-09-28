from PyQt6.QtCore import QPoint


class MyQPoint(QPoint):
    def __init__(self, x, y):
        super().__init__(int(x), int(y))