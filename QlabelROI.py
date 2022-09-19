from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPoint, Qt, QEvent
from abc import abstractmethod
from abc import ABCMeta
from CameraGUI import CameraGUI
from RightClickMenu import RightMenu, RightClickLabel
from Abstract import abstractmetod


class ROI:
    x0, x1, y0, y1 = 0, 0, 0, 0
    firstPress = False

    top = False
    bottom = False
    left = False
    right = False

    leftTop = False
    rightTop = False
    leftBottom = False
    rightBottom = False

    move = False

    pressPrecision = 100

    def __init__(self, mainWindow, x1, y1, x2, y2, name='1'):

        self.minX = min(x1, x2)
        self.minY = min(y1, y2)
        self.maxX = max(x1, x2)
        self.maxY = max(y1, y2)
        self.x0 = self.minX
        self.x1 = self.maxX
        self.y0 = self.minY
        self.y1 = self.maxY
        self.name = name
        self.mainWindow = mainWindow

        self._createRectagle()

    def _createRectagle(self):
        self.rect = QRect(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def inROI(self, pos):
        return self.minX < pos.x() < self.maxX and self.minY < pos.y() < self.maxY

    def edit(self):
        self.mainWindow.editTrybe = True
        self.mainWindow.editedROI = self

    def mousePress(self, e):
        self.firstPress = True

        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

        self.move = False

        self.px0, self.py0 = e.x(), e.y()

        if self.x0 - self.pressPrecision < self.px0 < \
                self.x0 + self.pressPrecision and \
                self.y0 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision:
            self.right = True

        if self.x1 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision and \
                self.y0 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision:
            self.left = True

        if self.y0 - self.pressPrecision < self.py0 < \
                self.y0 + self.pressPrecision and \
                self.x0 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision:
            self.top = True

        if self.y1 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision and \
                self.x0 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision:
            self.bottom = True

        self.leftTop = self.left and self.top
        self.rightTop = self.right and self.top

        self.leftBottom = self.left and self.bottom
        self.rightBottom = self.right and self.bottom

        if self.y0 + self.pressPrecision < self.py0 < \
                self.y1 - self.pressPrecision and \
                self.x0 + self.pressPrecision < self.px0 < \
                self.x1 - self.pressPrecision:
            self.move = True

        self._createRectagle()

    def mouseRelease(self, e):

        self.firstPress = False

        self.px1, self.py1 = e.x(), e.y()

        if self.move:
            dx, dy = self.px1 - self.px0, self.py1 - self.py0
            self.x0 += dx
            self.x1 += dx
            self.y0 += dy
            self.y1 += dy
        elif self.leftTop:
            self.x1 = self.px1
            self.y0 = self.py1
        elif self.leftBottom:
            self.x1 = self.px1
            self.y1 = self.py1
        elif self.rightBottom:
            self.x0 = self.px1
            self.y1 = self.py1
        elif self.rightTop:
            self.x0 = self.px1
            self.y0 = self.py1
        elif self.bottom:
            self.y1 = self.py1
        elif self.left:
            self.x1 = self.px1
        elif self.right:
            self.x0 = self.px1
        elif self.top:
            self.y0 = self.py1

        self._createRectagle()

    def mouseMove(self, e):

        if self.firstPress:

            self.px1, self.py1 = e.x(), e.y()

            if self.move:
                dx, dy = self.px1 - self.px0, self.py1 - self.py0
                self.x0 += dx
                self.x1 += dx
                self.y0 += dy
                self.y1 += dy
                self.px0, self.py0 = e.x(), e.y()
            elif self.leftTop:
                self.x1 = self.px1
                self.y0 = self.py1
            elif self.leftBottom:
                self.x1 = self.px1
                self.y1 = self.py1
            elif self.rightBottom:
                self.x0 = self.px1
                self.y1 = self.py1
            elif self.rightTop:
                self.x0 = self.px1
                self.y0 = self.py1
            elif self.bottom:
                self.y1 = self.py1
            elif self.left:
                self.x1 = self.px1
            elif self.right:
                self.x0 = self.px1
            elif self.top:
                self.y0 = self.py1

        self._createRectagle()

    def delete(self):
        self.mainWindow.ROIList.remove(self)

    def _pobierz_gorny_naroznik(self, ox=100, oy=100):

        if self.x0 < self.x1 and self.y0 < self.y1:
            xp0 = (self.x0 - ox)
            yp0 = (self.y0 - oy)
        elif self.x0 < self.x1 and self.y0 > self.y1:
            xp0 = (self.x0 - ox)
            yp0 = (self.y1 - oy)
        elif self.x0 > self.x1 and self.y0 < self.y1:
            xp0 = (self.x1 - ox)
            yp0 = (self.y0 - oy)
        else:
            xp0 = (self.x1 - ox)
            yp0 = (self.y1 - oy)

        return xp0, yp0


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


if __name__ == '__main__':
    class CameraGUIextention(CameraGUI):

        def __init__(self, *args, **kwargs) -> None:
            super(CameraGUIextention, self).__init__(*args, **kwargs)

            self.cameraView = QlabelROI(self)

            self.setCentralWidget(self.cameraView)
            self.showMaximized()


    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = CameraGUIextention()

    window.show()

    app.exec_()
