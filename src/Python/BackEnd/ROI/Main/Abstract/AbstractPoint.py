from abc import ABCMeta
from functools import cache

from PyQt5.QtCore import QRect, QPoint, QLine

from src.Python.BackEnd.ROI.Main.Abstract.Abstract import AbstractR


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
        l1 = QLine(QPoint(self.x0 + dx + 10, self.y0 + dx), QPoint(self.x0 + dx - 10, self.y0 + dx))
        l2 = QLine(QPoint(self.x0 + dx, self.y0 + dx + 10), QPoint(self.x0 + dx, self.y0 + dx - 10))
        return [l1, l2]

    @cache
    def getMarkerMap(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale, MapLabel):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]

        x0mm = x0 / self.xOffset
        y0mm = y0 / self.yOffset

        x0mm = int(MapLabel.calculatePixels(x0mm, screenWidth, mapX0, mapX0 + mapWidth))
        y0mm = int(MapLabel.calculatePixels(y0mm, screenheight, mapY0, mapY0 + mapHeight))

        l1 = QLine(QPoint(x0mm + 10, y0mm), QPoint(x0mm - 10, y0mm))
        l2 = QLine(QPoint(x0mm, y0mm + 10), QPoint(x0mm, y0mm - 10))

        self.loger(x0mm, y0mm)
        return [l1, l2]

    def foundCenter(self) -> (int, int):
        return self.x0, self.y0
