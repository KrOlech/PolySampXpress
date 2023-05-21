from src.Calibration.DialogWindow.ResultWindow.CalibrationResultWindowNoResults import \
    CalibrationResultWindowNoResults
from src.Calibration.CalibrationFunctions.Calibration import Calibrate
from src.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker
from src.Calibration.DialogWindow.ResultWindow.CalibrationResultWindow import CalibrationResultsDialog


class CalibrateAsync(Calibrate):

    def __startAsyncProcesCalibrationProces(self, startUpFun, EndFun):
        if self.calibrationOnGoing:
            workFunWorker(self, startUpFun, EndFun)
        else:
            self.calibrateEndCallQuick()

    def startAsyncCalibration(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateXStartCall, self.calibrateXEndAndStartY)

    def calibrateXStartCall(self):
        self.calibrateX(self.manipulatorInterferes)

    def calibrateXEndAndStartY(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateYStartCall, self.calibrateYEndAndStartXY)

    def calibrateYStartCall(self):
        self.calibrateY(self.manipulatorInterferes)

    def calibrateYEndAndStartXY(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateXYStartCall, self.calibrateXYEndAndStartNegativeX)

    def calibrateXYStartCall(self):
        self.calibrateXY(self.manipulatorInterferes, self.template0)

    def calibrateXYEndAndStartNegativeX(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateNegativeXStartCall,
                                                 self.calibrateNegativeXEndAndStartNegativeY)

    def calibrateNegativeXStartCall(self):
        self.calibrateNegativeX(self.manipulatorInterferes)

    def calibrateNegativeXEndAndStartNegativeY(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateNegativeYStartCall,
                                                 self.calibrateNegativeYEndAndStartNegativeXY)

    def calibrateNegativeYStartCall(self):
        self.calibrateNegativeY(self.manipulatorInterferes)

    def calibrateNegativeYEndAndStartNegativeXY(self):
        self.__startAsyncProcesCalibrationProces(self.calibrateNegativeXYStartCall, self.calibrateEndCall)

    def calibrateNegativeXYStartCall(self):
        self.calibrateNegativeXY(self.manipulatorInterferes, self.template0)

    def calibrateEndCall(self):
        self.loger("Calibration End")
        self.calibrationDialog.end()
        CalibrationResultsDialog(self.manipulatorInterferes).exec_()

    def calibrateEndCallQuick(self):
        self.loger("Calibration End Quick")
        self.calibrationDialog.end()
        CalibrationResultWindowNoResults(self.manipulatorInterferes).exec_()
