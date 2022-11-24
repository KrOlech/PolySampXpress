from MAP.GUI.MapWindow import MapWindow
from MainWindow.MainWindowROIList.MainWindowROIList import MainWindowROIList


class MainWindowInicialisationFlag(MainWindowROIList):
    fildParams = 0

    def __init__(self, *args, **kwargs):
        super(MainWindowInicialisationFlag, self).__init__(*args, **kwargs)

        self.mapWindowObject = self.crateMapObject()

        showMap = self.qActionCreate("Show Map", self.showMap)
        createMapAction = self.qActionCreate("Create Map", self.createMap)

        mapMenu = self.menu.addMenu("&MAP")
        mapMenu.addAction(showMap)
        mapMenu.addAction(createMapAction)

    def createMap(self):
        pass

    def showMap(self):
        self.mapWindowObject.show()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams

    def crateMapObject(self):
        return MapWindow(self, self.windowSize)
