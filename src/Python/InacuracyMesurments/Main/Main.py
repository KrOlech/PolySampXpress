from src.Python.InacuracyMesurments.UserDataForInacuracy.InaccuracyDialog import InaccuracyDialog
from src.Python.InacuracyMesurments.InfoWindow.InacuracyResultWindow import InacuracyResultWindow
from src.Python.BackEnd.Calibration.LocateCrossAutomatic_2_0.Main import LocateCross
from src.Python.InacuracyMesurments.InfoWindow.InaccuracyEnforcementsWindow import InaccuracyEnforcementsWindow
from src.Python.BaseClass.Logger.Logger import Loger
from random import randint


class InaccuracyMeasurements(Loger):
    InaccuracyMeasurementOnGoing = True

    def __init__(self, master):
        self.master = master

    def runScript(self):
        self.loger("Start Inaccuracy Measurements")

        self.UserWindow = InaccuracyDialog(self.master)
        self.UserWindow.exec_()

        # self.master.calibrate()
        self.InaccuracyMeasurementOnGoing = True
        self.infoWindow = InaccuracyEnforcementsWindow(self.master, self)

        self.infoWindow.run()

        self.oldCrossLocation = LocateCross(self.master, "00Location").locateCross()

        self.master.manipulatorInterferes.goToCords(self.UserWindow.valueX.value(), self.UserWindow.valueY.value())

        self.__ranodmMovment()

        self.master.manipulatorInterferes.goToCords(26, 0)

        self.newCrossLocation = LocateCross(self.master, "New00Location").locateCross()

        self.InaccuracyMeasurementOnGoing = False

        self.infoWindow.exec_()

        self.delta = str([self.oldCrossLocation[0] - self.newCrossLocation[0],
                          self.oldCrossLocation[1] - self.newCrossLocation[1]])

        self.__displayResults()

        self.loger("End Inaccuracy Measurements")

    def __displayResults(self):
        self.loger(f"Measured delta of Cross location: {self.delta}")

        InacuracyResultWindow(self.master, self).exec_()

    def __ranodmMovment(self):
        movmentCount = int(self.UserWindow.randomMovementCount.value())
        for i in range(movmentCount):
            x, y = randint(0, 10), randint(0, 10)

            self.master.manipulatorInterferes.goToCords(self.UserWindow.valueX.value() + x,
                                                        self.UserWindow.valueY.value() + y)
            self.master.manipulatorInterferes.waitForTarget()

            self.infoWindow.pbar.setValue(int(i / movmentCount * 100))
