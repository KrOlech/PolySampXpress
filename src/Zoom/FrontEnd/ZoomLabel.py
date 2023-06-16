from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


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
            QPoint(master.windowSize.width() - (master.windowSize.width() // 8), master.windowSize.height() - 25))
        self.show()

    def setText(self, a0: str) -> None:
        super().setText("zoom: " + a0)
