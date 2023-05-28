from abc import ABCMeta
from abc import abstractmethod

import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPoint, QLine
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor

from src.ROI.Main.Point.PointClass import Point
from src.ROI.Main.ROI.ROI import ROI
from src.MainWindow.RightClickMenu.Label import RightClickLabel
from src.MainWindow.RightClickMenu.RightClickMenu import RightMenu
from src.ROI.Creation.main.CreateRoi import CreateRoi


class QlabelROI(RightClickLabel, CreateRoi):
    __metaclass__ = ABCMeta

    rightClickPos = None
    rois = None

    afterInitialisation = False

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

    @abstractmethod
    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()

        for i, rectangle in enumerate(self.ROIList):
            rx, ry = rectangle.GetTextLocation(self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)

            if not self.mainWindow.manipulator.inMotion:
                cv2.putText(cvBGBImg, str(rectangle.name),
                            (rx, ry), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2)

        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

        frame = QPixmap.fromImage(qImg)

        return frame

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), frame := self.getFrame())

        qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

        self.setPixmap(frame)

        if not self.mainWindow.manipulator.inMotion:
            for rectagle in self.ROIList:
                if isinstance(rectagle, ROI):
                    qp.drawRect(rectagle.getMarker(self.mainWindow.manipulator.x, self.mainWindow.manipulator.y))
                elif isinstance(rectagle, Point):
                    qp.drawLines(rectagle.getMarker(self.mainWindow.manipulator.x, self.mainWindow.manipulator.y))

        if self.pressed and not self.mainWindow.creatingMap:
            if self.mainWindow.mode == "Point":
                l1 = QLine(QPoint(self.x1 + 10, self.y1), QPoint(self.x1 - 10, self.y1))
                l2 = QLine(QPoint(self.x1, self.y1 + 10), QPoint(self.x1, self.y1 - 10))
                qp.drawLines([l1, l2])
            else:
                if self.mainWindow.mode == "Clicks" or self.mainWindow.mode == "Clicks Scatter":
                    dx, dy = self.calculateOffset()
                    x1, y1 = self.x1 + dx, self.y1 + dy
                else:
                    x1, y1 = self.x1, self.y1
                qp.drawRect(QRect(QPoint(x1, y1), QPoint(self.x2, self.y2)))

    @abstractmethod
    def right_menu(self, pos):

        menu = RightMenu(self)

        self.rightClickPos = pos

        self.rois = self.checkIfInROI()

        menu.addRoiMenus(self.rois, self.editTribe)

        menu.exec_(self.mapToGlobal(pos))

    @abstractmethod
    def center(self):
        self.mainWindow.manipulator.center(self.rightClickPos.x(), self.rightClickPos.y())

    @abstractmethod
    def checkIfInROI(self):
        rois = []
        for roi in self.ROIList:
            if roi.inROI(self.rightClickPos, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y):
                rois.append(roi)
        return rois

    def removeLable(self, ROI):
        self.mainWindow.removeROIFromList(ROI)
