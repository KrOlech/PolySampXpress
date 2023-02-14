from PySide2.QtGui import QPixmap, QImage, QPainter
from PySide2 import QtGui
from PySide2.QtWidgets import QLabel


class SimpleView(QLabel):

    def __init__(self, mainWindow, *args, **kwargs) -> None:
        super(SimpleView, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.setPixmap(self.getFrame())

    def getFrame(self) -> QPixmap:
        cvBGBImg = self.mainWindow.camera.getFrame()
        qImg = QImage(cvBGBImg.data, cvBGBImg.shape[1], cvBGBImg.shape[0], QImage.Format_BGR888)

        frame = QPixmap.fromImage(qImg)

        return frame

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)

        qp.drawPixmap(self.rect(), frame := self.getFrame())

        self.setPixmap(frame)
