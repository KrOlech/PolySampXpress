from PyQt5.QtCore import QPoint, QLine

from src.ROI.Main.Cursor.Cursor import Cursor
from src.ROI.Main.Edit.PointEdit import PointEdit
from src.ROI.Main.NameHandling.NameHandling import NameHandling


class Point(PointEdit, NameHandling, Cursor):

    def __init__(self, master, x1, y1, name, manipulatotrX, manipulatorY, pixelAbsolutValue):
        self.loger(f"x1 = {x1},  y1 = {y1}")
        self.x0Label, self.y0Label = x1, y1
        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        NameHandling.__init__(self, **kwargs)
        PointEdit.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame()

        self.pixelAbsolutValue = pixelAbsolutValue

    def __dict__(self) -> dict:
        return {"x0": self.x0 - self.pixelAbsolutValue[0], "y0": self.y0 - self.pixelAbsolutValue[1]}

    def createLabelMarker(self, scalaX, scalaY):
        xlabel = self.x0Label // scalaX
        ylabel = self.y0Label // scalaY
        l1 = QLine(QPoint(xlabel + 5, ylabel),
                   QPoint(xlabel - 5, ylabel))
        l2 = QLine(QPoint(xlabel, ylabel + 5),
                   QPoint(xlabel, ylabel - 5))
        return [l1, l2]
