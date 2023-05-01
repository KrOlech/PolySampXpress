from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt


class ReNameWindow(QLineEdit):

    def __init__(self, ROI, *args, **kwargs):
        super(ReNameWindow, self).__init__(*args, **kwargs)

        self.ROI = ROI

        x,y = 0,0 #toDo corect placement

        self.setGeometry(x, y, 10, 10)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setWindowOpacity(0)
        self.textChanged.connect(self.textChangedEvent)

        self.setFocusPolicy(Qt.ClickFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.close()
            self.ROI.setName(self.text())
        else:
            super().keyPressEvent(event)

    def textChangedEvent(self, event):
        self.ROI.setName(self.text())

    def focusOutEvent(self, event):
        self.close()
