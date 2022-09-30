from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ExampleWindow(QMainWindow):

    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.windowsize)

        widget = QWidget()
        self.setCentralWidget(widget)
        pixmap1 = QPixmap('1.jpg')
        pixmap1 = pixmap1.scaledToWidth(self.windowsize.width())
        self.image = QLabel(widget)
        self.image.setPixmap(pixmap1)

        layout_box = QHBoxLayout(widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.image)

        self.image2 = QWidget(self)
        leyaout = QHBoxLayout()
        leyaout.addWidget(QPushButton())
        leyaout.addWidget(QPushButton())
        leyaout.addWidget(QPushButton())
        self.image2.setLayout(leyaout)

        p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        #self.image2.move(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

    sys.exit(app.exec_())