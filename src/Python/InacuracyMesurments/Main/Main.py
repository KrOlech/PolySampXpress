from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleMasterFunWorker import workFunWorkerMaster
from Python.InacuracyMesurments.UserDataForInacuracy.InaccuracyDialog import InaccuracyDialog
from Python.InacuracyMesurments.InfoWindow.InacuracyResultWindow import InacuracyResultWindow
from Python.BackEnd.Calibration.LocateCrossAutomatic_2_0.Main import LocateCross
from Python.InacuracyMesurments.InfoWindow.InaccuracyEnforcementsWindow import InaccuracyEnforcementsWindow
from Python.BaseClass.Logger.Logger import Loger
from random import randint


class InaccuracyMeasurements(Loger):
    InaccuracyMeasurementOnGoing = True

    def __init__(self, master):
        self.master = master

    def runScript(self):
        self.loger("Start Inaccuracy Measurements")
        self.aggregateUserData()
        self.loger("End Inaccuracy Measurements")

    def aggregateUserData(self):
        self.loger("Start UserData aggregation")
        self.UserWindow = InaccuracyDialog(self.master, self)
        self.UserWindow.exec_()
        self.loger("End UserData aggregation")

    def acceptEvent(self):
        # self.master.calibrate()
        self.InaccuracyMeasurementOnGoing = True
        self.infoWindow = InaccuracyEnforcementsWindow(self.master, self)

        self.oldCrossLocation = LocateCross(self.master, "00Location").locateCross()

        workFunWorkerMaster(self, self.ranodmMovment, funEnd=self.finaliszeCalibration)

        self.infoWindow.run()
        self.infoWindow.exec_()

    def cancelEvent(self):
        self.loger("User Cancelled inaccuracy measurement")
        self.InaccuracyMeasurementOnGoing = False

    def finaliszeCalibration(self):
        if self.InaccuracyMeasurementOnGoing:
            self.newCrossLocation = LocateCross(self.master, "New00Location").locateCross()

            self.InaccuracyMeasurementOnGoing = False

            self.__showResults()

    def __showResults(self):
        self.delta = str([self.oldCrossLocation[0] - self.newCrossLocation[0],
                          self.oldCrossLocation[1] - self.newCrossLocation[1]])

        self.__displayResults()

    def __displayResults(self):
        self.loger(f"Measured delta of Cross location: {self.delta}")

        InacuracyResultWindow(self.master, self).exec_()

        self.loger("End Inaccuracy Measurements")

    @staticmethod
    def ranodmMovment(self):  # TODO better name and sepatation
        self.master.manipulatorInterferes.goToCords(self.UserWindow.valueX.value(), self.UserWindow.valueY.value())

        movmentCount = int(self.UserWindow.randomMovementCount.value())
        for i in range(movmentCount):

            if self.infoWindow.cancelled:
                self.InaccuracyMeasurementOnGoing = False
                self.cancelEvent()
                return

            x, y = randint(0, 10), randint(0, 10)

            self.master.manipulatorInterferes.goToCords(self.UserWindow.valueX.value() + x,
                                                        self.UserWindow.valueY.value() + y)
            self.master.manipulatorInterferes.waitForTarget()

            self.infoWindow.pbar.setValue(int(i / movmentCount * 100))

            self.infoWindow.pbar.update()

        self.master.manipulatorInterferes.goToCords(26, 0)
        self.master.manipulatorInterferes.waitForTarget()
