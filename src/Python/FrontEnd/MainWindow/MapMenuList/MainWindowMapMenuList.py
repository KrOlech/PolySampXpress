from PyQt5.QtWidgets import QMenu, QDesktopWidget

from Python.BackEnd.ROI.RenameWindow.RenameWidnow import ReNameWindow
from Python.FrontEnd.MainWindow.MapMenuAbstract.MainWindowMapAbstract import MainWindowMapAbstract


class MainWindowMapMenuList(MainWindowMapAbstract):
    mapListMenu = None

    def createMapMenuList(self):
        self.mapListMenu = QMenu("Mozaik list", self)
        self.menu.addMenu(self.mapListMenu)

    def __createMapMenu(self, mapWindowObject):
        mapMenu = QMenu(str(self.mapId), self)
        mapMenu.addAction(self.qActionCreate("Show", lambda checked, nr=mapWindowObject.mapId: self.showMap(nr)))
        mapMenu.addAction(self.qActionCreate("Remove", lambda checked, nr=mapWindowObject.mapId: self.removeMap(nr)))
        mapMenu.addAction(self.qActionCreate("ReName", lambda checked, nr=mapWindowObject.mapId: self.newNameOfMap(nr)))
        mapMenu.addAction(self.qActionCreate("Save Map", lambda checked, nr=mapWindowObject.mapId: self.saveMap(nr)))
        return mapMenu


    def addMap(self, mapWindowObject):

        self.mapsList[self.mapId] = mapWindowObject

        mapMenu = self.__createMapMenu(mapWindowObject)

        self.mapListMenu.addMenu(mapMenu)
        mapWindowObject.menu = mapMenu

        self.mapId += 1

    def newNameOfMap(self, mapId):
        mapO = self.mapsList[mapId]
        ReNameWindow(mapO, self, text=str(mapO.mapId)).show()

    def saveMap(self, mapId):
        self.mapsList[mapId].saveMapFile()

    def showMap(self, mapId):
        self.mapsList[mapId].move(QDesktopWidget().availableGeometry().topLeft())
        self.mapsList[mapId].showMap()

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