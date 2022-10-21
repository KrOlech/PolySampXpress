from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class ROIList(QScrollArea):
    tekst_placeholdera = "Brak oznaczonych obszarów"
    roiCount = 0

    def __init__(self, mainWindow, *args, **kwargs):
        super(ROIList, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.defalaut_lable = QLabel(self.tekst_placeholdera)

        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.widget.setLayout(self.vbox)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setWidgetResizable(True)

        self.setWidget(self.widget)

        self.setMaximumSize(300, 1200)
        self.setMinimumSize(300, 1200)

        self.vbox.addWidget(self.defalaut_lable)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 10);")

    def addROI(self, ROI):
        self._delDefalautLable()
        self.vbox.addWidget(ROI)
        self.roiCount += 1

    def removeROI(self, ROI):
        self.vbox.removeWidget(ROI)
        self.roiCount -= 1
        if not self.roiCount:
            self._addDefalautLable()

    def _delDefalautLable(self):
        self.vbox.removeWidget(self.defalaut_lable)
        self.defalaut_lable = None

    def _addDefalautLable(self):
        self.defalaut_lable = QLabel(self.tekst_placeholdera)
        self.vbox.addWidget(self.defalaut_lable)
