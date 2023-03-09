from MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowRoiCreationInterferes(MainWindowAbstract):
    mode = "Classic"

    __classic = None
    __point = None
    __scatter = None

    def createRoiModsMenu(self):
        self.__classic = self.qActionCreate("Classic mode", self.__toggleClassicMode, checkable=True)
        self.__point = self.qActionCreate("Point mode", self.__togglePointMode, checkable=True)
        self.__scatter = self.qActionCreate("Scatter mode", self.__toggleScatterMode, checkable=True)

        self.__classic.setChecked(True)

        roi = self.menu.addMenu("&ROI")

        roi.addAction(self.__classic)
        roi.addAction(self.__point)
        roi.addAction(self.__scatter)

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

    def __UncheckAll(self, State=False):
        self.__classic.setChecked(State)
        self.__point.setChecked(State)
        self.__scatter.setChecked(State)
