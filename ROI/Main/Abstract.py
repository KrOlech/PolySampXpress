from abc import ABCMeta

from PyQt5.QtCore import QRect, QPoint

from ROI.Label.ROILable import ROILabel
from ROI.Main.CommonNames import CommonNames
from utilitis.JsonRead.JsonRead import loadOffsetsJson


class AbstractROI(CommonNames):
    __metaclass__ = ABCMeta

    rect = None

    x0, x1, y0, y1 = 0, 0, 0, 0

    minX, minY = 0, 0
    maxX, maxY = 0, 0

    xOffset, yOffset = loadOffsetsJson()

    def __init__(self, *args, **kwargs):
        self.master = kwargs['master']
        self.label = ROILabel(self, self.master.mainWindow.windowSize)

    def delete(self):
        self.master.ROIList.remove(self)
        self.master.removeLable(self.label)
        self.label = None

    def calculateOffset(self, x, y):
        return int((x - 25) * self.xOffset), int((y - 25) * self.yOffset)

    def createRectangle(self):
        return QRect(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def inROI(self, pos, x, y):
        dx, dy = self.calculateOffset(x, y)
        return self.minX - dx < pos.x() < self.maxX - dx and self.minY - dy < pos.y() < self.maxY - dy

    def getRect(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        return QRect(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x1 - dx, self.y1 - dy))
