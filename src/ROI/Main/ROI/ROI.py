from PyQt5.QtCore import QRect, QPoint

from src.ROI.Main.Abstract.AbstractROI import AbstractROI
from src.ROI.Main.Cursor.Cursor import Cursor
from src.ROI.Main.Edit.ROIEdit import ROIEdit
from src.ROI.Main.NameHandling.NameHandling import NameHandling


class ROI(ROIEdit, Cursor, AbstractROI, NameHandling):

    def __init__(self, master, x1, y1, x2, y2, name, manipulatotrX, manipulatorY, pixelAbsolutValue, scatter=False):
        self.loger(
            f"x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}, manipulatotrX = {manipulatotrX}, manipulatorY = {manipulatorY}, absolutePixelValue = {pixelAbsolutValue}")

        self.x0Label, self.x1Label, self.y0Label, self.y1Label = x1, x2, y1, y2

        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "x2": x2, "y2": y2,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        ROIEdit.__init__(self, **kwargs)
        NameHandling.__init__(self, **kwargs)
        AbstractROI.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame()

        self.scatter = scatter

        self.pixelAbsolutValue = pixelAbsolutValue

    def __dict__(self) -> dict:
        return {"x0": self.x0 - self.pixelAbsolutValue[0], "x1": self.x1 - self.pixelAbsolutValue[0],
                "y0": self.y0 - self.pixelAbsolutValue[1], "y1": self.y1 - self.pixelAbsolutValue[1],
                "scatter": self.scatter}

    def createLabelMarker(self, scalaX, scalaY):
        return QRect(QPoint(self.x0Label // scalaX, self.y0Label // scalaY),
                     QPoint(self.x1Label // scalaX, self.y1Label // scalaY))