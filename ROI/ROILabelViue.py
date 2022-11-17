from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QLabel


class ROILegendViue(QLabel):
    x = 256
    y = 144
    scalaX = 10
    scalaY = 10

    def __init__(self, roi, *args, **kwargs):
        super(ROILegendViue, self).__init__(*args, **kwargs)

        self.roi = roi

        self.rectangle = self._convertRectagle()

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), self.roi.viue)

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

        qp.drawRect(self.rectangle)

    def _convertRectagle(self):
        return QRect(QPoint(self.roi.x0 // self.scalaX, self.roi.y0 // self.scalaY),
                     QPoint(self.roi.x1 // self.scalaX, self.roi.y1 // self.scalaY))

    def update(self):
        self.rectangle = self._convertRectagle()
