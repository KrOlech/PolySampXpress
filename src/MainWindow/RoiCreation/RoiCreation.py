from src.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowRoiCreationInterferes(MainWindowAbstract):
    mode = "Classic"

    __classic = None
    __point = None
    __scatter = None
    __fromClicks = None

    def createRoiModsMenu(self):
        self.__classic = self.qActionCreate("Classic mode", self.__toggleClassicMode, checkable=True)
        self.__point = self.qActionCreate("Point mode", self.__togglePointMode, checkable=True)
        self.__scatter = self.qActionCreate("Scatter mode", self.__toggleScatterMode, checkable=True)
        self.__fromClicks = self.qActionCreate("Click mode", self.__toggleClicksMode, checkable=True)
        self.__fromScatterClicks = self.qActionCreate("Click Scatter mode", self.__toggleScatterClicksMode, checkable=True)

        self.__classic.setChecked(True)

        roi = self.menu.addMenu("&ROI")

        roi.addAction(self.__classic)
        roi.addAction(self.__point)
        roi.addAction(self.__scatter)
        roi.addAction(self.__fromClicks)
        roi.addAction(self.__fromScatterClicks)

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

    def __toggleClicksMode(self):
        self.__UncheckAll()
        self.__fromClicks.setChecked(True)
        self.mode = "Clicks"

    def __toggleScatterClicksMode(self):
        self.__UncheckAll()
        self.__fromScatterClicks.setChecked(True)
        self.mode = "Clicks Scatter"

    def __UncheckAll(self, State=False):
        self.__classic.setChecked(State)
        self.__point.setChecked(State)
        self.__scatter.setChecked(State)
        self.__fromClicks.setChecked(State)
