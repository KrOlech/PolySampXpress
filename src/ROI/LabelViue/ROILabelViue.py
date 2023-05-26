from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QLabel


class ROILegendVue(QLabel):

    def __init__(self, roi, x, y, xScale, yScale, *args, **kwargs):
        super(ROILegendVue, self).__init__(kwargs['widget'])

        self.x, self.y = x, y
        self.scalaX, self.scalaY = xScale, yScale

        self.roi = roi

        self.rectangle = self.__convertRectagle()

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), self.roi.view)

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

        qp.drawRect(self.rectangle)

    def __convertRectagle(self):
        return QRect(QPoint(self.roi.x0Label // self.scalaX, self.roi.y0Label // self.scalaY),
                     QPoint(self.roi.x1Label // self.scalaX, self.roi.y1Label // self.scalaY))

    def update(self):
        self.rectangle = self.__convertRectagle()
