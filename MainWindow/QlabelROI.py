import cv2
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPoint, Qt, QEvent
from abc import abstractmethod
from abc import ABCMeta
from MainWindow.MainWindowCameraGUI.CameraGUI import CameraGUI
from RightClickMenu import RightMenu, RightClickLabel
from utilitis.Abstract import abstractmetod
from ROI.ROI import ROI


class QlabelROI(RightClickLabel):
    __metaclass__ = ABCMeta
    editTrybe = False
    rightClickPos = None
    rois = None
    roinames = 0
    editedROI = None
    leftMouseButton = False

    def eventFilter(self, source, event):
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

        self.presed = False

        self.installEventFilter(self)

        cvBGBImg = self.mainWindow.camera.getFrame()

        self.setMaximumSize(cvBGBImg.shape[1], cvBGBImg.shape[0])
        self.setMinimumSize(cvBGBImg.shape[1], cvBGBImg.shape[0])

    @abstractmethod
    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()
        for i, rectangle in enumerate(self.ROIList):
            rx, ry = rectangle.pobierz_lokacje_tekstu()

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

        for rectagle in self.ROIList:
            qp.drawRect(rectagle.rect)

        if self.presed:
            qp.drawRect(QRect(QPoint(self.x1, self.y1), QPoint(self.x2, self.y2)))

    def mousePressEvent(self, e):
        if not self.leftMouseButton:
            return

        if self.editTrybe:
            self.editedROI.mousePress(e)
        else:
            self.savePressLocation(e)

    def mouseReleaseEvent(self, e):
        if not self.leftMouseButton:
            return

        if self.editTrybe:
            self.editedROI.mouseRelease(e)
        else:
            self.seveReliseLocation(e)

    def mouseMoveEvent(self, e):
        if not self.leftMouseButton:
            return

        if self.editTrybe:
            self.editedROI.mouseMove(e)
        else:
            self.saveTemporaryLocation(e)

    @abstractmethod
    def savePressLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
        self.presed = True

    @abstractmethod
    def seveReliseLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()

        self.ROIList.append(ROI(self, self.x1, self.y1, self.x2, self.y2, self.roinames + 1))
        self.roinames += 1

        self.presed = False

    @abstractmethod
    def saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()

    @abstractmethod
    def right_menu(self, pos):

        menu = RightMenu(self)

        self.rightClickPos = pos

        self.rois = self.checkIfInROI()

        menu.addRoiMenus(self.rois, self.editTrybe)

        menu.exec_(self.mapToGlobal(pos))

    @abstractmethod
    def center(self):
        abstractmetod()

    @abstractmethod
    def checkIfInROI(self):
        rois = []
        for roi in self.ROIList:
            if roi.inROI(self.rightClickPos):
                rois.append(roi)
        return rois

    def endEdit(self):
        self.editTrybe = False


class CameraGUIextention(CameraGUI):

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUIextention, self).__init__(*args, **kwargs)

        self.cameraView = QlabelROI(self)

        self.setCentralWidget(self.cameraView)

        self.showMaximized()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = CameraGUIextention()

    window.show()

    app.exec_()
