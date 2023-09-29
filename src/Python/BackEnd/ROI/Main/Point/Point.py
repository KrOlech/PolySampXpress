from src.Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract
from src.Python.BackEnd.ROI.Main.Point.PointClass import Point


class RoiPoint(CreateRoiAbstract):

    def __savePressLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
        self.pressed = True

    def __seveReliseLocation(self, e):
        if self.pressed:
            self.x1 = e.x()
            self.y1 = e.y()
            self.x2 = e.x()
            self.y2 = e.y()

            self.ROIList.append(
                Point(self, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulatorInterferes.x,
                      self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue))
            self.roiNames += 1

            self.pressed = False

            self.mainWindow.addROIToList()

    def __saveTemporaryLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
