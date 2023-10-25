from PyQt5.QtWidgets import QRadioButton, QLabel

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class InaccuracyDialog(AbstractDialogMaster):
    __CENTER = 100, 100

    @property
    def windowName(self):
        return "Inaccuracy"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.__CENTER[0])
        self.valueY = self.createQSpinBox(self.__CENTER[0])

        self.center = QRadioButton("Center")
        self.fromCords = QRadioButton("From Coords:")

        self.center.toggle().connect(self.centerToggle)
        self.fromCords.toggle().connect(self.fromCordsToggle)

        self.center.setChecked(True)

        self.randomMovementCount = self.createQSpinBox(5)

        self.form.addRow(QLabel("Perform Calibration:"))
        self.form.addRow(self.center)
        self.form.addRow(self.fromCords)
        self.form.addRow("X size [mm]", self.valueX)
        self.form.addRow("Y size [mm]", self.valueY)
        self.form.addRow("Random Movement Count", self.randomMovementCount)

        self.finaliseGUI()

    def centerToggle(self):
        self.fromCords.setChecked(False)

        self.valueX.setDisabled()
        self.valueY.setDisabled()

    def fromCordsToggle(self):
        self.center.setChecked(False)

        self.valueX.setEnabled()
        self.valueY.setEnabled()

    def okPressed(self):
        self.master.referencePoint = self.__CENTER if self.center.isChecked() \
            else self.valueX.value(), self.valueY.value()

        self.master.movementCount = self.randomMovementCount.value()

        self.master.proceed()

        self.accept()
