import inspect
from abc import ABCMeta

import cv2
from PyQt5.QtGui import QImage, QPixmap

from utilitis.Logger.Logger import Loger
from utilitis.ThreadWorker.Sleeper.SleeperFun import workSleeperFun


class AbstractMapWindow(Loger):
    __metaclass__ = ABCMeta

    # Pointer to Object of class Map Label for showcase of mam purpose
    mapWidget = None

    # Direction of next frame passable values "R" i "L"
    mapDirection = "R"

    # If true map is finished
    mapEnd = False

    # map container Numpy
    mapNumpy = None

    # map container Pixmap
    mapPx = None

    scaledCameraFrameSize = None

    def move(self, geometry):
        self.mapWidget.move(geometry)

    def showMap(self):
        self.mapWidget.show()

    __ZOOM = "zoom"

    @property
    def ZOOM(self) -> str:
        return type(self).__ZOOM

    __MANIPULATOR_FULL_MOVEMENT_FILEPATH = "ManipulatorFullConfig.json"

    @property
    def MANIPULATOR_FULL_MOVEMENT_FILEPATH(self) -> str:
        return type(self).__MANIPULATOR_FULL_MOVEMENT_FILEPATH

    def convertMap(self):
        qImage = QImage(self.mapNumpy.data, self.mapNumpy.shape[1], self.mapNumpy.shape[0], self.mapNumpy.shape[1] * 3,
                        QImage.Format_BGR888)
        self.mapPx = QPixmap.fromImage(qImage)

    def takePhoto(self):
        return self.scalleFream(self.master.camera.getFrame())

    def scalleFream(self, frame):
        return cv2.resize(frame, self.scaledCameraFrameSize)

    def wait(self, time=30, fun=None):
        workSleeperFun(self, time, fun)
