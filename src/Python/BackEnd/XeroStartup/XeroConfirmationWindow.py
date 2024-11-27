from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster

class XeroConfirmationWindow(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Mark 00 Points"

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Remember To turn on correct lighting"))
        self.form.addRow(QLabel("Do you  wont to mark 00 points"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.createMapVariable = True
        super(XeroConfirmationWindow, self).okPressed()

    def cancelPressed(self):
        self.master.createMapVariable = False
        self.accept()