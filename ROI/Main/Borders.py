from abc import ABCMeta

from ROI.Main.Abstract import AbstractROI


class ROIBorders(AbstractROI):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        super(ROIBorders, self).__init__(*args, **kwargs)

        dx, dy = self.calculateOffset(kwargs["manipulatotrX"], kwargs["manipulatorY"])

        x1, y1, x2, y2 = kwargs["x1"] + dx, kwargs['y1'] + dy, kwargs['x2'] + dx, kwargs["y2"] + dy
        self.__setBorders(x1, x2, y1, y2)

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
