from PyQt5.QtWidgets import QDesktopWidget

from Python.BackEnd.MAP.Main.MapWindow import MapWindow
from Python.BackEnd.MAP.MapFromFile.MapFromFile import MapFromFile
from Python.BackEnd.ROI.RenameWindow.RenameWidnow import ReNameWindow
from Python.FrontEnd.MainWindow.InicialisationFlag.MapFromHearWindow import MapFromHearWindow
from Python.FrontEnd.MainWindow.MapMenuAbstract.MainWindowMapAbstract import MainWindowMapAbstract


class MainWindowMapMenu(MainWindowMapAbstract):
    mapFromHearX = 5
    mapFromHearY = 5

    def createMapMenu(self):
        createMapAction = self.qActionCreate("Create Mozaik", self.createMap)
        createMapFromHearAction = self.qActionCreate("Create Mozaik From Hear", self.createMapFromHear)
        loadMapFromFile = self.qActionCreate("load Mozaik from Fille", self.loadMap)
        self.mozaikBorders = self.qActionCreate("Show Border Lines", lambda _: _, checkable=True)

        self.mozaikBorders.setChecked(False)  # toDo reimplement or remove

        mapMenu = self.menu.addMenu("&Mozaik")
        mapMenu.addAction(createMapAction)
        mapMenu.addAction(createMapFromHearAction)
        mapMenu.addAction(loadMapFromFile)
        mapMenu.addAction(self.mozaikBorders)

    def createMapFromHear(self):
        MapFromHearWindow(self).exec_()

    def loadMap(self):
        newMap = MapFromFile(self, self.windowSize, self.mapId)
        newMap.loadMap()
        self.addMap(newMap)

        newMap.setName(newMap.name)
        self.mapId += 1
