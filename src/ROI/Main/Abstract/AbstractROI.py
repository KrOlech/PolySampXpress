from abc import ABCMeta

from PyQt5.QtCore import QRect, QPoint

from src.ROI.Main.Abstract.Abstract import AbstractR


class AbstractROI(AbstractR):
    __metaclass__ = ABCMeta

    rect = None

    x0, x1, y0, y1 = 0, 0, 0, 0

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
        #self.loger(f"x1 = {self.x0}, x2 = {self.x1}, y1 = {self.y0}, y2 = {self.y1}, manipulatotrX = {x}, manipulatorY = {y} deltaX = {dx} deltaY = {dy}")
        return QRect(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x1 - dx, self.y1 - dy))

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
