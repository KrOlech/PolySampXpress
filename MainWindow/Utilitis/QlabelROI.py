from abc import ABCMeta
from abc import abstractmethod

import cv2
from PySide2 import QtGui
from PySide2.QtCore import QRect, QPoint, Qt, QEvent
from PySide2.QtGui import QPixmap, QImage, QPainter, QBrush, QColor
from PySide2.QtWidgets import QApplication

from MainWindow.RightClickMenu.Label import RightClickLabel
from MainWindow.RightClickMenu.RightClickMenu import RightMenu
from ROI.Main.ROI import ROI


class QlabelROI(RightClickLabel):
    __metaclass__ = ABCMeta
    editTribe = False
    rightClickPos = None
    rois = None
    roiNames = 0
    editedROI = None
    leftMouseButton = False
    afterInitialisation = False

    def eventFilter(self, source, event):
        if self.afterInitialisation:
            if event.type() == QEvent.MouseButtonPress or \
                    event.type() == QEvent.MouseButtonRelease:
                if event.button() == Qt.LeftButton:
                    self.leftMouseButton = True
                elif event.button() == Qt.RightButton:
                    self.leftMouseButton = False

        return super().eventFilter(source, event)

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
                qp.drawRect(rectagle.getRect(self.mainWindow.manipulator.x, self.mainWindow.manipulator.y))

        if self.pressed:
            qp.drawRect(QRect(QPoint(self.x1, self.y1), QPoint(self.x2, self.y2)))

    def mousePressEvent(self, e):
        if not self.leftMouseButton:
            return

        if self.mainWindow.manipulator.inMotion:
            return

        if self.editTribe:
            self.editedROI.mousePress(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
        else:
            self.savePressLocation(e)

    def mouseReleaseEvent(self, e):

        if self.mainWindow.manipulator.inMotion:
            return

        if not self.leftMouseButton:
            return

        if self.editTribe:
            self.editedROI.mouseRelease(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
        else:
            self.seveReliseLocation(e)

    def mouseMoveEvent(self, e):

        match (self.leftMouseButton, self.editTribe):
            case False, False:
                self.mainWindow.showROIList(e)
            case False, True:
                self.editedROI.cursorEdit(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, True:
                self.editedROI.mouseMove(e, self.mainWindow.manipulator.x, self.mainWindow.manipulator.y)
            case True, False:
                self.saveTemporaryLocation(e)
                self.mainWindow.showROIList(e)
            case _, _:
                print("error 1")

    @abstractmethod
    def savePressLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
        self.pressed = True

    @abstractmethod
    def seveReliseLocation(self, e):
        if self.pressed:
            self.x2 = e.x()
            self.y2 = e.y()

            self.ROIList.append(
                ROI(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulator.x,
                    self.mainWindow.manipulator.y))
            self.roiNames += 1

            self.pressed = False

            self.mainWindow.addROIToList()

    @abstractmethod
    def saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()

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

    def endEdit(self):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        self.editTribe = False

    def removeLable(self, ROI):
        self.mainWindow.removeROIFromList(ROI)
