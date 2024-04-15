import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from os import chdir, curdir

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
                                                  "Json Files (*.json)")
        return filePath, curdir

    def loadImage(self, name):
        self.loger(self.directoryPath + r"/" + name)
        cvBGBImg = cv2.imread(self.directoryPath + r"/" + name + ".png")
        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

        QPixmap.fromImage(qImg)
