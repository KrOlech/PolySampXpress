from abc import ABCMeta, abstractmethod
from functools import cache

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from numpy import frombuffer

from Python.BackEnd.ROI.Label.ROILable import ROILabel
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger
from Python.FrontEnd.MainWindow.RoiCreation.ScatterConfigureWindow import ScatterConfigureWindow


class AbstractR(Loger):
    __metaclass__ = ABCMeta

    scatter = None
    zoom = None
    pixelAbsolutValue = None

    def __init__(self, *args, **kwargs):

        self.master = kwargs['master']
        self.label = ROILabel(self, self.master.mainWindow.windowSize)

    def delete(self):
        try:
            self.master.ROIList.remove(self)
            self.master.removeLable(self.label)
            self.label = None
        except Exception as e:
            self.logError(e)

    def resolveZeroPoint(self):

        currentZoom = self.master.mainWindow.zoom
        try:
            zeroPoint = self.master.mainWindow.zeroPoint[currentZoom]
            xp = zeroPoint.x0
            yp = zeroPoint.y0
            xOffsetP, yOffsetP = JsonHandling.loadOffsetsJson(currentZoom)
            zeroPointStatus = True
        except KeyError as e:
            xp = 0
            yp = 0
            xOffsetP, yOffsetP = 1, 1
            zeroPointStatus = False
            self.logWarning("Zero Point was not set")

        return xp / xOffsetP, yp / yOffsetP, zeroPointStatus

    @cache
    def calculateOffset(self, x, y):
        x0 = self.master.mainWindow.manipulatorInterferes.x0
        y0 = self.master.mainWindow.manipulatorInterferes.y0
        ox, oy = self.calculateOffsetStatic(x, y, x0, y0)
        self.loger(f"wynik x={ox}, offset y={oy}")
        return ox, oy

    def calculateOffsetStatic(self, x, y, mx=0, my=0):
        xOffset, yOffset = JsonHandling.loadOffsetsJson(self.master.mainWindow.zoom)
        ox = int((x - mx) * xOffset)
        oy = int((y - my) * yOffset)
        return ox, oy

    def calculateMapMarker4Cordynats(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale,
                                     MapLabel):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]

        x0mm = x0 / self.xOffset
        x1mm = x1 / self.xOffset
        y0mm = y0 / self.yOffset
        y1mm = y1 / self.yOffset

        self.loger("milimetry", x0mm, y0mm, x1mm, y1mm)

        x0mm = int(MapLabel.calculatePixels(x0mm, screenWidth, mapX0, mapX0 + mapWidth))
        y0mm = int(MapLabel.calculatePixels(y0mm, screenheight, mapY0, mapY0 + mapHeight))
        x1mm = int(MapLabel.calculatePixels(x1mm, screenWidth, mapX0, mapX0 + mapWidth))
        y1mm = int(MapLabel.calculatePixels(y1mm, screenheight, mapY0, mapY0 + mapHeight))

        self.loger("pixele", x0mm, y0mm, x1mm, y1mm)

        return x0mm, y0mm, x1mm, y1mm

    def calculateCords(self, **kwargs):
        dx, dy = self.calculateOffset(kwargs["manipulatotrX"], kwargs["manipulatorY"])

        return kwargs["x1"] + dx, kwargs['x2'] + dx, kwargs['y1'] + dy, kwargs["y2"] + dy

    @abstractmethod
    def createMarker(self):
        self.abstractmetod()

    @abstractmethod
    def inROI(self, pos, x, y):
        self.abstractmetod()

    @abstractmethod
    def getMarker(self, x, y):
        self.abstractmetod()

    @abstractmethod
    def getMarkerMap(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale):
        self.abstractmetod()

    @abstractmethod
    def __dict__(self) -> dict:
        self.abstractmetod()
        return {}

    @abstractmethod
    def createLabelMarker(self, scalaX, scalaY):
        self.abstractmetod()
        return

    @abstractmethod
    def centerOnMe(self):
        x, y = self.foundCenter()
        x -= self.master.mainWindow.windowSize.width() // 2
        y -= self.master.mainWindow.windowSize.height() // 2
        x, y = self.convertPixelsTomm(x, y)
        self.loger(x, y)
        self.master.mainWindow.manipulatorInterferes.goToCords(x=x, y=y)

    def convertPixelsTomm(self, x, y):
        self.xOffset, self.yOffset = JsonHandling.loadOffsetsJson(self.master.mainWindow.zoom)
        return x / self.xOffset, y / self.yOffset

    @abstractmethod
    def foundCenter(self) -> (int, int):
        self.abstractmetod()
        return 0, 0

    @abstractmethod
    def foundAbsoluteCenter(self) -> (int, int):
        self.abstractmetod()
        return 0, 0

    def resolveFileDict(self):
        self.fillFileDict()
        self.saveCenterToFileDict()
        return self.fileDict

    def saveCenterToFileDict(self):
        xCenter, yCenter = self.foundAbsoluteCenter()
        self.fileDict["Pixell Values"]["center Pixell"] = {"x": xCenter, "y": yCenter}

        xOffset, yOffset = JsonHandling.loadOffsetsJson(self.zoom)
        xCenterMM, yCenterMM = xCenter / xOffset, yCenter / xOffset,
        self.fileDict["mm Values"]["center mm"] = {"x": xCenterMM, "y": yCenterMM}

        deltaX, deltaY, zeroPointStatus = self.resolveZeroPoint()
        self.fileDict["sample mm Values"]["sample center mm"] = {"x": xCenterMM - deltaX, "y": yCenterMM - deltaY}

    @abstractmethod
    def saveViue(self, path):
        self.abstractmetod()

    @staticmethod
    def convertQimageToQpixmap(qimage):
        return QPixmap.fromImage(qimage)

    @staticmethod
    def convertQpixmapToOpenCV(Qpixmap):
        image_array = Qpixmap.toImage().convertToFormat(QImage.Format_RGB888)
        width = image_array.width()
        height = image_array.height()
        buffer = image_array.bits().asstring(width * height * 3)

        opencv_image = frombuffer(buffer, dtype=np.uint8).reshape((height, width, 3))
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

        return opencv_image

    @staticmethod
    def convertQimageToOpenCV(qimage):
        return AbstractR.convertQpixmapToOpenCV(AbstractR.convertQimageToQpixmap(qimage))

    @abstractmethod
    def editScatter(self):
        self.scatter = True
        self.fileDict["scatter"] = True
        ScatterConfigureWindow(self.master).exec_()
