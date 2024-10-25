from abc import ABC
from functools import cache

from PyQt5.QtCore import QLine, QPoint

from Python.BackEnd.ROI.Main.Abstract.Abstract import AbstractR


class AbstractLine(AbstractR, ABC):

    x0, x1, y0, y1 = 0, 0, 0, 0
    x0Label, x1Label, y0Label, y1Label = 0, 0, 0, 0

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.x0, self.x1, self.y0, self.y1 = self.calculateCords(**kwargs)


    def createMarker(self):
        return QLine(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def inROI(self, pos, x, y):  # toDo Bounding Box for edit
        dx, dy = self.calculateOffset(x, y)
        p0 = self.x0 - dx - 20 < pos.x() < self.x0 - dx + 20 and self.y0 - dy - 20 < pos.y() < self.y0 - dy + 20
        p1 = self.x1 - dx - 20 < pos.x() < self.x1 - dx + 20 and self.y1 - dy - 20 < pos.y() < self.y1 - dy + 20
        return p0 or p1

    def getMarker(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        return QLine(QPoint(self.x0 + dx, self.y0 + dy), QPoint(self.x1 + dx, self.y1 + dy))

    @cache
    def getMarkerMap(self, *args):
        x0mm, y0mm, x1mm, y1mm = self.calculateMapMarker4Cordynats(self, *args)

        return QLine(QPoint(x0mm, y0mm), QPoint(x1mm, y1mm))

    def foundCenter(self) -> (int, int):
        return (self.x1 + self.x0) // 2, (self.y1 + self.y0) // 2

    def foundAbsoluteCenter(self) -> (int, int):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]
        return (x1 + x0) // 2, (y1 + y0) // 2
