import cv2
from PyQt5.QtCore import QPoint, QLine

from Python.BackEnd.ROI.Main.Edit.PointEdit import PointEdit
from Python.BackEnd.ROI.Main.NameHandling.NameHandling import NameHandling
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class Point(PointEdit, NameHandling):

    def __init__(self, master, x1, y1, name, manipulatotrX, manipulatorY, pixelAbsolutValue, viue=None, zoom=None,
                 ooPoint=False, zValue=None, id=None):
        self.loger(f"x1 = {x1},  y1 = {y1}")

        self.x0Label, self.y0Label = x1, y1

        self.zValue = zValue

        self.pixelAbsolutValue = pixelAbsolutValue

        kwargs = {"master": master,
                  "name": name,
                  "id": id,
                  "x1": x1, "y1": y1,
                  "manipulatotrX": manipulatotrX,
                  "manipulatorY": manipulatorY}

        NameHandling.__init__(self, **kwargs)
        PointEdit.__init__(self, **kwargs)

        self.rect = self.createMarker()

        self.view = self.master.getFrame() if viue is None else viue

        self.zoom = zoom if zoom else self.master.mainWindow.zoom

        self.fileDict = {}

        if not ooPoint:
            self.fillFileDict()
            self.saveCenterToFileDict()

    def fillFileDict(self):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]

        self.fileDict["Pixell Values"] = {}

        self.fileDict["Pixell Values"]["x0"] = x0
        self.fileDict["Pixell Values"]["y0"] = y0

        self.xOffset, self.yOffset = JsonHandling.loadOffsetsJson(self.zoom)
        absoluteMMValuesX, absoluteMMValuesY = x0 / self.xOffset, y0 / self.yOffset

        self.fileDict["mm Values"] = {}

        self.fileDict["mm Values"]["x0"] = absoluteMMValuesX
        self.fileDict["mm Values"]["y0"] = absoluteMMValuesY

        deltaX, deltaY, zeroPointStatus = self.resolveZeroPoint()

        self.fileDict["sample mm Values"] = {}

        self.fileDict["sample mm Values"]["x0"] = absoluteMMValuesX - deltaX
        self.fileDict["sample mm Values"]["y0"] = absoluteMMValuesY - deltaY

        self.fileDict["zero Point Present"] = zeroPointStatus

        if self.zValue:
            self.fileDict["Pixell Values"] = {"x0": self.x0, "y0": self.y0, "z0": self.zValue}
            self.fileDict["zero Point Present"] = None

        self.fileDict["zoom"] = self.zoom
        self.fileDict["name"] = self.name

        self.fileDict["Type"] = "Point"

        return self.fileDict

    def createLabelMarker(self, scalaX, scalaY):
        xlabel = int(self.x0Label // scalaX)
        ylabel = int(self.y0Label // scalaY)
        l1 = QLine(QPoint(xlabel + 5, ylabel),
                   QPoint(xlabel - 5, ylabel))
        l2 = QLine(QPoint(xlabel, ylabel + 5),
                   QPoint(xlabel, ylabel - 5))
        return [l1, l2]

    def saveViue(self, path):
        image = self.convertQpixmapToOpenCV(self.view)

        cv2.line(image, (self.x0Label + 5, self.y0Label), (self.x0Label - 5, self.y0Label), (0, 0, 255), 2)
        cv2.line(image, (self.x0Label, self.y0Label + 5), (self.x0Label, self.y0Label - 5), (0, 0, 255), 2)

        cv2.imwrite(path + str(self.name) + ".png", image)

    def createViue(self):
        image = self.convertQpixmapToOpenCV(self.view)

        cv2.line(image, (self.x0Label + 5, self.y0Label), (self.x0Label - 5, self.y0Label), (0, 0, 255), 2)
        cv2.line(image, (self.x0Label, self.y0Label + 5), (self.x0Label, self.y0Label - 5), (0, 0, 255), 2)

        return image
