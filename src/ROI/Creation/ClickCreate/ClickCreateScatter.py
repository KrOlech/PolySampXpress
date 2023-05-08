from abc import ABCMeta

from src.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


# toDo lern how to inhariet from ClikcCreateRoi private metods
class ClikcCreateScatter(CreateRoiAbstract):
    __metaclass__ = ABCMeta

    def __savePressLocation(self, e):
        if not (self.firstPress or self.secondPress):
            self.manipulatorXFirstPresX = self.mainWindow.manipulator.x
            self.manipulatorYFirstPresY = self.mainWindow.manipulator.y
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
            dx, dy = self.calculateOffset()
            self.x1 += dx
            self.y1 += dy

            self.createAndAddROIToList(True)

            self.pressed = False
            self.secondPress = False
            self.firstPress = False

    def __saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()
