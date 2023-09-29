from PyQt5.QtWidgets import QLabel, QProgressBar

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class DialogWindowMap(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel("Creating Mozaik"))

        self.pbar = QProgressBar(self)

        self.pbar.setTextVisible(False)

        self.pbar.setStyleSheet("QProgressBar"
                          "{"
                          "border: solid grey;"
                          "border-radius: 15px;"
                          " color: black; "
                          "}"
                          "QProgressBar::chunk "
                          "{background-color: # 05B8CC;"
                          "border-radius :15px;"
                          "}")

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
