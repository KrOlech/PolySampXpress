from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QSizeGrip

from src.ROI.Main.Point.PointClass import Point
from src.ROI.Main.ROI.ROI import ROI
from src.MAP.Label.WaitWindow import WaitWindow
from src.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker
from src.MainWindow.Utilitis.WindowBar import MyBar


class MapLabel(QLabel):
    _aspectRatio = 4 / 3

    def __init__(self, master, *args, **kwargs):
        super(MapLabel, self).__init__(*args, **kwargs)

        self.master = master

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Mozaik")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            grip.setStyleSheet("""background-color: transparent; """)
            self.grips.append(grip)

        self.xMin = self.master.master.fildParams[0]
        self.xMax = self.master.master.fildParams[1]
        self.mapWidth = self.xMax - self.xMin

        self.yMin = self.master.master.fildParams[2]
        self.yMax = self.master.master.fildParams[3]
        self.mapHeight = self.yMax - self.yMin

    def resizeEvent(self, event):
        rect = self.rect()

        self.grips[1].move(rect.right() - self.gripSize, 0)
        self.grips[2].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        self.grips[3].move(0, rect.bottom() - self.gripSize)


        if abs(event.size().width() - self.width()) > abs(event.size().height() - self.height()):
            height = event.size().width() // self._aspectRatio
            width = event.size().width()
        else:
            width = event.size().height() * self._aspectRatio
            height = event.size().height()

        self.resize(int(width), int(height))

        self.titleBar.resize(self.width(), self.titleBar.height())

    def paintEvent(self, QPaintEvent):
        if self.master.mapPx is not None:

            qp = QPainter(self)
            qp.drawPixmap(self.rect(), self.master.mapPx)
            qp.setBrush(QBrush(QColor(200, 10, 10, 200)))

            qp.setFont(QFont("Arial", 24))

            pen = qp.pen()
            pen.setColor(QColor("blue"))
            qp.setPen(pen)

            for i, rectangle in enumerate(self.master.master.cameraView.ROIList):
                rx, ry = rectangle.GetTextLocationMap(self.width(),
                                                      self.height(),
                                                      self.mapWidth,
                                                      self.mapHeight,
                                                      self.xMin, self.yMin,
                                                      self.master.scale)
                qp.drawText(rx, ry, str(rectangle.name))

                if isinstance(rectangle, ROI):
                    qp.drawRect(rectangle.getMarkerMap(self.width(),
                                                       self.height(),
                                                       self.mapWidth,
                                                       self.mapHeight,
                                                       self.xMin, self.yMin,
                                                       self.master.scale))
                elif isinstance(rectangle, Point):
                    qp.drawLines(rectangle.getMarkerMap(self.width(),
                                                        self.height(),
                                                        self.mapWidth,
                                                        self.mapHeight,
                                                        self.xMin, self.yMin,
                                                        self.master.scale))

    def setAspectRatio(self, aspectRatio):
        self._aspectRatio = aspectRatio
        self.updateGeometry()

    def sizeHint(self):
        width = self.widthForHeight(self.height())
        return self.minimumSizeHint().expandedTo(QSize(width, self.height()))

    def widthForHeight(self, height):
        return int(height * self._aspectRatio)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            waitWindow = WaitWindow(self)
            waitWindow.run(event)
            waitWindow.exec_()

    def threadFun(self, event):
        x, y = event.x(), event.y()

        self.master.manipulator.goToCords(
            x=self.calculateCords(x, self.master.windowSize.width(), self.xMin, self.xMax),
            y=self.calculateCords(y, self.master.windowSize.height(), self.yMin, self.yMax))

    @staticmethod
    def calculateCords(clickPosytion, windowSize, mapMinimulPosytion, mapMaximumPosytion):
        return (clickPosytion * (mapMaximumPosytion - mapMinimulPosytion)) / windowSize + mapMinimulPosytion

    def mouseMoveEvent(self, event):
        ...

    def mouseReleaseEvent(self, event):
        ...
