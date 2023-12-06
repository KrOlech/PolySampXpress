from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from Python.FrontEnd.MainWindow.RoiCreation.ScatterConfigureWindow import ScatterConfigureWindow
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowRoiCreationInterferes(MainWindowAbstract):
    mode = "Classic"

    __classic = None
    __point = None
    __scatter = None
    __fromClicks = None
    __fromScatterClicks = None

    scatterConfig = None

    def createRoiModsMenu(self):
        self.__pointer = self.qActionCreate("Pointer Mode", self.__togglePointerMode,
                                            checkable=True)
        self.__classic = self.qActionCreate("Classic mode", self.__toggleClassicMode, checkable=True)
        self.__point = self.qActionCreate("Point mode", self.__togglePointMode, checkable=True)
        self.__scatter = self.qActionCreate("Scatter mode", self.__toggleScatterMode, checkable=True)
        self.__fromClicks = self.qActionCreate("Click mode", self.__toggleClicksMode, checkable=True)
        self.__fromScatterClicks = self.qActionCreate("Click Scatter mode", self.__toggleScatterClicksMode,
                                                      checkable=True)

        self.__classic.setChecked(True)

        roi = self.menu.addMenu("&ROI")

        roi.addAction(self.__pointer)
        roi.addAction(self.__classic)
        roi.addAction(self.__point)
        roi.addAction(self.__scatter)
        roi.addAction(self.__fromClicks)
        roi.addAction(self.__fromScatterClicks)

        self.myStatusBarClick = self.clickCreateStatus()

    def __toggleClassicMode(self):
        self.__UncheckAll()
        self.__classic.setChecked(True)
        self.mode = "Classic"

    def __togglePointMode(self):
        self.__UncheckAll()
        self.__point.setChecked(True)
        self.mode = "Point"

    def __toggleScatterMode(self):
        self.__UncheckAll()
        self.__scatter.setChecked(True)
        self.mode = "Scatter"
        ScatterConfigureWindow(self).exec_()

    def __toggleClicksMode(self):
        self.__UncheckAll()
        self.__fromClicks.setChecked(True)
        self.mode = "Clicks"
        self.myStatusBarClick.setText("Click Mode")

    def __toggleScatterClicksMode(self):
        self.__UncheckAll()
        self.__fromScatterClicks.setChecked(True)
        self.mode = "Clicks Scatter"
        self.myStatusBarClick.setText("Click Mode")
        ScatterConfigureWindow(self).exec_()

    def __togglePointerMode(self):
        self.__UncheckAll()
        self.__pointer.setChecked(True)
        self.mode = "Pointer"
        self.myStatusBarClick.setText("Pointer Mode")

    def __UncheckAll(self, State=False):
        self.__classic.setChecked(State)
        self.__point.setChecked(State)
        self.__scatter.setChecked(State)
        self.__fromClicks.setChecked(State)
        self.__pointer.setChecked(State)
        self.__fromScatterClicks.setChecked(State)
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
            QPoint(self.windowSize.width() // 2 - self.windowSize.width() // 16, self.windowSize.height() - 25))
        myStatusBar.show()

        return myStatusBar
