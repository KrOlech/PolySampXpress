import cv2
import numpy as np

from Python.BackEnd.Calibration.DialogWindow.waitWindow.DialogWindow import CalibrationDialog
from Python.BackEnd.Calibration.LocateCrossAutomatic_3_0.main import LocateCross
from Python.BackEnd.Calibration.asyncFunctionality.CalibrateAsync import CalibrateAsync


class MainCalibrate(CalibrateAsync):
    calibrationOnGoing = True

    def calibrate(self, manipulatorInterferes):
        self.calibrationOnGoing = True

        self.manipulatorInterferes = manipulatorInterferes

        self.template0 = self.extractTemplate(self.getGrayFrame())

        self.patternLocator = LocateCross(self.master,"0")

        self.x0, self.yo = self.patternLocator.locateCross(True)

        #circles = cv2.HoughCircles(cv2.medianBlur(cv2.cvtColor(self.master.camera.getFrame(), cv2.COLOR_BGR2GRAY), 5),
        #                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
        #                           param1=100, param2=30, minRadius=0, maxRadius=0)

        #if circles is None:
        #    self.logError("Caliration failed")

        #circles = np.round(circles[0, :]).astype("int")

        #self.loger(f"Circles {circles}")

        #self.x0, self.yo, _ = circles[0]

        self.calibrationDialog = CalibrationDialog(self)

        self.startAsyncCalibration()

        self.calibrationDialog.exec_()

    def stopCalibrationProces(self):
        self.calibrationOnGoing = False
