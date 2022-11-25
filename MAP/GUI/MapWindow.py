from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from numpy import ones
import numpy as np
from MAP.GUI.MapLabel import MapLabel
import cv2

from utilitis.JsonRead.JsonRead import loadOffsetsJson


class MapWindow(QWidget):
    x = 2560
    y = 1440
    dim = (y // 10, x // 10)
    mapPQ = None  # mapa w Pyqt
    crop = None
    map = ones((x, y, 3), dtype=np.uint8)  # mapa jako tablica numpy

    def __init__(self, master, windowSize, *args, **kwargs):
        super(MapWindow, self).__init__(*args, **kwargs)

        self.master = master

        # [25.0, 30.0, 25.0, 30.0, 'pole 0']
        # [xmin,xmax,ymin,ymax,name]
        self.fild = self.master.fildParams

        self.xOffset = self.x / (self.fild[1] - self.fild[0])
        self.yOffset = self.y / (self.fild[3] - self.fild[2])
        self.xOffset, self.yOffset = loadOffsetsJson()

        self.mapViue = MapLabel(self)

        self.setFixedSize(windowSize)
        self.mapViue.setFixedSize(windowSize)

        self.crop = self.scalleFream(master.camera.getFrame())
        self._addFreame(self.crop)

        self.cpmwertMap()

        leyout = QVBoxLayout()
        leyout.addWidget(self.mapViue)
        self.setLayout(leyout)

    def scalleFream(self, fream):
        return cv2.resize(fream, self.dim)

    def conwertManipulatotrCordsToMap(self, manipulatotrX, manipulatorY):
        x = int((manipulatotrX - self.fild[0]) * self.xOffset/10)
        y = int((manipulatorY - self.fild[2]) * self.yOffset/10)

        return x, y

    def _addFreame(self, crop, x=25, y=25):
        x, y = self.conwertManipulatotrCordsToMap(x, y)

        self.map[x:x + (self.x // 10), y:y + (self.y // 10)] = crop

    def addFreame(self, viue, x=25, y=25):
        x, y = self.conwertManipulatotrCordsToMap(x, y)
        self.map[x:x + (self.x // 10), y:y + (self.y // 10)] = self.scalleFream(viue)
        self.cpmwertMap()

    def cpmwertMap(self):
        qImage = QImage(self.map.data, self.map.shape[1], self.map.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)

    def conwertImage(self, image):
        qImage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)
