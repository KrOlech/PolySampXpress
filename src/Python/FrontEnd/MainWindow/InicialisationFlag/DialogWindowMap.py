from PyQt5.QtWidgets import QLabel

from src.Python.FrontEnd.Utilitis.ProgresBar import ProgresBar
from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class DialogWindowMap(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel("Creating Mozaik"))

        self.pbar = ProgresBar(self)

        self.form.addRow(self.pbar)

        self.form.addRow(self.cancelButton)

    def isMapReadi(self):
        while not self.master.isMapReadi:
            pass
        return

    def run(self):
        workFunWorker(self, self.isMapReadi, self.end)

    def end(self):
        self.accept()

    def cancelPressed(self):
        self.loger("Mozaik Creation Stopped")
        self.master.manipulatorInterferes.stop()
        self.master.mapWindowObject.mapEnd = True
        self.master.isMapReadi = True
        self.master.creatingMap = False
