from PyQt5.QtWidgets import QLabel

from src.Camera.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class CalibrationDialog(AbstractWindow):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.form.addRow(QLabel("Calibration On Going"))
        self.form.addRow(QLabel(""), self.cancelButton)

    def end(self):
        self.accept()

    def cancelPressed(self):
        self.manipulator.stopCalibrationProces()
        self.accept()
