from abc import ABCMeta

from src.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


# toDo lern how to inhariet from SimpleCreateRoi private metods
class SimpleCreateScatter(CreateRoiAbstract):
    __metaclass__ = ABCMeta

    def __savePressLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
        self.pressed = True

    def __seveReliseLocation(self, e):
        if self.pressed:
            self.x2 = e.x()
            self.y2 = e.y()

            self.createAndAddROIToList(self.mainWindow.scatterConfig)

            self.pressed = False

    def __saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()
