from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QLabel

from MainWindow.Utilitis.WindowBar import MyBar


class MapLabel(QLabel):

    def __init__(self, master, *args, **kwargs):
        super(MapLabel, self).__init__(*args, **kwargs)

        self.master = master

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self,"Map")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), self.master.mapPx)

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))
