import asyncio

from PyQt5.QtWidgets import QDesktopWidget

from MAP.Main.MapWindow import MapWindow
from MainWindow.RoiList.MainWindowROIList import MainWindowROIList
from utilitis.Depracation.DepractionFactory import deprecated
from utilitis.ThreadWorker.SimpleThreadWorker.FunWorkerAsync import workFunWorkerAsync


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
        workFunWorkerAsync(self,self.mapWindowObject.mapCreate)
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
            workFunWorkerAsync(self,self.mapWindowObject.mapCreate)
        else:
            print("do you wont to owe ride created Map?")
            # ToDo implement Correct in the future

    def showMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.move(QDesktopWidget().availableGeometry().topLeft())
            self.mapWindowObject.showMap()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams

    def crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulator)
