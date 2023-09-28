from src.Python.BackEnd.Calibration.DialogWindow.waitWindow.DialogWindow import CalibrationDialog
from src.Python.BackEnd.Calibration.asyncFunctionality.CalibrateAsync import CalibrateAsync


class MainCalibrate(CalibrateAsync):
    calibrationOnGoing = True

    def calibrate(self, manipulatorInterferes):
        self.calibrationOnGoing = True

        self.manipulatorInterferes = manipulatorInterferes

        self.template0 = self.extractTemplate(self.getGrayFrame())

        self.calibrationDialog = CalibrationDialog(self)

        self.startAsyncCalibration()

        self.calibrationDialog.exec_()

    def stopCalibrationProces(self):
        self.calibrationOnGoing = False
