from Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


class PointerMode(CreateRoiAbstract):
    pressed = False

    def __savePressLocation(self, e):
        self.pressed = True

    def __seveReliseLocation(self, e):
        self.pressed = False

    def __saveTemporaryLocation(self, e):
        if self.pressed:
            self.mainWindow.manipulatorInterferes.center(e.x(), e.y(), self.mainWindow.zoom)

    def __toggleModeCleenUp(self):
        self.pressed = False
