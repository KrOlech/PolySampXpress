import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from os import chdir, curdir

from src.Python.BackEnd.ROI.Main.Point.Point import Point
from src.Python.BackEnd.ROI.Main.ROI.ROI import ROI
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class LoadRoiList(JsonHandling):

    def __init__(self, master):
        self.master = master

        self.absolutPxX = self.master.cameraView.pixelAbsolutValue[0]
        self.absolutPxY = self.master.cameraView.pixelAbsolutValue[1]

    def load(self):
        curentDirectory = curdir
        filePath, _ = QFileDialog.getOpenFileName(self.master, "Select file with Roi List", "",
                                                  "Json Files (*.json)")

        directoryPath = filePath[:filePath.rfind(r"/")]

        self.loger(filePath)

        data = JsonHandling.readFileRow(filePath)
        try:
            for name, values in data.items():
                cords = values['absolute Pixell Values']

                self.loger(directoryPath + r"/" + name)
                cvBGBImg = cv2.imread(directoryPath + r"/" + name + ".png")
                qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

                img = QPixmap.fromImage(qImg)

                if len(cords) == 4:
                    roi = ROI(self.master.cameraView, cords["x0"] + self.absolutPxX, cords["y0"] + self.absolutPxY,
                              cords["x1"] + self.absolutPxX, cords["y1"] + self.absolutPxY, name, 0,
                              0, self.master.cameraView.pixelAbsolutValue, scatter=values["scatter"], viue=img)

                elif len(cords) == 2:
                    roi = Point(self.master.cameraView, cords["x0"] + self.absolutPxX, cords["y0"] + self.absolutPxY,
                                name, 0,
                                0, self.master.cameraView.pixelAbsolutValue, viue=img)

                self.master.cameraView.ROIList.append(roi)

                self.master.addROIToList()

            self.master.cameraView.roiNames = len(self.master.cameraView.ROIList)

        except KeyError as e:
            self.logError(e)
            self.logError("Incorect Fille for Roi List Recreation")
            # toDo proper errore as a mesageWindow
        finally:
            chdir(curentDirectory)
