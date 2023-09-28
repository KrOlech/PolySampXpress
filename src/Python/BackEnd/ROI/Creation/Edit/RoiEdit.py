from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from src.Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


class RoiEdit(CreateRoiAbstract):

    editTribe = False
    editedROI = None

    def endEdit(self):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        self.editTribe = False

    def mousePressEventEdit(self, e):
        self.editedROI.mousePress(e, self.mainWindow.manipulatorInterferes.x, self.mainWindow.manipulatorInterferes.y)