from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class RemoveSampleDialog(AbstractDialogMaster):
    @property
    def windowName(self):
        return 'Remove Sample Dialog'

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Do You wont to save ROI list before removing sample Trey"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.saveListOfROI()

    def cancelPressed(self):
        self.accept()
