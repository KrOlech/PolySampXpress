from abc import ABCMeta

from PyQt5.QtCore import QRect, QPoint

from src.ROI.Main.Abstract.Abstract import AbstractR


class AbstractPoint(AbstractR):
    __metaclass__ = ABCMeta

    rect = None

    x0, y0 = 0, 0
    x1, y1 = 0, 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        dx, dy = self.calculateOffset(kwargs["manipulatotrX"], kwargs["manipulatorY"])

        self.x0, self.y0 = kwargs["x1"] + dx, kwargs['y1'] + dy
        self.x1, self.y1 = kwargs["x1"] + dx, kwargs['y1'] + dy

    def createMarker(self):
        return QRect(QPoint(self.x0, self.y0), QPoint(self.x0, self.y0))

    def inROI(self, pos, x, y):
        dx, dy = self.calculateOffset(x, y)
        return self.x0 - dx - 20 < pos.x() < self.x0 - dx + 20 and self.y0 - dy - 20 < pos.y() < self.y0 - dy + 20

    def getMarker(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        return QRect(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x0 - dx, self.y0 - dy))
