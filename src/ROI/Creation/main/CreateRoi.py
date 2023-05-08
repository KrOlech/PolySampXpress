from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent

from src.ROI.Creation.ClickCreate.ClickCreateScatter import ClikcCreateScatter
from src.ROI.Creation.SimpleCreate.SimpleCreateScatter import SimpleCreateScatter
from src.ROI.Creation.ClickCreate.ClikcCreateRoi import ClikcCreateRoi
from src.ROI.Creation.Edit.RoiEdit import RoiEdit
from src.ROI.Creation.SimpleCreate.SimpleCreateRoi import SimpleCreateRoi
from src.ROI.Main.Point.Point import RoiPoint


class CreateRoi(SimpleCreateRoi, RoiEdit, RoiPoint, ClikcCreateRoi, SimpleCreateScatter, ClikcCreateScatter):
    leftMouseButton = False

    supportedModes = {
        "Classic": "_SimpleCreateRoi",
        "Point": "_RoiPoint",
        "Scatter": "_SimpleCreateScatter",
        "Clicks": "_ClikcCreateRoi",
        "Clicks Scatter": "_ClikcCreateScatter"
    }

    def eventFilter(self, source, event):
        if self.afterInitialisation:
            if event.type() == QEvent.MouseButtonPress or \
                    event.type() == QEvent.MouseButtonRelease:
                if event.button() == Qt.LeftButton:
                    self.leftMouseButton = True
                elif event.button() == Qt.RightButton:
                    self.leftMouseButton = False

        return super().eventFilter(source, event)

    def mousePressEvent(self, e):

        if self.__isOkToProcesEvent():
            return

        if self.editTribe:
            self.mousePressEventEdit(e)
        else:
            getattr(self, self.supportedModes[self.mainWindow.mode] + "__savePressLocation")(e)

    def mouseReleaseEvent(self, e):

        if self.__isOkToProcesEvent():
            return

        if self.editTribe:
            self.editedROI.mouseRelease(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
        else:
            getattr(self, self.supportedModes[self.mainWindow.mode] + "__seveReliseLocation")(e)

    def mouseMoveEvent(self, e):
        match self.leftMouseButton, self.editTribe, self.mainWindow.manipulator.inMotion:
            case False, False, _:
                self.mainWindow.showROIList(e)
            case False, True, False:
                self.editedROI.cursorEdit(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, True, False:
                self.editedROI.mouseMove(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, False, False:
                getattr(self, self.supportedModes[self.mainWindow.mode] + "__saveTemporaryLocation")(e)
                self.mainWindow.showROIList(e)

    def __isOkToProcesEvent(self):
        return self.mainWindow.manipulator.inMotion or not self.leftMouseButton
