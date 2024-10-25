from abc import ABC
from functools import cache

from PyQt5.QtCore import QRect, QPoint

from Python.BackEnd.ROI.Main.Abstract.Abstract import AbstractR


class AbstractROI(AbstractR, ABC):
    rect = None

    x0, x1, y0, y1 = 0, 0, 0, 0
    x0Label, x1Label, y0Label, y1Label = 0, 0, 0, 0

    minX, minY = 0, 0
    maxX, maxY = 0, 0

    def __init__(self, *args, **kwargs):
        super(AbstractROI, self).__init__(*args, **kwargs)

        self.__setBorders(*self.calculateCords(**kwargs))

    def createMarker(self):
        return QRect(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def inROI(self, pos, x, y):
        dx, dy = self.calculateOffset(x, y)
        return self.minX - dx - 20 < pos.x() < self.maxX - dx + 20 and self.minY - dy - 20 < pos.y() < self.maxY - dy + 20

    def getMarker(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        # self.loger(f"x1 = {self.x0}, x2 = {self.x1}, y1 = {self.y0}, y2 = {self.y1}, manipulatotrX = {x}, manipulatorY = {y} deltaX = {dx} deltaY = {dy}")
        return QRect(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x1 - dx, self.y1 - dy))

    @cache
    def getMarkerMap(self, *args):
        x0mm, y0mm, x1mm, y1mm = self.calculateMapMarker4Cordynats(self, *args)

        return QRect(QPoint(x0mm, y0mm), QPoint(x1mm, y1mm))

    def __setBorders(self, x1, x2, y1, y2):
        self.minX = min(x1, x2)
        self.minY = min(y1, y2)
        self.maxX = max(x1, x2)
        self.maxY = max(y1, y2)
        self.x0 = self.minX
        self.x1 = self.maxX
        self.y0 = self.minY
        self.y1 = self.maxY

    def setNewBorders(self):
        self.__setBorders(self.x0, self.x1, self.y0, self.y1)

    def foundCenter(self) -> (int, int):
        return self.x0 + (self.x1 - self.x0) // 2, self.y0 + (self.y1 - self.y0) // 2

    def foundAbsoluteCenter(self) -> (int, int):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]
        return x0 + (x1 - x0) // 2, y0 + (y1 - y0) // 2
