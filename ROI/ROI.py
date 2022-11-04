from PyQt5.QtCore import QRect, QPoint
from ROI.RenameWidnow import ReNameWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from ROI.ROILable import ROILabel
from utilitis.JsonRead.JsonRead import loadOffsetsJson


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

    pressPrecision = 50

    xOffset = 172
    yOffset = 145

    def __init__(self, mainWindow, x1, y1, x2, y2, name='1', manipulatotrX=25.0, manipulatorY=25.0):

        self.xOffset, self.yOffset = loadOffsetsJson()

        dx = int((manipulatotrX - 25) * self.xOffset)
        dy = int((manipulatorY - 25) * self.yOffset)

        x1, y1, x2, y2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy

        self._setBorders(x1, x2, y1, y2)
        print(self.x0, self.x1, self.y0, self.y1)
        self.name = name
        self.mainWindow = mainWindow

        self._createRectagle()

        self.textedit = ReNameWindow(self, text=str(name))

        self.label = ROILabel(self)

        self.viue = self.mainWindow.mainWindow.cameraView.getFrame()

    def _createRectagle(self):
        self.rect = QRect(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def updateViue(self):
        self.label.update()

    def _setBorders(self, x1, x2, y1, y2):
        self.minX = min(x1, x2)
        self.minY = min(y1, y2)
        self.maxX = max(x1, x2)
        self.maxY = max(y1, y2)
        self.x0 = self.minX
        self.x1 = self.maxX
        self.y0 = self.minY
        self.y1 = self.maxY

    def setNewBorders(self):
        self.minX = min(self.x0, self.x1)
        self.minY = min(self.y0, self.y1)
        self.maxX = max(self.x0, self.x1)
        self.maxY = max(self.y0, self.y1)
        self.x0 = self.minX
        self.x1 = self.maxX
        self.y0 = self.minY
        self.y1 = self.maxY

    def inROI(self, pos):
        return self.minX < pos.x() < self.maxX and self.minY < pos.y() < self.maxY

    def edit(self):
        self.mainWindow.editTribe = True
        self.mainWindow.editedROI = self

    def mousePress(self, e):
        self.firstPress = True
        self.mousePositionCheck(e)

        self._createRectagle()
        self.updateViue()

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
        self.setNewBorders()
        self.mainWindow.leftMouseButton = False
        self.updateViue()

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
        self.updateViue()

    def mousePositionCheck(self, e):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

        self.leftTop = False
        self.rightTop = False

        self.leftBottom = False
        self.rightBottom = False

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

    def cursorEdit(self, e):
        self.mousePositionCheck(e)
        if self.move:
            QApplication.setOverrideCursor(Qt.SizeAllCursor)
        elif self.rightTop or self.leftBottom:
            QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
        elif self.leftTop or self.rightBottom:
            QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
        elif self.left or self.right:
            QApplication.setOverrideCursor(Qt.SizeHorCursor)
        elif self.top or self.bottom:
            QApplication.setOverrideCursor(Qt.SizeVerCursor)
        else:
            QApplication.setOverrideCursor(Qt.ArrowCursor)

    def delete(self):
        self.mainWindow.ROIList.remove(self)
        self.mainWindow.removeLable(self.label)
        self.label = None
        self.mainWindow.endEdit()

    def GetTextLocation(self, x, y):
        dx = int((x - 25) * self.xOffset)
        dy = int((y - 25) * self.yOffset)
        return self.x0 - 15 - dx, self.y0 - 15 - dy

    def rename(self):
        self.textedit.show()

    def setName(self, name):
        self.name = name

    def getRect(self, x, y):
        dx = int((x - 25) * self.xOffset)
        dy = int((y - 25) * self.yOffset)
        return QRect(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x1 - dx, self.y1 - dy))
