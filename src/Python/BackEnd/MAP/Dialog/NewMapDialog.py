from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class NewMapDialog(AbstractDialogMaster):

    @property
    def windowName(self):
        return "New Mozaik"

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Create New Mozaik"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.createMapVariable = True
        super(NewMapDialog, self).okPressed()

    def cancelPressed(self):
        self.master.createMapVariable = False
        self.accept()
