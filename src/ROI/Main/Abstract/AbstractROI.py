from abc import ABCMeta
from functools import cache

from PyQt5.QtCore import QRect, QPoint

from src.ROI.Main.Abstract.Abstract import AbstractR


class AbstractROI(AbstractR):
    __metaclass__ = ABCMeta

    rect = None

    x0, x1, y0, y1 = 0, 0, 0, 0
    x0Label, x1Label, y0Label, y1Label = 0, 0, 0, 0

    minX, minY = 0, 0
    maxX, maxY = 0, 0

    def __init__(self, *args, **kwargs):
        super(AbstractROI, self).__init__(*args, **kwargs)

        dx, dy = self.calculateOffset(kwargs["manipulatotrX"], kwargs["manipulatorY"])

        x1, y1, x2, y2 = kwargs["x1"] + dx, kwargs['y1'] + dy, kwargs['x2'] + dx, kwargs["y2"] + dy
        self.__setBorders(x1, x2, y1, y2)

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
    def getMarkerMap(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]

        x0mm = x0 / self.xOffset
        x1mm = x1 / self.xOffset
        y0mm = y0 / self.yOffset
        y1mm = y1 / self.yOffset

        x0mm -= mapX0
        x1mm -= mapX0
        y0mm -= mapY0
        y1mm -= mapY0

        x0mm /= mapWidth
        x1mm /= mapWidth
        y0mm /= mapHeight
        y1mm /= mapHeight

        x0mm *= screenheight
        x1mm *= screenheight
        y0mm *= screenWidth
        y1mm *= screenWidth

        x0mm /= scale
        x1mm /= scale
        y0mm /= scale
        y1mm /= scale

        x0mm = int(x0mm)
        x1mm = int(x1mm)
        y0mm = int(y0mm)
        y1mm = int(y1mm)

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
