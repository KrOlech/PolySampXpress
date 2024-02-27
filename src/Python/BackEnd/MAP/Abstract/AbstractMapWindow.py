from abc import ABCMeta

import cv2
from PyQt5.QtGui import QImage, QPixmap

from Python.BaseClass.Logger.Logger import Loger
from Python.BackEnd.ThreadWorker.Sleeper.SleeperFun import workSleeperFun


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
    mapNumpyBorders = None

    # map container Pixmap
    mapPx = None

    scaledCameraFrameSize = None

    missedFrames = 0

    master = None

    def move(self, geometry):
        self.mapWidget.move(geometry)

    def showMap(self):
        if self.master.mozaikBorders.isChecked():
            self.mapPx = self.convertMap(self.mapNumpyBorders)
        else:
            self.mapPx = self.convertMap(self.mapNumpy)

        self.mapWidget.show()
        self.mapWidget.activateWindow()

    __ZOOM = "zoom"

    @property
    def ZOOM(self) -> str:
        return type(self).__ZOOM

    __MANIPULATOR_FULL_MOVEMENT_FILEPATH = "ManipulatorFullConfig.json"

    @property
    def MANIPULATOR_FULL_MOVEMENT_FILEPATH(self) -> str:
        return type(self).__MANIPULATOR_FULL_MOVEMENT_FILEPATH

    @staticmethod
    def convertMap(mozaikData):
        qImage = QImage(mozaikData.data, mozaikData.shape[1], mozaikData.shape[0], mozaikData.shape[1] * 3,
                        QImage.Format_BGR888)
        return QPixmap.fromImage(qImage)

    def takePhoto(self):
        frame = self.master.camera.getFrame()
        cv2.imwrite(f"Map_{self.photoCount}.png",frame)
        return self.scalleFream(frame)

    def scalleFream(self, frame):
        return cv2.resize(frame, self.scaledCameraFrameSize)

    def wait(self, time=30, fun=None):
        workSleeperFun(self, time, fun)
