from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget

class FixedAspectRatioWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._aspectRatio = 4/3

    def setAspectRatio(self, aspectRatio):
        self._aspectRatio = aspectRatio
        self.updateGeometry()

    def sizeHint(self):
        width = self.widthForHeight(self.height())
        return self.minimumSizeHint().expandedTo(QSize(width, self.height()))

    def resizeEvent(self, event):
        width = self.widthForHeight(event.size().height())
        self.resize(width, event.size().height())

    def widthForHeight(self, height):
        return int(height * self._aspectRatio)


from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication

app = QApplication([])
layout = QVBoxLayout()

widget = FixedAspectRatioWidget()
label = QLabel("Hello, world!")
widget.setLayout(QVBoxLayout(label))

widget.setAspectRatio(16/9)  # Change aspect ratio to 16:9

layout.addWidget(widget)
layout.addStretch()
app.exec_()
