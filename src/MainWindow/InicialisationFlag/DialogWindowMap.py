from PyQt5.QtWidgets import QLabel

from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from src.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class DialogWindowMap(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel("Creating Map"))

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
        self.loger("Map Creation Stopped")
        self.master.manipulator.stop()
        self.master.mapWindowObject.mapEnd = True
        self.master.isMapReadi = True
        self.master.creatingMap = False
