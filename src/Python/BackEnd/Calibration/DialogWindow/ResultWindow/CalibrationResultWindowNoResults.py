from PyQt5.QtWidgets import QLabel

from src.Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class CalibrationResultWindowNoResults(AbstractWindow):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.form.addRow(QLabel("Calibration was Stoped befor end"))

        self.form.addRow(QLabel(""), self.okButton)
