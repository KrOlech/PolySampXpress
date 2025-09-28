from Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract

from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class PointSpacing(CreateRoiAbstract):
    firstPress = False
    secondPress = False
    manipulatorXFP = None
    manipulatorXFirstPresX = None
    manipulatorYFirstPresY = None

    xOffset, yOffset = JsonHandling.loadOffsetsJson()

    def __savePressLocation(self, e):
        if not (self.firstPress or self.secondPress):
            self.manipulatorXFirstPresX = self.mainWindow.manipulatorInterferes.x
            self.manipulatorYFirstPresY = self.mainWindow.manipulatorInterferes.y
            self.x1 = int(e.position().x())
            self.y1 = int(e.position().y())
            self.x2 = int(e.position().x())
            self.y2 = int(e.position().y())
            self.firstPress = True
            self.pressed = True
        elif self.firstPress and not self.secondPress:
            self.x2 = int(e.position().x())
            self.y2 = int(e.position().y())
            self.firstPress = False
            self.secondPress = True

    def __seveReliseLocation(self, e):
        if self.secondPress:
            self.x2 = int(e.position().x())
            self.y2 = int(e.position().y())
            dx, dy = self.calculateOffset()
            self.x1 += dx
            self.y1 += dy

            self.createAndAddLineToList()

            self.pressed = False
            self.secondPress = False
            self.firstPress = False

    def __saveTemporaryLocation(self, e):
        self.x2 = int(e.position().x())
        self.y2 = int(e.position().y())

    def calculateOffset(self):
        return int((self.manipulatorXFirstPresX - self.mainWindow.manipulatorInterferes.x) * self.xOffset), int(
            (self.manipulatorYFirstPresY - self.mainWindow.manipulatorInterferes.y) * self.yOffset)

    def __toggleModeCleenUp(self):
        self.firstPress = False
        self.secondPress = False
        self.manipulatorXFP = None
        self.manipulatorXFirstPresX = None
        self.manipulatorYFirstPresY = None

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
