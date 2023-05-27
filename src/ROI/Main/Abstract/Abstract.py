from abc import ABCMeta, abstractmethod
from functools import cache

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from numpy import frombuffer

from src.ROI.Label.ROILable import ROILabel
from src.BaseClass.Abstract import abstractmetod
from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.BaseClass.Logger.Logger import Loger


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
        x0 = self.master.mainWindow.manipulator.x0  # powino to byc zawsze 0 obecnie z uwagi na blad z kalibracja
        y0 = self.master.mainWindow.manipulator.y0
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
        abstractmetod(self)

    @abstractmethod
    def inROI(self, pos, x, y):
        abstractmetod(self)

    @abstractmethod
    def getMarker(self, x, y):
        abstractmetod(self)

    @abstractmethod
    def __dict__(self) -> dict:
        abstractmetod(self)
        return {}

    @abstractmethod
    def createLabelMarker(self, scalaX, scalaY):
        abstractmetod(self)
        return

    @abstractmethod
    def centerOnMe(self):
        x, y = self.foundCenter()
        x -= self.master.master.manipulator.screenSize.width() // 2
        y -= self.master.master.manipulator.screenSize.height() // 2
        x, y = self.convertPixelsTomm(x, y)
        self.loger(x, y)
        self.master.master.manipulator.goToCords(x=x, y=y)

    def convertPixelsTomm(self, x, y):
        return x / self.xOffset, y / self.yOffset

    @abstractmethod
    def foundCenter(self) -> (int, int):
        abstractmetod(self)
        return 0, 0

    @abstractmethod
    def saveViue(self, path):
        abstractmetod(self)

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
