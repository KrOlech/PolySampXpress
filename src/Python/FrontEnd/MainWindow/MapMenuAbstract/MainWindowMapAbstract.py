from Python.BackEnd.MAP.Dialog.NewMapDialog import NewMapDialog
from Python.BackEnd.MAP.Main.MapWindow import MapWindow
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.FunWorkerAsync import workFunWorkerAsync
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract
from Python.FrontEnd.MainWindow.InicialisationFlag.DialogWindowMap import DialogWindowMap


class MainWindowMapAbstract(MainWindowAbstract):
    mapsList = {}

    createMapVariable = None
    isMapReadi = None
    mapWindowObject = None

    creatingMap = False

    mapId = 0

    def closeActionMapMenus(self):
        for mapO in self.mapsList.values():
            mapO.mapWidget.close()

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

            self.__addMenuEntryForMap()

    def endMapCreation(self):
        for mapObject in self.mapsList.values():
            mapObject.mapEnd = True

    def __addMenuEntryForMap(self):
        mapWindowObject = self.__crateMapObject()

        self.dialogWindowMap = DialogWindowMap(self)
        self.dialogWindowMap.run()
        workFunWorkerAsync(self, mapWindowObject.mapCreate)
        self.dialogWindowMap.exec_()

        self.addMap(mapWindowObject)

    def __crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulatorInterferes, self.mapId)

    def addMap(self, mapWindowObject):
        self.abstractmetod()
