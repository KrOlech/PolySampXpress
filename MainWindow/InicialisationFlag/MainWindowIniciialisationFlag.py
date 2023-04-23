from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDesktopWidget

from MAP.Main.MapWindow import MapWindow
from MainWindow.RoiList.MainWindowROIList import MainWindowROIList
from WorkFeald.Main.main import ReadPoleRobocze
from utilitis.Depracation.DepractionFactory import deprecated
from utilitis.ThreadWorker.SimpleThreadWorker.FunWorkerAsync import workFunWorkerAsync


# todo podzielic do dwóch klas
class MainWindowInicialisationFlag(MainWindowROIList):
    fildParams = 0
    selectedManipulatorZoom = 1
    mapWindowObject = None

    def __init__(self, *args, **kwargs):
        super(MainWindowInicialisationFlag, self).__init__(*args, **kwargs)

        showMap = self.qActionCreate("Show Map", self.showMap)
        createMapAction = self.qActionCreate("Create Map", self.createMap)

        mapMenu = self.menu.addMenu("&MAP")
        mapMenu.addAction(showMap)
        mapMenu.addAction(createMapAction)

        self.readWorkFieldWindow = ReadPoleRobocze(self, self.windowSize)

        self.workFildMenu = self.menu.addMenu("&Work Field")

        self.workFildActions = []

        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            action = self.qActionCreate(str(field[-1]), lambda checked, nr=i: self.togle(nr), checkable=True)
            self.workFildMenu.addAction(action)
            self.workFildActions.append(action)

    def togle(self, nr):
        self.__UncheckAll()
        self.workFildActions[nr].setChecked(True)
        self.fildParams = self.readWorkFieldWindow.workFields[nr]
        self.loger(self.fildParams)

    def __UncheckAll(self, State=False):
        for workFildAction in self.workFildActions:
            workFildAction.setChecked(State)

    @deprecated("old Map cration manual")
    def createMapManual(self):
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
        else:
            x = self.manipulator.x
            y = self.manipulator.y
            self.mapWindowObject.addFrame(self.camera.getFrame())

    def createMap(self):
        self.mapWindowObject = self.crateMapObject()
        workFunWorkerAsync(self, self.mapWindowObject.mapCreate)
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
            workFunWorkerAsync(self, self.mapWindowObject.mapCreate)
        else:
            self.loger("do you wont to owe ride created Map?")
            # ToDo implement Correct in the future

    def showMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.move(QDesktopWidget().availableGeometry().topLeft())
            self.mapWindowObject.showMap()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams
        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            if self.fildParams == field:
                self.workFildActions[i].setChecked(True)
                break

    def crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulator)
