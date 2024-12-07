from abc import ABCMeta

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent

from Python.BackEnd.ROI.PointDistance.PointSpacing import PointSpacing
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Depracation.DepractionFactory import deprecated
from Python.BackEnd.ROI.Creation.ClickCreate.PointerMode import PointerMode
from Python.BackEnd.ROI.Main.Point.PointClass import Point
from Python.BackEnd.ROI.Creation.ClickCreate.ClikcCreateRoi import ClikcCreateRoi
from Python.BackEnd.ROI.Creation.Edit.RoiEdit import RoiEdit
from Python.BackEnd.ROI.Creation.SimpleCreate.SimpleCreateRoi import SimpleCreateRoi


class CreateRoi(SimpleCreateRoi,
                RoiEdit,
                ClikcCreateRoi,
                PointerMode,
                PointSpacing):
    __metaclass__ = ABCMeta

    leftMouseButton = False

    pixelAbsolutValue = [0, 0]

    __absolutZeroPoint = None

    supportedModes = {
        "Classic": "_SimpleCreateRoi",
        "Clicks": "_ClikcCreateRoi",
        "Pointer": "_PointerMode",
        "pointSpacing": "_PointSpacing"
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

        if self.mainWindow.calibratePixelsMode:
            self.logWarning("Deprecated Method of Zero Positioning")
            self.__setAbsolutZeroPositionForPixels(e)
            return

        if self.editTribe:
            self.mousePressEventEdit(e)
        else:
            getattr(self, self.supportedModes[self.mainWindow.mode] + "__savePressLocation")(e)

    def mouseReleaseEvent(self, e):

        if self.__isOkToProcesEvent():
            return

        if self.mainWindow.calibratePixelsMode:
            self.logWarning("Deprecated Method of Zero Positioning")
            self.mainWindow.calibratePixelsMode = False
            return

        if self.editTribe:
            self.editedROI.mouseRelease(e, self.mainWindow.manipulatorInterferes.x,
                                        self.mainWindow.manipulatorInterferes.y)
        else:
            getattr(self, self.supportedModes[self.mainWindow.mode] + "__seveReliseLocation")(e)

    def mouseMoveEvent(self, e):

        if self.mainWindow.creatingMap:
            return

        if self.mainWindow.calibratePixelsMode:
            self.logWarning("Deprecated Method of Zero Positioning")
            return

        else:
            match self.leftMouseButton, self.editTribe, self.mainWindow.manipulatorInterferes.inMotion:
                case False, True, False:
                    self.editedROI.cursorEdit(e, self.mainWindow.manipulatorInterferes.x,
                                              self.mainWindow.manipulatorInterferes.y)
                case True, True, False:
                    self.editedROI.mouseMove(e, self.mainWindow.manipulatorInterferes.x,
                                             self.mainWindow.manipulatorInterferes.y)
                case True, False, False:
                    getattr(self, self.supportedModes[self.mainWindow.mode] + "__saveTemporaryLocation")(e)

        # xOffset, yOffset = JsonHandling.loadOffsetsJson() #{self.x / xOffset} mm, {self.y / yOffset} mm, prawie ok brakuje wspułrzednych pkt 00

        self.mainWindow.myStatusBarMouse.setText(f"     Cursor X: {e.x()}     Y: {e.y()}")

    def toggleModeCleenUp(self):
        getattr(self, self.supportedModes[self.mainWindow.mode] + "__toggleModeCleenUp")()

    def __isOkToProcesEvent(self):
        return self.mainWindow.manipulatorInterferes.inMotion or not self.leftMouseButton or self.mainWindow.creatingMap

    @deprecated
    def __removeZeroPoint(self):
        if self.__absolutZeroPoint is not None:
            self.__absolutZeroPoint.delete()
            self.__absolutZeroPoint = None

    @deprecated
    def __newZeroPoint(self, x=None, y=None):
        x = x if x else self.pixelAbsolutValue[0]
        y = y if y else self.pixelAbsolutValue[1]
        return Point(self, x, y, "PX 0 0",
                     self.mainWindow.manipulatorInterferes.x,
                     self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue, ooPoint=True)

    def __resolvePixelAbsolutValue(self, x, y):
        ofsetX, ofsetY = JsonHandling.loadOffsetsJson(self.mainWindow.zoom)
        return x + ofsetX, y + ofsetY

    @deprecated
    def __createAndSaveZeroPoint(self, x, y):
        self.pixelAbsolutValue = self.__resolvePixelAbsolutValue(x, y)
        self.loger(f"Calculated zero point absolute Pixels: {self.pixelAbsolutValue}")

        self.__removeZeroPoint()

        self.__absolutZeroPoint = self.__newZeroPoint(x, y)

        self.mainWindow.addROIToList(self.__absolutZeroPoint)
        self.mainWindow.zeroPoint = self.__absolutZeroPoint

        self.__absolutZeroPoint.fillFileDict()

    @deprecated("old manual metode")
    def __setAbsolutZeroPositionForPixels(self, e):
        if self.leftMouseButton and not self.mainWindow.manipulatorInterferes.inMotion:
            self.__createAndSaveZeroPoint(e.x(), e.y())

            self.mainWindow.myStatusBarClick.setText("")

    @deprecated
    def setAbsolutZeroPositionForPixels(self, x, y):
        if not self.mainWindow.manipulatorInterferes.inMotion:
            self.__createAndSaveZeroPoint(x, y)
