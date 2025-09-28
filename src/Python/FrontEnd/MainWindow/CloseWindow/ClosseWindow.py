from Python.BaseClass.Depracation.DepractionFactory import deprecated
from Python.BackEnd.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog
from PyQt6.QtWidgets import QLabel
from Python.BaseClass.Depracation.DepractionFactory import deprecated


class ClosseWindow(AbstractDialog):

    def __init__(self):
        super(ClosseWindow, self).__init__()


    @deprecated
    def resizeEvent_depracated(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    @property
    def windowName(self):
        return "mesage"

    @property
    def okName(self):
        return "Yes"

    @property
    def CancelName(self):
        return "No"

    def __init__(self, master):
        super(ClosseWindow, self).__init__()

        self.master = master

        self.form.addRow(QLabel("Czy napewno chcesz zamknac program?"))

        self.finaliseGUI()

    @deprecated
    def resizeEvent_depracated(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def okPressed(self):
        self.master.testEventClose = True
        super(ClosseWindow, self).okPressed()
        self.master.close()
