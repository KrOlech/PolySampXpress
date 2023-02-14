from PySide2.QtCore import QRect, QPoint
from PySide2.QtGui import QPainter, QBrush, QColor
from PySide2.QtWidgets import QLabel


class MapLabel(QLabel):

    def __init__(self, master, *args, **kwargs):
        super(MapLabel, self).__init__(*args, **kwargs)

        self.master = master

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), self.master.mapPx)

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))
