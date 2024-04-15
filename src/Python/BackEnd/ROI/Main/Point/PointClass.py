import cv2
from PyQt5.QtCore import QPoint, QLine

from Python.BackEnd.ROI.Main.Cursor.Cursor import Cursor
from Python.BackEnd.ROI.Main.Edit.PointEdit import PointEdit
from Python.BackEnd.ROI.Main.NameHandling.NameHandling import NameHandling


class Point(PointEdit, NameHandling, Cursor):

    def __init__(self, master, x1, y1, name, manipulatotrX, manipulatorY, pixelAbsolutValue, viue=None):
        self.loger(f"x1 = {x1},  y1 = {y1}")

        self.x0Label, self.y0Label = x1, y1

        self.pixelAbsolutValue = pixelAbsolutValue

        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        NameHandling.__init__(self, **kwargs)
        PointEdit.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame() if viue is None else viue

        self.zoom = self.master.mainWindow.zoom

        self.fileDict = self.__createFileDict()

    def __createFileDict(self) -> dict:
        x0 = self.x0 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]

        return {"absolute Pixell Values": {"x0": x0,
                                           "y0": y0},
                "absolute mm Values": {"x0": x0 / self.xOffset,
                                       "y0": y0 / self.yOffset},
                "zoom":self.zoom
                }

    def createLabelMarker(self, scalaX, scalaY):
        xlabel = self.x0Label // scalaX
        ylabel = self.y0Label // scalaY
        l1 = QLine(QPoint(xlabel + 5, ylabel),
                   QPoint(xlabel - 5, ylabel))
        l2 = QLine(QPoint(xlabel, ylabel + 5),
                   QPoint(xlabel, ylabel - 5))
        return [l1, l2]

    def saveViue(self, path):
        image = self.convertQpixmapToOpenCV(self.view)

        cv2.line(image, (self.x0Label + 5, self.y0Label), (self.x0Label - 5, self.y0Label), (0, 0, 255), 2)
        cv2.line(image, (self.x0Label, self.y0Label + 5), (self.x0Label, self.y0Label - 5), (0, 0, 255), 2)

        cv2.imwrite(path + str(self.name) + ".png", image)
