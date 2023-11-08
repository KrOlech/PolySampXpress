from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class ROIList(QScrollArea):
    placeholder = "No marked ROI's"
    roiCount = 0
    width = 300

    def __init__(self, mainWindow, *args, **kwargs):
        super(ROIList, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.defalcateLabel = QLabel(self.placeholder)

        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.widget.setLayout(self.vbox)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setWidgetResizable(True)

        self.setWidget(self.widget)

        self.hight = self.calculateHight()
        self.setMaximumSize(self.width, self.hight)
        self.setMinimumSize(self.width, self.hight)

        self.vbox.addWidget(self.defalcateLabel)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 10);")

    def calculateHight(self):
        screenHight = self.mainWindow.windowSize.height()

        hight = screenHight - 290  #TODO calculate insted of approximated size of Manipulator buttons

        return hight

    def addROI(self, ROI):
        self.__delDefalautLable()
        self.vbox.addWidget(ROI)
        self.roiCount += 1

    def removeROI(self, ROI):
        self.vbox.removeWidget(ROI)
        self.roiCount -= 1
        if not self.roiCount:
            self.__addDefalautLable()

    def __delDefalautLable(self):
        self.vbox.removeWidget(self.defalcateLabel)
        self.defalcateLabel = None

    def __addDefalautLable(self):
        self.defalcateLabel = QLabel(self.placeholder)
        self.vbox.addWidget(self.defalcateLabel)
