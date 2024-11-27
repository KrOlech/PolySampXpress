from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class CalibrationResultWindowNoResults(AbstractWindow):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master.manipulatorInterferes, *args, **kwargs)

        self.form.addRow(QLabel("Calibration was Stoped befor end"))

        self.form.addRow(QLabel(""), self.okButton)
