from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class RemoveSampleDialog(AbstractDialogMaster):
    @property
    def windowName(self):
        return 'Sample access position'

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Do You wont to save ROI list before Go to Sample access position"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.saveListOfROI()
        self.accept()

    def cancelPressed(self):
        self.accept()
