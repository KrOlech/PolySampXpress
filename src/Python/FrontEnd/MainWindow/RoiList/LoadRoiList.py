import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from os import chdir, curdir
import zipfile
import json
import numpy as np
from PIL import Image
from io import BytesIO

from Python.BackEnd.ROI.Main.Point.Point import Point
from Python.BackEnd.ROI.Main.ROI.ROI import ROI
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class LoadRoiList(JsonHandling):
    directoryPath: str = ""
    filePath: str = ""
    currentDirectory: str = ""

    def __init__(self, master):
        self.master = master

        self.absolutPxX = self.master.cameraView.pixelAbsolutValue[0]
        self.absolutPxY = self.master.cameraView.pixelAbsolutValue[1]

    def load(self):

        self.filePath, currentDirectory = self.resolveFile()

        if not self.filePath or not currentDirectory:
            self.loger("File loading interrupted by user no file was selected to load")
            return

        self.directoryPath = self.filePath[:self.filePath.rfind(r"/")]

        self.loger(self.filePath)

        with zipfile.ZipFile(self.filePath, 'r') as zipF:

            with zipF.open('data.json') as jsonfile:
                json_data = jsonfile.read().decode('utf-8')
                data = json.loads(json_data)
                self.loger("Dictionary from JSON:", data)

            for fileName in zipF.namelist():
                if fileName.endswith('.png') or fileName.endswith('.jpg'):

                    with zipF.open(fileName) as imgfile:

                        img = np.array(Image.open(BytesIO(imgfile.read())))

                        qImg = QPixmap.fromImage(QImage(img.data, img.shape[1], img.shape[0], QImage.Format_BGR888))

                        name = fileName[:fileName.rfind(r".")]

                        cords = data[name]['Pixell Values']

                        if len(cords) == 4:
                            roi = ROI(self.master.cameraView, cords["x0"] + self.absolutPxX,
                                      cords["y0"] + self.absolutPxY,
                                      cords["x1"] + self.absolutPxX, cords["y1"] + self.absolutPxY, name, 0,
                                      0, self.master.cameraView.pixelAbsolutValue, scatter=data[name]["scatter"],
                                      viue=qImg,
                                      zoom=data[name]["zoom"])

                        elif len(cords) == 2:
                            roi = Point(self.master.cameraView, cords["x0"] + self.absolutPxX,
                                        cords["y0"] + self.absolutPxY,
                                        name, 0,
                                        0, self.master.cameraView.pixelAbsolutValue, viue=qImg,
                                        zoom=data[name]["zoom"])
                        self.master.cameraView.ROIList.append(roi)

                        self.master.addROIToList()

            self.master.cameraView.roiNames = len(self.master.cameraView.ROIList)

        self.master.autoZoomMode = True
        self.master.zooms.setCurrentText(str(self.master.cameraView.ROIList[-1].zoom))
        self.master.autoZoomMode = False

    def loadDeprecated(self):

        self.filePath, currentDirectory = self.resolveFile()

        if not self.filePath or not currentDirectory:
            self.loger("File loading interrupted by user no file was selected to load")
            return

        self.directoryPath = self.filePath[:self.filePath.rfind(r"/")]

        self.loger(self.filePath)

        data = JsonHandling.readFileRow(self.filePath)
        try:
            for name, values in data.items():
                cords = values['absolute Pixell Values']

                img = self.loadImage(name)

                if len(cords) == 4:
                    roi = ROI(self.master.cameraView, cords["x0"] + self.absolutPxX, cords["y0"] + self.absolutPxY,
                              cords["x1"] + self.absolutPxX, cords["y1"] + self.absolutPxY, name, 0,
                              0, self.master.cameraView.pixelAbsolutValue, scatter=values["scatter"], viue=img,
                              zoom=values["zoom"])

                elif len(cords) == 2:
                    roi = Point(self.master.cameraView, cords["x0"] + self.absolutPxX, cords["y0"] + self.absolutPxY,
                                name, 0,
                                0, self.master.cameraView.pixelAbsolutValue, viue=img, zoom=values["zoom"])

                self.master.cameraView.ROIList.append(roi)

                self.master.addROIToList()

            self.master.cameraView.roiNames = len(self.master.cameraView.ROIList)

        except KeyError as e:
            self.logError(e)
            self.logError("Incorect Fille for Roi List Recreation")

            msg = QMessageBox()
            msg.setWindowTitle("Incorect Fille for Roi List Recreation")
            msg.setText("Incorect Fille for Roi List Recreation")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel)

            msg.exec_()


        finally:
            chdir(currentDirectory)

    def resolveFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self.master, "Select file with Roi List", "",
                                                  "Json Files (*.zip)")
        return filePath, curdir

    def loadImage(self, name):
        self.loger(self.directoryPath + r"/" + name)
        cvBGBImg = cv2.imread(self.directoryPath + r"/" + name + ".png")
        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

        QPixmap.fromImage(qImg)
