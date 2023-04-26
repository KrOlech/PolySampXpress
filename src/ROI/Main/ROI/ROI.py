from src.ROI.Main.Abstract.AbstractROI import AbstractROI
from src.ROI.Main.Cursor.Cursor import Cursor
from src.ROI.Main.Edit.ROIEdit import ROIEdit
from src.ROI.Main.NameHandling.NameHandling import NameHandling


class ROI(ROIEdit, Cursor, AbstractROI, NameHandling):

    def __init__(self, master, x1, y1, x2, y2, name='1', manipulatotrX=25.0, manipulatorY=25.0):
        self.loger(f"x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}, manipulatotrX = {manipulatotrX}, manipulatorY = {manipulatorY}")

        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "x2": x2, "y2": y2,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        ROIEdit.__init__(self, **kwargs)
        AbstractROI.__init__(self, **kwargs)
        NameHandling.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame()
