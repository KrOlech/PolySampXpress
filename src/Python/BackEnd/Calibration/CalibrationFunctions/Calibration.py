import cv2
import numpy as np

from Python.BackEnd.Calibration.Abstract.Abstract import AbstractCalibrate


class Calibrate(AbstractCalibrate):

    def __calibrate(self, manipulatorInterferes, movementFun, index=None, template=None):
        movementFun()
        manipulatorInterferes.waitForTarget()

        self.patternLocator.name = str(int(self.patternLocator.name) + 1)

        crossLocation = self.patternLocator.locateCross()

        delta = self.x0 - crossLocation[0], self.yo - crossLocation[1]

        self.loger(f"Calculated different in template location {delta}")

        self.loger(f"Index {index}")

        if delta[not index] > 5:
            self.logWarning(f"To math distortion in other axis")  # todo invalidate calibration
            return

        if index is not None:
            self.saveCalibrationResults(delta, index)

    def calibrateX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveRight, 0)

    def calibrateY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveUp, 1)

    def calibrateNegativeX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveLeft, 0)

    def calibrateNegativeY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveDown, 1)

    def calibrateXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveNegativeXY, template=template0)

    def calibrateNegativeXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveXY, template=template0)
