import cv2
import numpy as np
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget
from numpy import ones

from MAP.GUI.Sleeper import sleeper
from utilitis.JsonRead.JsonRead import loadCameraResolutionJson


class AbstractMapWindow(QWidget):
    x, y = loadCameraResolutionJson()  # 2560, 1440

    mapPQ = None  # mapa w Pyqt
    crop = None
    map = ones((x, y, 3), dtype=np.uint8)  # mapa jako tablica numpy
    mapDirection = None
    mapEnd = None

    def scalleFream(self, fream):
        return cv2.resize(fream, self.dim)

    def cpmwertMap(self):
        qImage = QImage(self.map.data, self.map.shape[1], self.map.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)

    def conwertImage(self, image):
        qImage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_BGR888)
        self.mapPQ = QPixmap.fromImage(qImage)

    def wait(self, time, fun=None):
        self.thread1 = QThread()
        #self.worker1 = sleeper(self, time*30, fun)
        self.worker1 = sleeper(self, 0.1, fun)

        self.worker1.moveToThread(self.thread1)

        self.thread1.started.connect(self.worker1.run)
        self.worker1.finished.connect(self.thread1.quit)
        self.worker1.finished.connect(self.worker1.deleteLater)
        self.thread1.finished.connect(self.thread1.deleteLater)

        self.thread1.start()

    def _addFrameZero(self, crop):
        self.map[: int(self.x / self.scalX), :int(self.y / self.scalY)] = crop
        self.cpmwertMap()
