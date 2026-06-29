from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel
from Python.FrontEnd.MyQPoint.MyQPoint import MyQPoint

class ZoomLabel(QLabel):

    def __init__(self, master, value):
        super().__init__(master)

        self.setFixedWidth(master.windowSize.width() // 8)

        self.setStyleSheet("background-color: rgba(255, 255, 255, 75);")
        self.setText(str(value))
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)
        self.move(
            MyQPoint(master.windowSize.width() - (master.windowSize.width() // 8), master.windowSize.height() - self.height()))
        self.show()

    def setText(self, a0: str) -> None:
        super().setText("zoom: " + a0)
