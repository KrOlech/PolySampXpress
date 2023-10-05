from PyQt5.QtWidgets import QLabel

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog


class NoMapDialog(AbstractDialog):

    @property
    def windowName(self):
        return ""

    def __init__(self, master):
        super(NoMapDialog, self).__init__()

        self.master = master

        self.form.addRow(QLabel("No Mozaik"))

        self.form.addRow("", self.okButton)
