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

        self.patternLocator = LocateCross(self.master, "0")

        self.x0, self.yo = self.patternLocator.locateCross(True)

        self.calibrationDialog = CalibrationDialog(self)

        self.startAsyncCalibration()

        self.calibrationDialog.exec_()

    def stopCalibrationProces(self):
        self.calibrationOnGoing = False
