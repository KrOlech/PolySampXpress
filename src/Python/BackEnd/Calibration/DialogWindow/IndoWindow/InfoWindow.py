from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class CalibrationInfoWindow(AbstractWindow):


    @property
    def CancelName(self):
        return "No"

    @property
    def okName(self):
        return "Yes"

    def __init__(self, master):
        super(CalibrationInfoWindow, self).__init__(master)

        self.master = master

        self.form.addRow(QLabel("Wuld you like to perform Calibration??"))

        self.finaliseGUI()

    def okPressed(self):
        super(CalibrationInfoWindow, self).okPressed()
        self.master.performCalibration()

