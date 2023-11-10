from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker
from src.Python.FrontEnd.Utilitis.ProgresBar import ProgresBar
from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class InaccuracyEnforcementsWindow(AbstractDialogMaster):
    @property
    def windowName(self):
        return "Inaccuracy"

    def __init__(self, master, main, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.main = main

        self.pbar = ProgresBar(self)

        self.form.addRow(self.cancelButton)

    def isCalibrationReadi(self):
        while self.main.InaccuracyMeasurementOnGoing:
            pass
        return

    def run(self):
        workFunWorker(self, self.isCalibrationReadi, self.end)

    def end(self):
        self.accept()

    def cancelPressed(self):
        self.loger("Inaccuracy measurement Stopped")
