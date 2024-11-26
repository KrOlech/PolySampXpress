from Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


class PointerMode(CreateRoiAbstract):
    pressed = False

    def __savePressLocation(self, e):
        #self.pressed = True
        self.mainWindow.manipulatorInterferes.center(e.x(), e.y(), self.mainWindow.zoom)

    def __seveReliseLocation(self, e):
        pass
        #self.mainWindow.manipulatorInterferes.center(e.x(), e.y(), self.mainWindow.zoom)
        #self.pressed = False

    def __saveTemporaryLocation(self, e):
        pass
        #if self.pressed:
        #    self.mainWindow.manipulatorInterferes.center(e.x(), e.y(), self.mainWindow.zoom)

    def __toggleModeCleenUp(self):
        self.pressed = False
