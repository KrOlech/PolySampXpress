from src.Camera.Calibration.DialogWindow.waitWindow.DialogWindow import CalibrationDialog
from src.Camera.Calibration.asyncFunctionality.CalibrateAsync import CalibrateAsync
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


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
