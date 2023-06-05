from PyQt5.QtWidgets import QRadioButton

from src.MainWindow.InicialisationFlag.AbstractCreateWorkFild import AbstractCreateWorkFild
from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class MapFromHearWindow(AbstractDialogMaster, AbstractCreateWorkFild):

    @property
    def okName(self):
        return "Save and select"

    @property
    def CancelName(self):
        return "Cancel"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.x0 = self.createQSpinBox(0)
        self.y0 = self.createQSpinBox(0)

        self.form.addRow("X size [mm]", self.x0)
        self.form.addRow("Y size [mm]", self.y0)

        self.around = QRadioButton("Around hear")
        self.fromHear = QRadioButton("From hear")

        self.around.toggled.connect(self.aroundFun)
        self.fromHear.toggled.connect(self.fromHearFun)

        self.around.setChecked(True)

        self.form.addRow(self.around, self.fromHear)

        self.finaliseOutput()

    def okPressed(self):
        manipulatorX = self.master.manipulator.x
        manipulatorY = self.master.manipulator.y

        if self.fromHear.isChecked():
            field = [manipulatorX, manipulatorX + self.x0.value(), manipulatorY, manipulatorY + self.y0.value(), "new"]
        elif self.around.isChecked():
            xHalf = self.x0.value() / 2
            yHalf = self.y0.value() / 2
            field = [manipulatorX - xHalf, manipulatorX + xHalf, manipulatorY - yHalf, manipulatorY + yHalf, "new"]
        else:
            return

        self.createWorkFild(field)

        super().okPressed()

        self.master.createMap()

    def aroundFun(self):
        self.fromHear.setChecked(False)

    def fromHearFun(self):
        self.around.setChecked(False)
