from src.ROI.Main.Cursor.Cursor import Cursor
from src.ROI.Main.Edit.PointEdit import PointEdit
from src.ROI.Main.NameHandling.NameHandling import NameHandling


class Point(PointEdit, NameHandling, Cursor):

    def __init__(self, master, x1, y1, name, manipulatotrX, manipulatorY, pixelAbsolutValue):
        self.loger(f"x1 = {x1},  y1 = {y1}")

        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        PointEdit.__init__(self, **kwargs)
        NameHandling.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame()

        self.pixelAbsolutValue = pixelAbsolutValue

    def __dict__(self) -> dict:
        return {"x0": self.x0 - self.pixelAbsolutValue[0], "y0": self.y0 - self.pixelAbsolutValue[1]}
