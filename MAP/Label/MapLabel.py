from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QLabel, QSizePolicy, QSizeGrip
from PyQt5 import QtCore, QtWidgets

from MainWindow.Utilitis.WindowBar import MyBar


class MapLabel(QLabel):
    _aspectRatio = 4 / 3

    def __init__(self, master, *args, **kwargs):
        super(MapLabel, self).__init__(*args, **kwargs)

        self.master = master

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Map")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            grip.setStyleSheet("""background-color: transparent; """)
            self.grips.append(grip)

    def resizeEvent(self, event):
        rect = self.rect()
        self.grips[1].move(rect.right() - self.gripSize, 0)
        self.grips[2].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        self.grips[3].move(0, rect.bottom() - self.gripSize)
        width = self.widthForHeight(event.size().height())
        self.resize(width, event.size().height())
        self.titleBar.resize(self.width(), self.titleBar.height())

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.drawPixmap(self.rect(), self.master.mapPx)
        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

    def setAspectRatio(self, aspectRatio):
        self._aspectRatio = aspectRatio
        self.updateGeometry()

    def sizeHint(self):
        width = self.widthForHeight(self.height())
        return self.minimumSizeHint().expandedTo(QSize(width, self.height()))

    def widthForHeight(self, height):
        return int(height * self._aspectRatio)
