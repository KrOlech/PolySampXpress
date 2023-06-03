from PyQt5.QtWidgets import QRadioButton

from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class ScatterConfigureWindow(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.gridSize = self.createQSpinBox(1, min=10, max=100)

        self.fullRandom = QRadioButton("Full Random")
        self.fullRandom.toggled.connect(self.fullRandowFun)

        self.randomToGrid = QRadioButton("random To Grid")
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
        # toDo save selected configuration
        super().okPressed()
