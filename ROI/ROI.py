from PyQt5.QtCore import QRect, QPoint
from ROI.RenameWidnow import ReNameWindow


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

        self._setBorders(x1, x2, y1, y2)

        self.name = name
        self.mainWindow = mainWindow

        self._createRectagle()

        self.textedit = ReNameWindow(self, text=str(name))

    def _createRectagle(self):
        self.rect = QRect(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))
        self.setNewBorders()

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

    def GetTextLocation(self):
        return self.x0 - 15, self.y0 - 15

    def rename(self):
        self.textedit.show()

    def setName(self, name):
        self.name = name
