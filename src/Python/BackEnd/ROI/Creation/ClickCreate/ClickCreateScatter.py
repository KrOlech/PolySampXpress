from abc import ABCMeta

from Python.BackEnd.ROI.Creation.ClickCreate.ClickCreateAbstract import ClickCreateAbstract


class ClikcCreateScatter(ClickCreateAbstract):
    __metaclass__ = ABCMeta

    @property
    def scatter(self):
        return True

    def __savePressLocation(self, e):
        self.savePressLocation(e)

    def __seveReliseLocation(self, e):
        self.seveReliseLocation(e)

    def __saveTemporaryLocation(self, e):
        self.saveTemporaryLocation(e)

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
