import cv2
from PyQt5.QtCore import QRect, QPoint

from Python.BackEnd.ROI.Main.Abstract.AbstractROI import AbstractROI
from Python.BackEnd.ROI.Main.Edit.ROIEdit import ROIEdit
from Python.BackEnd.ROI.Main.NameHandling.NameHandling import NameHandling
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class ROI(ROIEdit, AbstractROI, NameHandling):

    def __init__(self, master, x1, y1, x2, y2, name, manipulatotrX, manipulatorY, pixelAbsolutValue, scatter=False,
                 viue=None, zoom=None, id=None):
        self.loger(
            f"x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}, manipulatotrX = {manipulatotrX}, manipulatorY = {manipulatorY}, absolutePixelValue = {pixelAbsolutValue}")

        self.x0Label, self.x1Label, self.y0Label, self.y1Label = x1, x2, y1, y2

        self.pixelAbsolutValue = pixelAbsolutValue

        kwargs = {"master": master,
                  "name": name,
                  "id": id,
                  "x1": x1, "y1": y1,
                  "x2": x2, "y2": y2,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        ROIEdit.__init__(self, **kwargs)
        NameHandling.__init__(self, **kwargs)
        AbstractROI.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame() if viue is None else viue

        self.scatter = scatter

        self.zoom = zoom if zoom else self.master.mainWindow.zoom

        self.fileDict = {}
        self.fillFileDict()
        self.saveCenterToFileDict()

    def fillFileDict(self):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]
        self.fileDict["Pixell Values"] = {"x0": x0, "x1": x1, "y0": y0, "y1": y1}

        xOffset, yOffset = JsonHandling.loadOffsetsJson(self.zoom)
        absoluteMMValuesX0, absoluteMMValuesX1, = x0 / xOffset, x1 / xOffset,
        absoluteMMValuesY0, absoluteMMValuesY1 = y0 / yOffset, y1 / yOffset
        self.fileDict["mm Values"] = {"x0": absoluteMMValuesX0, "x1": absoluteMMValuesX1,
                                      "y0": absoluteMMValuesY0, "y1": absoluteMMValuesY1}

        deltaX, deltaY, zeroPointStatus = self.resolveZeroPoint()
        self.fileDict["sample mm Values"] = {"x0": absoluteMMValuesX0 - deltaX, "x1": absoluteMMValuesX1 - deltaX,
                                             "y0": absoluteMMValuesY0 - deltaY, "y1": absoluteMMValuesY1 - deltaY}
        self.fileDict["zero Point Present"] = zeroPointStatus

        self.fileDict["zoom"] = self.zoom
        self.fileDict["scatter"] = self.scatter
        self.fileDict["name"] = self.name

        return self.fileDict

    def createLabelMarker(self, scalaX, scalaY):
        return QRect(QPoint(self.x0Label // scalaX, self.y0Label // scalaY),
                     QPoint(self.x1Label // scalaX, self.y1Label // scalaY))

    def saveViue(self, path):
        cv2.imwrite(path + str(self.name) + ".png", self.createViue())

    def createViue(self):
        image = self.convertQpixmapToOpenCV(self.view)

        cv2.rectangle(image, [self.x0Label, self.y0Label], [self.x1Label, self.y1Label], (0, 0, 255), 2)

        return image
