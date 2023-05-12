from Camera.Calibration.DialogWindow.waitWindow.DialogWindow import CalibrationDialog
from src.Camera.Calibration.asyncFunctionality.CalibrateAsync import CalibrateAsync
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class MainCalibrate(CalibrateAsync):

    def calibrate(self, manipulatorInterferes):
        self.manipulatorInterferes = manipulatorInterferes

        self.template0 = self.extractTemplate(self.getGrayFrame())

        self.calibrationDialog = CalibrationDialog(self)

        self.startAsyncCalibration()

        self.calibrationDialog.exec_()
