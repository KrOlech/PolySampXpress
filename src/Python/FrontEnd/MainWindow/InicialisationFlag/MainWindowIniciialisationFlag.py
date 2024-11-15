from PyQt5.QtWidgets import QDesktopWidget, QMenu

from Python.BackEnd.MAP.Dialog.NewMapDialog import NewMapDialog
from Python.BackEnd.MAP.Main.MapWindow import MapWindow
from Python.BackEnd.ROI.RenameWindow.RenameWidnow import ReNameWindow
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.FunWorkerAsync import workFunWorkerAsync
from Python.BackEnd.WorkFeald.Main.main import ReadPoleRobocze
from Python.FrontEnd.MainWindow.InicialisationFlag.DialogWindowMap import DialogWindowMap
from Python.FrontEnd.MainWindow.InicialisationFlag.MapFromHearWindow import MapFromHearWindow
from Python.FrontEnd.MainWindow.InicialisationFlag.WindowCreateWorkFeald import WindowCreateWorkFeald
from Python.FrontEnd.MainWindow.RoiList.MainWindowROIList import MainWindowROIList
from Python.Utilitis.timer import timeit


class MainWindowInicialisationFlag(MainWindowROIList):
    fildParams = 0
    selectedManipulatorZoom = 1
    mapWindowObject = None
    isMapReadi = None
    creatingMap = False
    mapFromHearX = 5
    mapFromHearY = 5
    createMapVariable = None
    mapId = 0

    def __init__(self, *args, **kwargs):
        super(MainWindowInicialisationFlag, self).__init__(*args, **kwargs)

        self.mapsList = {}

        self.mapListMenu = QMenu("Mozaik list", self)
        createMapAction = self.qActionCreate("Create Mozaik", self.createMap)
        createMapFromHearAction = self.qActionCreate("Create Mozaik From Hear", self.createMapFromHear)
        self.mozaikBorders = self.qActionCreate("Show Border Lines", lambda _: _, checkable=True)

        self.mozaikBorders.setChecked(True)

        mapMenu = self.menu.addMenu("&Mozaik")
        mapMenu.addMenu(self.mapListMenu)
        mapMenu.addAction(createMapAction)
        mapMenu.addAction(createMapFromHearAction)
        mapMenu.addAction(self.mozaikBorders)

        self.__createWorkFieldMenu()

    def __createWorkFieldMenu(self):
        self.readWorkFieldWindow = ReadPoleRobocze(self, self.windowSize)

        self.workFildMenu = self.menu.addMenu("&Work Field")
        createWorkFiled = self.qActionCreate("Create Work Field", self.createWorkField)
        self.workFildMenu.addAction(createWorkFiled)

        self.workFildActions = []

        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            name = f"X:{field[0]}_{field[1]}; Y:{field[2]}_{field[3]}"
            action = self.qActionCreate(name, lambda checked, nr=i: self.togle(nr), checkable=True)
            self.workFildMenu.addAction(action)
            self.workFildActions.append(action)

        try:
            self.togle(0)
        except Exception as e:
            self.logError(e)

    def closeAction(self):
        super(MainWindowInicialisationFlag, self).closeAction()
        for mapO in self.mapsList.values():
            mapO.mapWidget.close()

    def togle(self, nr):
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

    def createMap(self):
        if self.creatingMap:
            self.loger("Can't create map already creating map")
            self.dialogWindowMap.show()
        else:
            self.creatingMap = True

            self.loger("do you wont to created Map?")
            NewMapDialog(self).exec_()

            if not self.createMapVariable:
                self.loger("no I don't wont to created Map?")
                self.creatingMap = False
                return

            self.loger("Yes I wont to created Map?")

            self.isMapReadi = False

            self.__createMap()


    @timeit
    def __createMap(self):
        mapWindowObject = self.crateMapObject()

        self.dialogWindowMap = DialogWindowMap(self)
        self.dialogWindowMap.run()
        workFunWorkerAsync(self, mapWindowObject.mapCreate)
        self.dialogWindowMap.exec_()

        self.addMap(mapWindowObject)

    def addMap(self, mapWindowObject):

        self.mapsList[self.mapId] = mapWindowObject

        mapMenu = QMenu(str(self.mapId), self)
        mapMenu.addAction(self.qActionCreate("Show", lambda checked, nr=mapWindowObject.mapId: self.showMap(nr)))
        mapMenu.addAction(self.qActionCreate("Remove", lambda checked, nr=mapWindowObject.mapId: self.removeMap(nr)))
        mapMenu.addAction(self.qActionCreate("ReName", lambda checked, nr=mapWindowObject.mapId: self.newNameOfMap(nr)))



        self.mapListMenu.addMenu(mapMenu)
        mapWindowObject.menu = mapMenu

        self.mapId += 1

    def removeMap(self, mapId):
        if self.mapsList[mapId].isMapReadi:
            self.loger(f"removing map from list {mapId}")
            self.mapListMenu.removeAction(self.mapsList[mapId].menu.menuAction())
            self.mapsList[mapId].mapWidget.close()
            self.mapsList[mapId] = None
            self.mapsList.pop(mapId)
            self.loger("removed map from list")
        else:
            self.loger("Cannot remove map from list, Map still in progress")
            self.dialogWindowMap.show()

    def createMapFromHear(self):
        MapFromHearWindow(self).exec_()

    def showMap(self, mapId):
        self.mapsList[mapId].move(QDesktopWidget().availableGeometry().topLeft())
        self.mapsList[mapId].showMap()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams
        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            if self.fildParams == field:
                self.workFildActions[i].setChecked(True)
                break

    def crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulatorInterferes, self.mapId)

    def saveMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.saveMapToFile()
            self.manipulatorInterferes.stop()

    def createWorkField(self):
        WindowCreateWorkFeald(self).exec_()

    def endMapCreation(self):
        for map in self.mapsList.values():
            map.mapEnd = True

    def newNameOfMap(self, mapId):
        mapO = self.mapsList[mapId]
        ReNameWindow(mapO, self, text=str(mapO.mapId)).show()