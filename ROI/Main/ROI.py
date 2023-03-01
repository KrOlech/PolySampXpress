from ROI.Main.Borders import ROIBorders
from ROI.Main.Cursor import Cursor
from ROI.Main.NameHandling import NameHandling
from ROI.Main.ROIEdit import ROIEdit


class ROI(ROIEdit, Cursor, ROIBorders, NameHandling):

    def __init__(self, master, x1, y1, x2, y2, name='1', manipulatotrX=25.0, manipulatorY=25.0):

        print(f"x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}")

        kwargs = {"master": master,
                  "name": name,
                  "x1": x1, "y1": y1,
                  "x2": x2, "y2": y2,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        super(ROI, self).__init__(**kwargs)

        self.rect = self.createRectangle()

        self.view = self.master.getFrame()
