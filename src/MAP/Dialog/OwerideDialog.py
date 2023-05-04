from PyQt5.QtWidgets import QLabel

from src.manipulator.DialogWindow.Abstract import AbstractDialog


class OwerideCurrentMapDialog(AbstractDialog):

    @property
    def windowName(self):
        return "Oweride Map"

    def __init__(self, master):
        super(OwerideCurrentMapDialog, self).__init__()

        self.master = master

        self.form.addRow(QLabel("Oweride Current Map Data?"))

        self.finaliseOutput()

    def okPressed(self):
        self.master.owerideMap = True
        super(OwerideCurrentMapDialog, self).okPressed()
