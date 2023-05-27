from PyQt5.QtWidgets import QLabel

from src.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class CalibrationDialog(AbstractWindow):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel("Calibration On Going"))
        self.form.addRow(QLabel(""), self.cancelButton)

    def end(self):
        self.accept()

    def cancelPressed(self):
        self.master.stopCalibrationProces()
        self.accept()
