from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class InsertSampleDialog(AbstractDialogMaster):

    @property
    def windowName(self):
        return 'insert Sample Dialog'

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Do You wont to insert sample Trey"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.removeSampleAsync()
        self.accept()

    def cancelPressed(self):
        self.accept()