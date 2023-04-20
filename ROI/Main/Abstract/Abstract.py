from abc import ABCMeta, abstractmethod

from ROI.Label.ROILable import ROILabel
from utilitis.Abstract import abstractmetod
from utilitis.JsonRead.JsonRead import loadOffsetsJson


class AbstractR:
    __metaclass__ = ABCMeta

    xOffset, yOffset = loadOffsetsJson()

    def __init__(self, *args, **kwargs):
        self.master = kwargs['master']
        self.label = ROILabel(self, self.master.mainWindow.windowSize)

    def delete(self):
        self.master.ROIList.remove(self)
        self.master.removeLable(self.label)
        self.label = None

    # to do caszowanie metody w celu szybszej ewaluacji
    def calculateOffset(self, x, y):
        return int((x - 25) * self.xOffset), int((y - 25) * self.yOffset)

    @abstractmethod
    def createMarker(self):
        abstractmetod()

    @abstractmethod
    def inROI(self, pos, x, y):
        abstractmetod()

    @abstractmethod
    def getMarker(self, x, y):
        abstractmetod()
