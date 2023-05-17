from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from src.ROI.RightMenu.ROIRightMenu import RoiRightMenu
from src.ROI.LabelViue.ROILabelViue import ROILegendVue
from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.BaseClass.Logger.Logger import Loger


class ROILabel(QWidget, Loger):
    scalaX, scalaY = JsonHandling.readRoiLabelScalles()

    def __init__(self, roi, screenSize, *args, **kwargs):
        super(ROILabel, self).__init__(*args, **kwargs)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenu)

        self.x = screenSize.width() // self.scalaX
        self.y = screenSize.height() // self.scalaY

        self.widget = QWidget()

        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.viue = ROILegendVue(roi, self.x, self.y, self.scalaX, self.scalaY, widget=self.widget)
        self.layout.addWidget(self.viue)

        self.name = QLabel(str(roi.name), self.widget)
        self.name.setFont(QFont('Times', 20))
        self.name.setStyleSheet("color: #c80a0a")  # Odpowiada 200 10 10 w RGB
        self.name.move(self.geometry().topRight())

        self.layout.addWidget(self.name)

        self.setLayout(self.layout)

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)

        self.roi = roi

    def rightMenu(self, e):
        menu = RoiRightMenu(self.roi)

        menu.exec_(self.mapToGlobal(e))

    def updateName(self, NewName):
        self.name.setText(NewName)
