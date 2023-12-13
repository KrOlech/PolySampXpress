from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, QPoint, QRect


class ReNameWindow(QLineEdit):

    def __init__(self, ROI, *args, **kwargs):
        super(ReNameWindow, self).__init__(*args, **kwargs)

        self.ROI = ROI

        self.setGeometry(QRect(QPoint(self.ROI.x0, self.ROI.y0), QPoint(self.ROI.x0 + 100, self.ROI.y0 + 20)))

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setWindowOpacity(0)
        self.textChanged.connect(self.textChangedEvent)

        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()

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
