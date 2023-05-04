from PyQt5.QtWidgets import QLabel

from src.manipulator.DialogWindow.Abstract import AbstractDialog


class ClosseWindow(AbstractDialog):

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

        self.finaliseOutput()

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def okPressed(self):
        self.master.testEventClose = True
        super(ClosseWindow, self).okPressed()
        self.master.close()
