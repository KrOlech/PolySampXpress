from PyQt5.QtWidgets import QLabel

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

        self.form.addRow(QLabel("Inaccuracy mesurment on going"))

        self.pbar = ProgresBar(self)

        self.form.addRow(self.pbar)

        self.form.addRow(self.cancelButton)

        self.cancelled = False

    def isCalibrationReadi(self):
        while self.main.InaccuracyMeasurementOnGoing:
            pass
        return

    def run(self):
        workFunWorker(self, self.isCalibrationReadi, self.end)

    def end(self):
        self.cancelled = True
        self.accept()

    def cancelPressed(self):
        self.cancelled = True
        self.loger("Inaccuracy measurement Stopped")
