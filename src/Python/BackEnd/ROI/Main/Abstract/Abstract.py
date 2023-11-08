from abc import ABCMeta, abstractmethod
from functools import cache

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from numpy import frombuffer

from src.Python.BackEnd.ROI.Label.ROILable import ROILabel
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Python.BaseClass.Logger.Logger import Loger


class AbstractR(Loger):
    __metaclass__ = ABCMeta

    xOffset, yOffset = JsonHandling.loadOffsetsJson()

    def __init__(self, *args, **kwargs):
        self.master = kwargs['master']
        self.label = ROILabel(self, self.master.mainWindow.windowSize)

    def delete(self):
        self.master.ROIList.remove(self)
        self.master.removeLable(self.label)
        self.label = None

    @cache
    def calculateOffset(self, x, y):
        x0 = self.master.mainWindow.manipulatorInterferes.x0
        y0 = self.master.mainWindow.manipulatorInterferes.y0
        ox, oy = self.calculateOffsetStatic(x, y, x0, y0)
        self.loger(f"wynik x={ox}, offset y={oy}")
        return ox, oy

    @staticmethod
    @cache
    def calculateOffsetStatic(x, y, mx=0, my=0):
        ox = int((x - mx) * AbstractR.xOffset)
        oy = int((y - my) * AbstractR.yOffset)
        return ox, oy

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
        return x / self.xOffset, y / self.yOffset

    @abstractmethod
    def foundCenter(self) -> (int, int):
        self.abstractmetod()
        return 0, 0

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
