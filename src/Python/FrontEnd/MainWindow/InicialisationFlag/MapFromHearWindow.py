from PyQt5.QtWidgets import QRadioButton

from Python.FrontEnd.MainWindow.InicialisationFlag.AbstractCreateWorkFild import AbstractCreateWorkFild
from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class MapFromHearWindow(AbstractDialogMaster, AbstractCreateWorkFild):

    @property
    def okName(self):
        return "Save and Create"

    @property
    def CancelName(self):
        return "Cancel"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.x0 = self.createQSpinBox(master.mapFromHearX)
        self.y0 = self.createQSpinBox(master.mapFromHearY)

        self.form.addRow("X size [mm]", self.x0)
        self.form.addRow("Y size [mm]", self.y0)

        self.around = QRadioButton("Around hear")
        self.fromHear = QRadioButton("From hear")

        self.around.toggled.connect(self.aroundFun)
        self.fromHear.toggled.connect(self.fromHearFun)

        self.around.setChecked(True)

        self.form.addRow(self.around, self.fromHear)

        self.finaliseGUI()

        self.master = master

    def okPressed(self):
        self.master.mapFromHearX = self.master.manipulatorInterferes.x
        self.master.mapFromHearY = self.master.manipulatorInterferes.y

        if self.x0.value() < 0.2 or self.y0.value() < 0.2:
            self.loger("Map from hear terminated size to small") #to do proper window info to User
            super().okPressed()
            return

        if self.fromHear.isChecked():
            field = [self.master.mapFromHearX, self.master.mapFromHearX + self.x0.value(), self.master.mapFromHearY,
                     self.master.mapFromHearY + self.y0.value(), "new"]
        elif self.around.isChecked():
            xHalf = self.x0.value() / 2
            yHalf = self.y0.value() / 2
            field = [self.master.mapFromHearX - xHalf, self.master.mapFromHearX + xHalf,
                     self.master.mapFromHearY - yHalf, self.master.mapFromHearY + yHalf, "new"]
        else:
            super().okPressed()
            return

        self.createWorkFild(field)

        super().okPressed()

        self.master.createMap()

    def aroundFun(self):
        self.fromHear.setChecked(False)

    def fromHearFun(self):
        self.around.setChecked(False)
