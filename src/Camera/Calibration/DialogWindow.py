from PyQt5.QtWidgets import QLabel

from src.manipulator.DialogWindow.Abstract import AbstractDialog


class CalibrationDialog(AbstractDialog):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.form.addRow(QLabel("Calibration On Going"))

    def end(self):
        self.accept()
