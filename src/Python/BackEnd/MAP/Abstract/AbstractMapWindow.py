import json
import zipfile
from abc import ABCMeta
from io import BytesIO
from os import curdir, chdir
from PIL import Image

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog

from Python.BaseClass.Logger.Logger import Loger
from Python.BackEnd.ThreadWorker.Sleeper.SleeperFun import workSleeperFun


class AbstractMapWindow(Loger):
    __metaclass__ = ABCMeta

    # Pointer to Object of class Map Label for showcase of mam purpose
    mapWidget = None

    # Direction of next frame passable values "R" i "L"
    mapDirection = "R"

    # If a true map is finished
    mapEnd = False

    # map container Numpy
    mapNumpy = None
    mapNumpyBorders = None

    # map container Pixmap
    mapPx = None

    scaledCameraFrameSize = None

    missedFrames = 0

    master = None

    name = None

    x0 = 100
    y0 = 100

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
        # cv2.imwrite(f"Map_{self.photoCount}.png",frame)
        return self.scalleFream(frame)

    def scalleFream(self, frame):
        return cv2.resize(frame, self.scaledCameraFrameSize)

    def wait(self, time=30, fun=None):
        workSleeperFun(self, time, fun)

    def setName(self, newName):
        self.name = newName
        self.menu.setTitle(newName)

    def saveMapFile(self):
        dict = self.createMapDict()

        currentDirectory = curdir

        folderPath, _ = QFileDialog.getSaveFileName(self.master, "Select Location to save Roi List", "",
                                                    "Zip Files (*.zip)")

        self.loger(f"folder path: {folderPath}")

        if folderPath:
            fileName = folderPath[folderPath.rfind(r"/") + 1:]

            chdir(folderPath[:folderPath.rfind(r"/")])

            with zipfile.ZipFile(f'{fileName}', 'w') as zipF:
                with zipF.open('data.json', 'w') as jsonfile:
                    jsonfile.write(json.dumps(dict, indent=4).encode('utf-8'))

                name = str(self.mapId) + ".png"

                img = Image.fromarray(self.mapNumpy)

                imgByte = BytesIO()
                img.save(imgByte, format='PNG')

                zipF.writestr(name, imgByte.getvalue())

        chdir(currentDirectory)

    def createMapDict(self) -> dict:
        return {self.mapId: {"MapParams": self.mapParams.dictionary, "MapName": self.name}}
