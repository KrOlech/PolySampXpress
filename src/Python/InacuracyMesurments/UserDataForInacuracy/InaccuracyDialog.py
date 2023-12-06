from PyQt5.QtWidgets import QRadioButton, QLabel

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class InaccuracyDialog(AbstractDialogMaster):
    __CENTER = 100, 100

    @property
    def windowName(self):
        return "Inaccuracy"

    def __init__(self, master, main, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.__CENTER[0])
        self.valueY = self.createQSpinBox(self.__CENTER[1])

        self.center = QRadioButton("Center")
        self.fromCords = QRadioButton("From Coords:")

        self.center.toggled.connect(self.centerToggle)
        self.fromCords.toggled.connect(self.fromCordsToggle)

        self.center.setChecked(True)

        self.randomMovementCount = self.createQSpinBox(5)

        self.form.addRow(QLabel("Perform Calibration:"))
        self.form.addRow(self.center)
        self.form.addRow(self.fromCords)
        self.form.addRow("X size [mm]", self.valueX)
        self.form.addRow("Y size [mm]", self.valueY)
        self.form.addRow("Random Movement Count", self.randomMovementCount)

        self.finaliseGUI()

        self.main = main

    def centerToggle(self):
        self.fromCords.setChecked(False)

        self.valueX.setDisabled(True)
        self.valueY.setDisabled(True)

    def fromCordsToggle(self):
        self.center.setChecked(False)

        self.valueX.setEnabled(True)
        self.valueY.setEnabled(True)

    def okPressed(self):
        self.accept()
        self.main.acceptEvent()

    def cancelPressed(self):
        self.accept()
        self.main.cancelEvent()
