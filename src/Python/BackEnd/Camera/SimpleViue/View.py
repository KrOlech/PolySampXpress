from PyQt6.QtCore import QRect
from PyQt6.QtGui import QPixmap, QImage, QPainter
from PyQt6 import QtGui
from PyQt6.QtWidgets import QLabel


class SimpleView(QLabel):

    def __init__(self, mainWindow, *args, **kwargs) -> None:
        super(SimpleView, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.setPixmap(self.getFrame())

    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()
        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format.Format_BGR888)

        frame = QPixmap.fromImage(qImg)

        return frame.copy(QRect(0,1080,0,1920))

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), frame := self.getFrame())

        self.setPixmap(frame)
