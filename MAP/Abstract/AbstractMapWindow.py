import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from numpy import ones
from MAP.Label.MapLabel import MapLabel
from utilitis.JsonRead.JsonRead import loadCameraResolutionJson
from utilitis.ThreadWorker.Sleeper.SleeperFun import workSleeperFun


class AbstractMapWindow(QWidget):
    cameraFrameSizeX, cameraFrameSizeY = loadCameraResolutionJson()  # 2560, 1440

    mapPQ = None  # mapa w Pyqt
    crop = None
    #map = ones((cameraFrameSizeX * 2, cameraFrameSizeY * 2, 3), dtype=np.uint8)  # mapa jako tablica numpy #TODO wlasciwa wartosc to bez przemnorzenia prz 2 #TODO wlasciwa inicializacja
    mapDirection = "R"
    mapEnd = None
    scaledCameraFrameSize = None

    def __init__(self, windowSize, *args, **kwargs):
        super(AbstractMapWindow, self).__init__(*args, **kwargs)
        self.__windowSize = windowSize
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

    def scalleFream(self, frame):
        return cv2.resize(frame, self.scaledCameraFrameSize)

    def cpmwertMap(self):
        qImage = QImage(self.map.data, self.map.shape[1], self.map.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)

    def conwertImage(self, image):
        qImage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)

    def wait(self, time=30, fun=None):
        workSleeperFun(self, time, fun)

    def _addFrameZero(self, crop):
        print(crop.shape)
        self.map[: int(self.cameraFrameSizeX / self.scalX), :int(self.cameraFrameSizeY / self.scalY)] = crop
        self.cpmwertMap()
