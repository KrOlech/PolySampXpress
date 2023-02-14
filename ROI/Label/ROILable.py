from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel
from ROI.LabelViue.ROILabelViue import ROILegendVue


class ROILabel(QWidget):
    scalaX = 10  # TODo move to config File
    scalaY = 10

    def __init__(self, roi, screenSize, *args, **kwargs):
        super(ROILabel, self).__init__(*args, **kwargs)

        self.x = screenSize.width() // self.scalaX
        self.y = screenSize.height() // self.scalaY

        self.widget = QWidget()

        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.viue = ROILegendVue(roi, self.x, self.y, self.scalaX, self.scalaY, widget=self.widget)
        self.layout.addWidget(self.viue)

        self.name = QLabel(str(roi.name), self.widget)
        self.name.setFont(QFont('Times', 20))
        self.name.setStyleSheet("color: #c80a0a")  # TODO color unification
        self.name.move(self.geometry().topRight())

        self.layout.addWidget(self.name)

        self.setLayout(self.layout)

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)
