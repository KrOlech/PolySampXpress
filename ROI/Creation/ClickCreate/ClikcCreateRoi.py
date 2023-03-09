from ROI.Creation.Abstract.Abstract import CreateRoiAbstract
from ROI.Main.ROI.ROI import ROI


class ClikcCreateRoi(CreateRoiAbstract):

    firstPress = False
    secondPress = False

    def __savePressLocation(self, e):
        if not(self.firstPress or self.secondPress):
            self.x1 = e.x()
            self.y1 = e.y()
            self.x2 = e.x()
            self.y2 = e.y()
            self.firstPress = True
            self.pressed = True
        elif self.firstPress and not self.secondPress:
            self.x2 = e.x()
            self.y2 = e.y()
            self.firstPress = False
            self.secondPress = True

    def __seveReliseLocation(self, e):
        if self.secondPress:
            self.x2 = e.x()
            self.y2 = e.y()

            self.ROIList.append(
                ROI(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulator.x,
                    self.mainWindow.manipulator.y))
            self.roiNames += 1

            self.pressed = False
            self.secondPress = False
            self.firstPress = False

            self.mainWindow.addROIToList()

    def __saveTemporaryLocation(self, e):
        if self.firstPress == True:
            self.x2 = e.x()
            self.y2 = e.y()