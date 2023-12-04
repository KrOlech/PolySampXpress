from PyQt5.QtWidgets import QDesktopWidget

from Python.BackEnd.MAP.Dialog.NoMapDialog import NoMapDialog
from src.Python.FrontEnd.MainWindow.InicialisationFlag.MapFromHearWindow import MapFromHearWindow
from src.Python.FrontEnd.MainWindow.InicialisationFlag.WindowCreateWorkFeald import WindowCreateWorkFeald
from src.Python.BackEnd.MAP.Dialog.OwerideDialog import OwerideCurrentMapDialog
from src.Python.FrontEnd.MainWindow.InicialisationFlag.DialogWindowMap import DialogWindowMap
from src.Python.BackEnd.MAP.Main.MapWindow import MapWindow
from src.Python.FrontEnd.MainWindow.RoiList.MainWindowROIList import MainWindowROIList
from src.Python.BackEnd.WorkFeald.Main.main import ReadPoleRobocze
from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.FunWorkerAsync import workFunWorkerAsync


class MainWindowInicialisationFlag(MainWindowROIList):
    fildParams = 0
    selectedManipulatorZoom = 1
    mapWindowObject = None
    isMapReadi = None
    owerideMap = False
    creatingMap = False
    mapFromHearX = 5
    mapFromHearY = 5

    def __init__(self, *args, **kwargs):
        super(MainWindowInicialisationFlag, self).__init__(*args, **kwargs)

        showMap = self.qActionCreate("Show Mozaik", self.showMap)
        createMapAction = self.qActionCreate("Create Mozaik", self.createMap)
        saveMapAction = self.qActionCreate("Save Mozaik", self.saveMap)
        createMapFromHearAction = self.qActionCreate("Create Mozaik From Hear", self.createMapFromHear)
        self.mozaikBorders = self.qActionCreate("Show Border Lines", lambda _: _, checkable=True)

        self.mozaikBorders.setChecked(True)

        mapMenu = self.menu.addMenu("&Mozaik")
        mapMenu.addAction(showMap)
        mapMenu.addAction(createMapAction)
        mapMenu.addAction(saveMapAction)
        mapMenu.addAction(createMapFromHearAction)
        mapMenu.addAction(self.mozaikBorders)

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

    def closeAction(self):
        super(MainWindowInicialisationFlag, self).closeAction()
        if self.mapWindowObject:
            self.mapWindowObject.mapWidget.close()

    def togle(self, nr):
        self.cameraView.afterInitialisation = True
        self.__UncheckAll()
        self.workFildActions[nr].setChecked(True)
        self.fildParams = self.readWorkFieldWindow.workFields[nr]
        self.loger(self.fildParams)

    def __UncheckAll(self, State=False):
        for workFildAction in self.workFildActions:
            workFildAction.setChecked(State)

    def createMap(self):
        self.creatingMap = True
        if not self.mapWindowObject:
            self.__createMap()
        else:
            self.loger("do you wont to owe ride created Map?")
            OwerideCurrentMapDialog(self).exec_()

            if not self.owerideMap:
                self.loger("no I don't wont to owe ride created Map?")
                self.creatingMap = False
                return

            self.loger("Yes I wont to owe ride created Map?")

            self.owerideMap = False
            self.mapWindowObject.mapWidget.close()
            self.mapWindowObject = None
            self.isMapReadi = False

            self.__createMap()

    def __createMap(self):
        self.mapWindowObject = self.crateMapObject()
        self.dialogWindowMap = DialogWindowMap(self)
        self.dialogWindowMap.run()
        workFunWorkerAsync(self, self.mapWindowObject.mapCreate)
        self.dialogWindowMap.exec_()

    def createMapFromHear(self):
        MapFromHearWindow(self).exec_()

    def showMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.move(QDesktopWidget().availableGeometry().topLeft())
            self.mapWindowObject.showMap()
        else:
            NoMapDialog(self).exec_()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams
        for i, field in enumerate(self.readWorkFieldWindow.workFields):
            if self.fildParams == field:
                self.workFildActions[i].setChecked(True)
                break

    def crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulatorInterferes)

    def saveMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.saveMapToFile()
            self.manipulatorInterferes.stop()

    def createWorkField(self):
        WindowCreateWorkFeald(self).exec_()
