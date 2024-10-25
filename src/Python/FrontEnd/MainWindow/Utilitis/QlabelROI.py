from abc import ABCMeta
from abc import abstractmethod

from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPoint, QLine
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor, QFont

from Python.BackEnd.ROI.Main.Line.Line import Line
from Python.BackEnd.ROI.Main.Point.Point import Point
from Python.BackEnd.ROI.Main.ROI.ROI import ROI
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.FrontEnd.MainWindow.RightClickMenu.Label import RightClickLabel
from Python.FrontEnd.MainWindow.RightClickMenu.RightClickMenu import RightMenu
from Python.BackEnd.ROI.Creation.main.CreateRoi import CreateRoi


class QlabelROI(RightClickLabel, CreateRoi):
    __metaclass__ = ABCMeta

    rightClickPos = None
    rois = None

    afterInitialisation = False

    rulerHeightOffset = 50
    rulerWidthOffset = 10

    def __init__(self, mainWindow, *args, **kwargs):
        super(QlabelROI, self).__init__(*args, **kwargs)

        self.ROIList = []

        self.mainWindow = mainWindow

        self.setPixmap(self.getFrame())

        self.pressed = False

        self.installEventFilter(self)

        cvBGBImg = self.mainWindow.camera.getFrame()

        self.setMaximumSize(cvBGBImg.shape[1], cvBGBImg.shape[0])
        self.setMinimumSize(cvBGBImg.shape[1], cvBGBImg.shape[0])

        self.setMouseTracking(True)

        self.zoomsLengths = self.__createZoomLengths()

        self.cen = self.__createCenter()

    @abstractmethod
    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()

        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

        frame = QPixmap.fromImage(qImg)

        return frame

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), frame := self.getFrame())

        qp.setFont(QFont("Arial", 24))

        pen = qp.pen()
        pen.setColor(QColor("blue"))
        qp.setPen(pen)

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

        self.setPixmap(frame)

        if not self.mainWindow.manipulatorInterferes.inMotion:
            self.__drawRectangles(qp)

        if self.pressed and not self.mainWindow.creatingMap:
            self.__drawCurrentlyMarkedRectangles(qp)

        self.__drawRuler(qp)

        self.__drawCenter(qp)

    def __createCenter(self):
        cx = self.size().height() // 2
        cy = self.size().width() // 2
        l1 = QPoint(cy, cx + 5), QPoint(cy, cx - 5)
        l2 = QPoint(cy + 5, cx), QPoint(cy - 5, cx)
        return l1, l2

    def __drawCenter(self, qp):
        pen = qp.pen()
        pen.setWidth(1)
        pen.setColor(QColor("blue"))
        qp.setPen(pen)

        qp.drawLine(*self.cen[0])
        qp.drawLine(*self.cen[1])

    def __drawRectangles(self, qp):
        for i, rectangle in enumerate(self.ROIList):

            if rectangle.zoom != self.mainWindow.zoom:
                continue

            self.__drawRectangleName(qp, rectangle)

            self.__drawRectangleMarker(qp, rectangle)

    def __drawRectangleName(self, qp, rectangle):
        rx, ry = rectangle.GetTextLocation(self.mainWindow.manipulatorInterferes.x,
                                           self.mainWindow.manipulatorInterferes.y)
        qp.drawText(rx, ry, str(rectangle.name))

    def __drawRectangleMarker(self, qp, rectangle):
        if isinstance(rectangle, ROI):
            qp.drawRect(rectangle.getMarker(self.mainWindow.manipulatorInterferes.x,
                                            self.mainWindow.manipulatorInterferes.y))
        elif isinstance(rectangle, Point):
            qp.drawLines(rectangle.getMarker(self.mainWindow.manipulatorInterferes.x,
                                             self.mainWindow.manipulatorInterferes.y))
        elif isinstance(rectangle, Line):
            qp.drawLine(rectangle.getMarker(self.mainWindow.manipulatorInterferes.x,
                                             self.mainWindow.manipulatorInterferes.y))

    def __drawCurrentlyMarkedRectangles(self, qp):
        if self.mainWindow.mode == "Point":
            l1 = QLine(QPoint(self.x1 + 10, self.y1), QPoint(self.x1 - 10, self.y1))
            l2 = QLine(QPoint(self.x1, self.y1 + 10), QPoint(self.x1, self.y1 - 10))
            qp.drawLines([l1, l2])
        elif self.mainWindow.mode == "pointSpacing":
            dx, dy = self.calculateOffset()
            x1, y1 = self.x1 + dx, self.y1 + dy
            qp.drawLine(QLine(QPoint(x1, y1), QPoint(self.x2, self.y2)))
        else:
            if self.mainWindow.mode == "Clicks" or self.mainWindow.mode == "Clicks Scatter":
                dx, dy = self.calculateOffset()
                x1, y1 = self.x1 + dx, self.y1 + dy
            else:
                x1, y1 = self.x1, self.y1
            qp.drawRect(QRect(QPoint(x1, y1), QPoint(self.x2, self.y2)))

    def __drawRuler(self, qp):

        pen = qp.pen()
        pen.setWidth(3)
        pen.setColor(QColor(200, 10, 10, 200))
        qp.setPen(pen)

        zoomsNames = {0: "1 mm", 1: "1 mm", 2: "0.5 mm", 3: "0.5 mm", 4: "0.2 mm", 5: "0.2 mm", 6: "0.2 mm",
                      7: "0.1 mm",
                      8: "0.1 mm", 9: "0.1 mm", 10: "0.1 mm"}

        length = self.zoomsLengths[int(self.mainWindow.zoom)]

        rulerHeight = self.size().height() - self.rulerHeightOffset

        rulerOffsetLength = self.rulerWidthOffset + length

        rulerHalfOffsetLength = rulerOffsetLength // 2

        rulerQuoterOffsetLength = rulerOffsetLength // 4

        p00 = QPoint(self.rulerWidthOffset, rulerHeight)

        lineHeight = self.size().height() - 60

        qp.drawLines(p00, QPoint(rulerOffsetLength, rulerHeight))

        qp.drawLines(p00,
                     QPoint(self.rulerWidthOffset, lineHeight))
        qp.drawLines(QPoint(rulerOffsetLength, rulerHeight),
                     QPoint(rulerOffsetLength, lineHeight))

        qp.drawLines(QPoint(rulerHalfOffsetLength, rulerHeight),
                     QPoint(rulerHalfOffsetLength, lineHeight))

        qp.drawLines(QPoint(rulerQuoterOffsetLength, rulerHeight),
                     QPoint(rulerQuoterOffsetLength, lineHeight + 5))
        qp.drawLines(QPoint(rulerHalfOffsetLength + length // 4, rulerHeight),
                     QPoint(rulerHalfOffsetLength + length // 4, lineHeight + 5))

        qp.drawText(length + 20, rulerHeight, zoomsNames[int(self.mainWindow.zoom)])

    def __createZoomLengths(self):
        zoomsLengths = {0: 100, 1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}
        realLengthsMM = [1, 1, 0.5, 0.5, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1]

        for zoom, length in zip(zoomsLengths, realLengthsMM):
            x, y = JsonHandling.loadOffsetsJson(zoom)
            zoomsLengths[zoom] = int(y * length)

        return zoomsLengths

    @abstractmethod
    def right_menu(self, pos):

        menu = RightMenu(self)

        self.rightClickPos = pos

        self.rois = self.checkIfInROI()

        menu.addRoiMenus(self.rois, self.editTribe)

        menu.exec_(self.mapToGlobal(pos))

    @abstractmethod
    def center(self):
        self.mainWindow.manipulatorInterferes.center(self.rightClickPos.x(),
                                                     self.rightClickPos.y(),
                                                     self.mainWindow.zoom)

    @abstractmethod
    def checkIfInROI(self):
        rois = []
        for roi in self.ROIList:
            if roi.inROI(self.rightClickPos, self.mainWindow.manipulatorInterferes.x,
                         self.mainWindow.manipulatorInterferes.y):
                rois.append(roi)
        return rois

    def removeLable(self, ROI):
        self.mainWindow.removeROIFromList(ROI)
