import asyncio

from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.SaveRoiWindow import SaveRoiWindow
from Python.Utilitis.GenericProgressClass import GenericProgressClass


class RemoveSampleDialog(AbstractDialogMaster):
    @property
    def windowName(self):
        return 'Sample access position'

    @property
    def CancelName(self):
        return "No"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(QLabel("Do You wont to save ROI list and clear it before Going to Sample access position"))

        self.finaliseGUI()

    def okPressed(self):
        self.accept()
        savingWindow = SaveRoiWindow("Saving ROI's",
                                      self.master.saveListOfROI, 200, self)
        savingWindow.run()
        savingWindow.exec_()

    def clearRoiList(self):
        clearingWindow = GenericProgressClass("Clearing ROI's",
                                      self.master.clearListOfRoi, 200, self)
        clearingWindow.run()
        clearingWindow.exec_()

    def cancelPressed(self):
        self.accept()
