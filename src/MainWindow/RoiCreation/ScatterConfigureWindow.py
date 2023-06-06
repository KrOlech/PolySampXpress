from PyQt5.QtWidgets import QRadioButton

from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class ScatterConfigureWindow(AbstractDialogMaster):
    FULRANDOM = "Full Random"
    RANDOMMGRID = "random To Grid"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.gridSize = self.createQSpinBox(1, min=10, max=100)

        self.fullRandom = QRadioButton(self.FULRANDOM)
        self.randomToGrid = QRadioButton(self.RANDOMMGRID)

        self.fullRandom.toggled.connect(self.fullRandowFun)
        self.randomToGrid.toggled.connect(self.randomToGridFun)

        self.form.addRow(self.fullRandom, self.randomToGrid)

        self.form.addRow("Grid Size [mm]:", self.gridSize)

        self.form.addRow("", self.okButton)

        self.fullRandom.setChecked(True)
        self.gridSize.setDisabled(True)

    def fullRandowFun(self):
        self.randomToGrid.setChecked(False)
        self.gridSize.setDisabled(True)

    def randomToGridFun(self):
        self.fullRandom.setChecked(False)
        self.gridSize.setEnabled(True)

    def okPressed(self):
        if self.fullRandom.isChecked():
            self.master.scatterConfig = self.FULRANDOM
        elif self.randomToGrid.isChecked():
            self.master.scatterConfig = self.RANDOMMGRID + str(self.gridSize.value())

        super().okPressed()
