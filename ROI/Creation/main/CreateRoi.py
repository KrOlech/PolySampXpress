from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from ROI.Creation.Edit.RoiEdit import RoiEdit
from ROI.Creation.SimpleCreate.SimpleCreateRoi import SimpleCreateRoi


class CreateRoi(SimpleCreateRoi, RoiEdit):
    leftMouseButton = False

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
            self.savePressLocation(e)

    def mouseReleaseEvent(self, e):

        if self.__isOkToProcesEvent():
            return

        if self.editTribe:
            self.editedROI.mouseRelease(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
        else:
            self.seveReliseLocation(e)

    def mouseMoveEvent(self, e):
        match self.leftMouseButton, self.editTribe, self.mainWindow.manipulator.inMotion:
            case False, False, _:
                self.mainWindow.showROIList(e)
            case False, True, False:
                self.editedROI.cursorEdit(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, True, False:
                self.editedROI.mouseMove(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, False, False:
                self.saveTemporaryLocation(e)
                self.mainWindow.showROIList(e)

    def __isOkToProcesEvent(self):
        return self.mainWindow.manipulator.inMotion or not self.leftMouseButton
