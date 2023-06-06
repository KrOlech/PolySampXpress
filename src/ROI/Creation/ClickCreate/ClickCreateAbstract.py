from abc import ABCMeta, abstractmethod

from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


class ClickCreateAbstract(CreateRoiAbstract):
    __metaclass__ = ABCMeta

    firstPress = False
    secondPress = False
    manipulatorXFP = None
    manipulatorXFirstPresX = None
    manipulatorYFirstPresY = None

    xOffset, yOffset = JsonHandling.loadOffsetsJson()

    @property
    @abstractmethod
    def scatter(self):
        return None

    def savePressLocation(self, e):
        if not (self.firstPress or self.secondPress):
            self.manipulatorXFirstPresX = self.mainWindow.manipulatorInterferes.x
            self.manipulatorYFirstPresY = self.mainWindow.manipulatorInterferes.y
            self.x1 = e.x()
            self.y1 = e.y()
            self.x2 = e.x()
            self.y2 = e.y()
            self.firstPress = True
            self.pressed = True
            self.mainWindow.myStatusBarClick.setText("First Corner Mark")
        elif self.firstPress and not self.secondPress:
            self.x2 = e.x()
            self.y2 = e.y()
            self.firstPress = False
            self.secondPress = True

    def seveReliseLocation(self, e):
        if self.secondPress:
            self.x2 = e.x()
            self.y2 = e.y()
            dx, dy = self.calculateOffset()
            self.x1 += dx
            self.y1 += dy

            self.createAndAddROIToList(self.scatter)

            self.pressed = False
            self.secondPress = False
            self.firstPress = False
            self.mainWindow.myStatusBarClick.setText("Click Mode")

    def saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()

    def calculateOffset(self):
        return int((self.manipulatorXFirstPresX - self.mainWindow.manipulatorInterferes.x) * self.xOffset), int(
            (self.manipulatorYFirstPresY - self.mainWindow.manipulatorInterferes.y) * self.yOffset)
