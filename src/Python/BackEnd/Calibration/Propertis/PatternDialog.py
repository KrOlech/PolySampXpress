from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class PatternDialog(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.x = self.createQSpinBox(0, max=2000)
        self.y = self.createQSpinBox(0, max=2000)
        self.x1 = self.createQSpinBox(0, max=2000)
        self.y1 = self.createQSpinBox(0, max=2000)

        self.form.addRow(QLabel("x_1"), self.x)
        self.form.addRow(QLabel("y_1"), self.y)
        self.form.addRow(QLabel("x_2"), self.x1)
        self.form.addRow(QLabel("y_2"), self.y1)

        self.finaliseGUI()

    def okPressed(self):
        self.master.dataPrivaided()
