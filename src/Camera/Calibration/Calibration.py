from src.Camera.Calibration.Abstract import AbstractCalibrate


class Calibrate(AbstractCalibrate):

    def __calibrate(self, manipulatorInterferes, movementFun, index, template=None):
        template, _, _ = self.extractTemplate(self.getGrayFrame()) if template is None else template

        frame_ = self.getFrame()

        self.saveFrameWithTemplate(str(index) + movementFun.__name__ +'s.png', frame_, (self.templateLocationY, self.templateLocationX))

        movementFun()
        manipulatorInterferes.waitForTarget()

        loc = self.matchTemplate(template)

        self.loger(f"locations of the template: {loc}")

        if loc is None:
            self.logWarning(f"No matched template")
            return

        delty = self.findTemplates(loc, index)

        self.loger(f"Calculated different in template location {delty}")

        if delty[not index] > 5:
            self.logWarning("To math distortion in other axis")
            return

        if index is not None:
            self.saveCalibrationResults(delty, index)

    def calibrateX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveRight, 0)

    def calibrateY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveUp, 1)

    def calibrateNegativeX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveLeft, 0)

    def calibrateNegativeY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveDown, 1)

    def calibrateXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveNegativeXY, None, template0)

    def calibrateNegativeXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveXY, None, template0)
