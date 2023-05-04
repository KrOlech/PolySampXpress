from PyQt5.QtWidgets import QLabel

from src.manipulator.DialogWindow.AbstractM import AbstractDialogManipulator
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class DialogWindowMap(AbstractDialogManipulator):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.form.addRow(QLabel("Creating Map"))

    def isMapReadi(self):
        while not self.manipulator.isMapReadi:
            pass
        return

    def run(self):
        workFunWorker(self, self.isMapReadi, self.end)

    def end(self):
        self.accept()
