from PyQt5.QtWidgets import QLabel

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog


class OwerideCurrentMapDialog(AbstractDialog):

    @property
    def windowName(self):
        return "Oweride Mozaik"

    def __init__(self, master):
        super(OwerideCurrentMapDialog, self).__init__()

        self.master = master

        self.form.addRow(QLabel("Oweride Current Mozaik Data?"))

        self.finaliseGUI()

    def okPressed(self):
        self.master.owerideMap = True
        super(OwerideCurrentMapDialog, self).okPressed()
