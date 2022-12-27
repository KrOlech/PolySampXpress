from PyQt5.QtWidgets import QVBoxLayout

from MAP.Abstract.AbstractMapWindow import AbstractMapWindow
from MAP.Label.MapLabel import MapLabel
from manipulator.TCIP.TCIPManipulator import TCIPManipulator
from utilitis.JsonRead.JsonRead import loadOffsetsJson


class MapWindowInitialise(AbstractMapWindow):

    # TODO beter values names

    def __init__(self, master, windowSize, manipulator: TCIPManipulator, *args, **kwargs):
        super(MapWindowInitialise, self).__init__(*args, **kwargs)

        self.master = master
        self.manipulator = manipulator
        self.__windowSize = windowSize
        self.fild = self.master.fildParams

        self.dx, self.dy = self.__deltaXY()
        self.xOffset, self.yOffset = loadOffsetsJson()
        self.maxX, self.maxY = self.__maxXYValues()
        self.scalX, self.scalY = self.__scalXY()

        print(self.scalY, self.scalX)

        self.dim = (int(self.y / self.scalY), int(self.x / self.scalX))
        print(self.dim)

        self._photoCount, self.photoCount = self.__calculatePhotoCount()

        self.cmdx = (self.x / self.xOffset)
        self.cmdy = (self.y / self.yOffset)

        self.mapViue = self.__mapLabel()
        self.__layout()

        self.setFixedSize(windowSize)

    def __mapLabel(self):
        mapViue = MapLabel(self)
        mapViue.setFixedSize(self.__windowSize)
        return mapViue

    def __layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.mapViue)
        self.setLayout(layout)

    def __maxXYValues(self):
        return self.xOffset * self.dx + self.x, self.yOffset * self.dy + self.y

    def __scalXY(self):
        return self.maxX / self.x, self.maxY / self.y

    def __deltaXY(self):
        return self.fild[1] - self.fild[0], self.fild[3] - self.fild[2]

    def __calculatePhotoCount(self):
        yint = self.y // self.dim[0]
        yfloat = self.y / self.dim[0]
        y = yint + 1 if yfloat - yint > 0 else yint
        # y = yint

        xint = self.x // self.dim[1]
        xfloat = self.x / self.dim[1]
        x = xint + 1 if xfloat - yint > 0 else xint
        # x = xint

        print((y, x))

        return (y, x), [0, 0]
