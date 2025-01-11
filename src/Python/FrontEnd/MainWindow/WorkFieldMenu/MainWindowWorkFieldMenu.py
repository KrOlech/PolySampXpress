from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract
from Python.BackEnd.WorkFeald.Main.main import ReadPoleRobocze
from Python.FrontEnd.MainWindow.InicialisationFlag.WindowCreateWorkFeald import WindowCreateWorkFeald


class MainWindowWorkFieldMenu(MainWindowAbstract):
    fildParams = 0

    workFildMenu = None

    readWorkFieldWindow = None

    workFildActions = []

    def createWorkFieldMenu(self):
        self.readWorkFieldWindow = ReadPoleRobocze(self, self.windowSize)

        self.workFildMenu = self.menu.addMenu("&Work Field")
        createWorkFiled = self.qActionCreate("Create Work Field", self.createWorkField)
        self.workFildMenu.addAction(createWorkFiled)

        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            name = f"X:{field[0]}_{field[1]}; Y:{field[2]}_{field[3]}"
            action = self.qActionCreate(name, lambda checked, nr=i: self.__toggle(nr), checkable=True)
            self.workFildMenu.addAction(action)
            self.workFildActions.append(action)

        self.toggleWorkField(0)

    def toggleWorkField(self,nr):
        try:
            self.__toggle(nr)
        except Exception as e:
            self.logError(e)

    def __toggle(self, nr):
        self.cameraView.afterInitialisation = True
        self.__UncheckAll()
        self.workFildActions[nr].setChecked(True)
        try:
            self.fildParams = self.readWorkFieldWindow.workFields[nr]
            self.loger(self.fildParams)
        except ImportError as e:
            self.logError(e)

    def __UncheckAll(self, State=False):
        for workFildAction in self.workFildActions:
            workFildAction.setChecked(State)

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams
        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            if self.fildParams == field:
                self.workFildActions[i].setChecked(True)
                break

    def createWorkField(self):
        WindowCreateWorkFeald(self).exec_()