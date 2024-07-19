import cv2
import numpy as np

from Python.BackEnd.Calibration.Abstract.Abstract import AbstractCalibrate


class Calibrate(AbstractCalibrate):

    def __calibrate(self, manipulatorInterferes, movementFun, index=None, template=None):
        movementFun()
        manipulatorInterferes.waitForTarget()

        #delta = self.findTemplates(loc, index)

        self.patternLocator.name = str(int(self.patternLocator.name) + 1)
        crossLocation = self.patternLocator.locateCross()

        #circles = cv2.HoughCircles(cv2.medianBlur(cv2.cvtColor(self.master.camera.getFrame(), cv2.COLOR_BGR2GRAY), 5),
        #                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
        #                           param1=100, param2=30, minRadius=0, maxRadius=0)

        #if circles is None:
        #    self.logError("Caliration failed")

        #circles = np.round(circles[0, :]).astype("int")

        #self.loger(f"Circles {circles}")

        #crossLocation = circles[0]

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
