from MAP.Abstract.AbstractMapWindow import AbstractMapWindow

from manipulator.TCIP.TCIPManipulator import TCIPManipulator
from utilitis.JsonRead.JsonRead import loadOffsetsJson
from numpy import ones
import numpy as np


class MapWindowInitialise(AbstractMapWindow):
    # TODO beter values names

    xOffset, yOffset = loadOffsetsJson()

    def __init__(self, master, windowSize, manipulator: TCIPManipulator, *args, **kwargs):
        super(MapWindowInitialise, self).__init__(windowSize, *args, **kwargs)

        self.master = master
        self.manipulator = manipulator

        self.fild = self.master.fildParams

        self.fildSizeXmm, self.fildSizeYmm = self.__fildSizeMM()

        self.fildSizeXpx, self.fildSizeYpx = self.__fildSizePx()

        self.nonScaledMapSizeXInPx, self.nonScaledMapSizeYInPx = self.__nonScaledMapSizeInPx()
        print("Non Scaled Map Size", self.nonScaledMapSizeXInPx, self.nonScaledMapSizeYInPx)

        self.scalX, self.scalY = self.__calculateScaleForMap()
        print("Scale", self.scalY, self.scalX)

        self.scaledMapSizeXInPx, self.scaledMapSizeYInPx = self.__scaledMapSizeInPx()
        print("Scaled Map Size", self.scaledMapSizeXInPx, self.scaledMapSizeYInPx)

        self.scaledCameraFrameSizeX, self.scaledCameraFrameSizeY = self.__scaleCameraSizeInPx()
        self.scaledCameraFrameSize = (int(self.scaledCameraFrameSizeY), int(self.scaledCameraFrameSizeX))
        print("scaled Camera Frame", self.scaledCameraFrameSizeX, self.scaledCameraFrameSizeY)

        self._photoCount, self.photoCount = self.__calculatePhotoCount()

        self.map = ones((int(self.scaledMapSizeXInPx * 2), int(self.scaledMapSizeYInPx * 2), 3), dtype=np.uint8)

        self.movementMap = self.__createMovementMap()

    def __createMovementMap(self):
        movementMap = []
        for i in range(self._photoCount[0] + 1):
            row = []
            for j in range(self._photoCount[1] + 1):
                x = self.fild[0] + self.cameraFrameSizeX / self.xOffset * j
                y = self.fild[2] + self.cameraFrameSizeY / self.yOffset * i
                x, xn, xr = (x, True, x) if x < 50 else (50, False, x)
                y, yn, yr = (y, True, y) if y < 50 else (50, False, y)
                row.append((x, y, xn, yn, xr, yr))
            movementMap.append(row)
        [print(row) for row in movementMap]  # Stworzyc lepsze wypisanie Tabeli
        return movementMap

    def __nonScaledMapSizeInPx(self):
        return self.fildSizeXpx + self.cameraFrameSizeX, self.fildSizeYpx + self.cameraFrameSizeY

    def __calculateScaleForMap(self):  # TODO Scalling to 4k non to Camera Size
        return self.nonScaledMapSizeXInPx / self.cameraFrameSizeX, self.nonScaledMapSizeYInPx / self.cameraFrameSizeY

    def __fildSizeMM(self):
        return self.fild[1] - self.fild[0], self.fild[3] - self.fild[2]

    def __fildSizePx(self):
        return self.xOffset * self.fildSizeXmm, self.yOffset * self.fildSizeYmm

    def __scaledMapSizeInPx(self):
        return self.nonScaledMapSizeXInPx / self.scalX, self.nonScaledMapSizeYInPx / self.scalY

    def __scaleCameraSizeInPx(self):
        return self.cameraFrameSizeX / self.scalX, self.cameraFrameSizeY / self.scalY

    def __calculatePhotoCount(self):

        yint = self.scaledMapSizeYInPx // self.scaledCameraFrameSize[0]
        yfloat = self.scaledMapSizeYInPx / self.scaledCameraFrameSize[0]
        y = yint if yfloat - yint > 0 else yint
        # cameraFrameSizeY = yint

        xint = self.scaledMapSizeXInPx // self.scaledCameraFrameSize[1]
        xfloat = self.scaledMapSizeXInPx / self.scaledCameraFrameSize[1]
        x = xint if xfloat - yint > 0 else xint
        # cameraFreamSizeX = xint

        x, y = int(x), int(y)

        print((y, x))

        return (y, x), [0, 0]
