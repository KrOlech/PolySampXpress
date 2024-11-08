from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowRoiCreationInterferes(MainWindowAbstract):
    mode = "Classic"

    __classic = None
    __point = None
    __scatter = None
    __fromClicks = None
    __fromScatterClicks = None

    scatterConfig = None

    zeroPoint = {}

    def createRoiModsMenu(self):
        self.__pointer = self.qActionCreate("Hand Mode", self.__togglePointerMode, checkable=True)
        self.__classic = self.qActionCreate("Classic mode", self.__toggleClassicMode, checkable=True)
        self.__point = self.qActionCreate("Point mode", self.__togglePointMode, checkable=True)
        self.__fromClicks = self.qActionCreate("Click mode", self.__toggleClicksMode, checkable=True)
        self.__pointSpacing = self.qActionCreate("Calculate distant between points", self.__togglePointSpacing,
                                                 checkable=True)

        self.modes = [self.__pointer, self.__classic, self.__point, self.__fromClicks, self.__pointSpacing]

        self.__classic.setChecked(True)

        roi = self.menu.addMenu("&ROI")

        for mod in self.modes:
            roi.addAction(mod)

        self.myStatusBarClick = self.clickCreateStatus()

    def __toggleClassicMode(self):
        self.__UncheckAll()
        self.__classic.setChecked(True)
        self.mode = "Classic"

    def __togglePointMode(self):
        self.__UncheckAll()
        self.__point.setChecked(True)
        self.mode = "Point"

    def __toggleClicksMode(self):
        self.__UncheckAll()
        self.__fromClicks.setChecked(True)
        self.mode = "Clicks"
        self.myStatusBarClick.setText("Click Mode")

    def __togglePointerMode(self):
        self.__UncheckAll()
        self.__pointer.setChecked(True)
        self.mode = "Pointer"
        self.myStatusBarClick.setText("Pointer Mode")

    def __togglePointSpacing(self):
        self.__UncheckAll()
        self.__pointSpacing.setChecked(True)
        self.mode = "pointSpacing"
        self.myStatusBarClick.setText("Calculate distant between points")

    def __UncheckAll(self, State=False):
        self.cameraView.toggleModeCleenUp()
        self.cameraView.pressed = False
        for mod in self.modes:
            mod.setChecked(State)
        self.myStatusBarClick.setText("")

    def clickCreateStatus(self):
        myStatusBar = QLabel(self)

        myStatusBar.setFixedWidth(self.windowSize.width() // 8)

        myStatusBar.setStyleSheet("background-color: rgba(255, 255, 255, 75);")

        font = QFont()
        font.setPointSize(13)

        myStatusBar.setAlignment(Qt.AlignCenter)
        myStatusBar.setFont(font)

        myStatusBar.move(
            QPoint(self.windowSize.width() // 2 - self.windowSize.width() // 16,
                   self.windowSize.height() - 25 - myStatusBar.height()))

        myStatusBar.show()

        return myStatusBar
