from PyQt5.QtWidgets import QLabel, QComboBox

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class XeroTreySelection(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Mark 00 Points"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.treyBox = QComboBox()
        self.treyBox.activated.connect(self.selectedTrey)

        self.treyBox.addItems([key for key in [key if key != "zoom" else None for key in  JsonHandling.loadTreyConfigurations()] if key is not None])

        self.master.sampleTreyName = self.treyBox.itemText(0)

        self.form.addRow(QLabel("Select sample Trey"), self.treyBox)

        self.form.addRow(self.okButton)

    def selectedTrey(self, treyID):
        self.master.sampleTreyName = self.treyBox.itemText(treyID)

    def okPressed(self):
        super(XeroTreySelection, self).okPressed()