from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from ROI.ROILabelViue import ROILegendViue


class ROILabel(QWidget):
    x = 256
    y = 144

    def __init__(self, roi, *args, **kwargs):
        super(ROILabel, self).__init__(*args, **kwargs)

        self.widget = QWidget()

        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.viue = ROILegendViue(roi, self.widget)
        self.layout.addWidget(self.viue)

        self.name = QLabel(str(roi.name), self.widget)
        self.name.setFont(QFont('Times', 20))
        # to-do color unification
        self.name.setStyleSheet("color: #c80a0a")
        self.name.move(self.geometry().topRight())

        self.layout.addWidget(self.name)

        self.setLayout(self.layout)

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)
