from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt, QPoint, QRect
from Python.FrontEnd.MyQPoint.MyQPoint import MyQPoint

class ReNameWindow(QLineEdit):

    def __init__(self, ROI, *args, **kwargs):
        super(ReNameWindow, self).__init__(*args, **kwargs)

        self.ROI = ROI

        self.setGeometry(QRect(MyQPoint(self.ROI.x0, self.ROI.y0), MyQPoint(self.ROI.x0 + 100, self.ROI.y0 + 20)))

        #self.setWindowFlags(self.windowFlags() | Qt..FramelessWindowHint)
        self.setWindowOpacity(0)
        self.textChanged.connect(self.textChangedEvent)

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.setFocus()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.close()
            self.ROI.setName(self.text())
        else:
            super().keyPressEvent(event)

    def textChangedEvent(self, event):
        self.ROI.setName(self.text())

    def focusOutEvent(self, event):
        self.close()
