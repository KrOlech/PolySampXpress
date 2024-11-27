import json
import zipfile
from abc import ABCMeta
from io import BytesIO
from os import curdir, chdir

import numpy as np
from PIL import Image

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from numpy import frombuffer

from Python.BackEnd.ROI.Main.Abstract.Abstract import AbstractR
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

    fildParams = None

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

                self.mapNumpy = self.mapNumpy[:, :, ::-1]
                img = Image.fromarray(self.mapNumpy)

                imgByte = BytesIO()
                img.save(imgByte, format='PNG')

                zipF.writestr(name, imgByte.getvalue())

        chdir(currentDirectory)

    def createMapDict(self) -> dict:
        return {
            self.mapId: {"MapParams": self.mapParams.dictionary, "MapName": self.name, "fildParams": self.fildParams}}

    def loadMapFile(self):

        filePath, _ = QFileDialog.getOpenFileName(self.master, "Select file with Roi List", "",
                                                  "Zip Files (*.zip)")

        currentDirectory = curdir

        if not filePath or not currentDirectory:
            self.loger("File loading interrupted by user no file was selected to load")
            return

        self.loger(filePath)

        with zipfile.ZipFile(filePath, 'r') as zipF:
            with zipF.open('data.json') as jsonfile:
                json_data = jsonfile.read().decode('utf-8')
                data = json.loads(json_data)
                self.loger("Dictionary from JSON:", data)

            fileName = list(data.keys())[0]

            with zipF.open(fileName + '.png') as imgfile:
                img = np.array(Image.open(BytesIO(imgfile.read())))

                #qImg = QPixmap.fromImage(QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888))

        return data, img
