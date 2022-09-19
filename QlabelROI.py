from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPoint
from abc import abstractmethod
from abc import ABCMeta
from CameraGUI import CameraGUI


class ROI:
    x1, x2, y1, y2 = 0, 0, 0, 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.rect = QRect(QPoint(x1, y1), QPoint(x2, y2))


class QlabelROI(QLabel):
    __metaclass__ = ABCMeta

    def __init__(self, mainWindow, *args, **kwargs):
        super(QlabelROI, self).__init__(*args, **kwargs)

        self.ROIList = []

        self.mainWindow = mainWindow

        self.setPixmap(self.getFrame())

        self.presed = False

    @abstractmethod
    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()
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
        self.savePressLocation(e)

    def mouseReleaseEvent(self, e):
        self.seveReliseLocation(e)

    def mouseMoveEvent(self, e):
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

        self.ROIList.append(ROI(self.x1, self.y1, self.x2, self.y2))

        self.presed = False

    @abstractmethod
    def saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()


class CameraGUIextention(CameraGUI):

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUIextention, self).__init__(*args, **kwargs)

        self.cameraView = QlabelROI(self)

        self.setCentralWidget(self.cameraView)
        self.showMaximized()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    from RightClickMenu import MainWindow

    app = QApplication(sys.argv)

    window = CameraGUIextention()

    window.show()

    app.exec_()
