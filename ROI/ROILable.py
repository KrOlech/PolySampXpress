import cv2
from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel


class ROILabel(QLabel):
    x = 256
    y = 144
    scalaX = 10
    scalaY = 10

    def __init__(self, roi, *args, **kwargs):
        super(ROILabel, self).__init__(*args, **kwargs)

        self.roi = roi

        self.rectangle = self._convertRectagle()

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), self.conwertViue())

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

        qp.drawRect(self.rectangle)

    def _convertRectagle(self):
        return QRect(QPoint(self.roi.x0 // self.scalaX, self.roi.y0 // self.scalaY),
                     QPoint(self.roi.x1 // self.scalaX, self.roi.y1 // self.scalaY))

    def update(self):
        self.rectangle = self._convertRectagle()

    def conwertViue(self):
        cvBGBImg = self.roi.viue[self.roi.y0:self.roi.y1, self.roi.x0:self.roi.x1].copy()
        cvBGBImg = cv2.resize(cvBGBImg,[256,144])
        img = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)
        return QPixmap.fromImage(img)
