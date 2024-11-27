from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class HomeAxisDialog(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Homing"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.createWaitingLabel()
        self.form.addRow(QLabel(""), self.cancelButton)

    def run(self):
        workFunWorker(self, self.master.homeAxis, self.end)

    def end(self):
        self.accept()

    def cancelPressed(self):
        self.master.stop()
