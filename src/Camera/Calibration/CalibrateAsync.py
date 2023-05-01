from src.Camera.Calibration.Calibration import Calibrate
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class CalibrateAsync(Calibrate):

    def CalibrateXStart(self):
        self.calibrateX(self.manipulatorInterferes)

    def calibrateXEnd(self):
        workFunWorker(self, self.CalibrateYStart, self.CalibrateYEnd)

    def CalibrateYStart(self):
        self.calibrateY(self.manipulatorInterferes)

    def CalibrateYEnd(self):
        workFunWorker(self, self.CalibrateXYStart, self.CalibrateXYEnd)

    def CalibrateXYStart(self):
        self.calibrateXY(self.manipulatorInterferes, self.template0)

    def CalibrateXYEnd(self):
        workFunWorker(self, self.calibrateNegativeXStart, self.calibrateNegativeXEnd)

    def calibrateNegativeXStart(self):
        self.calibrateNegativeX(self.manipulatorInterferes)

    def calibrateNegativeXEnd(self):
        workFunWorker(self, self.calibrateNegativeYStart, self.calibrateNegativeYEnd)

    def calibrateNegativeYStart(self):
        self.calibrateNegativeY(self.manipulatorInterferes)

    def calibrateNegativeYEnd(self):
        workFunWorker(self, self.calibrateNegativeXYStart, self.calibrateNegativeXYEnd)

    def calibrateNegativeXYStart(self):
        self.calibrateNegativeXY(self.manipulatorInterferes, self.template0)

    def calibrateNegativeXYEnd(self):
        self.loger("Calibration End")
        self.calibrationDialog.end()
