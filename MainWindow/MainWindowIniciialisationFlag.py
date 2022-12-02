from PyQt5.QtWidgets import QDesktopWidget

from MAP.GUI.MapWindow import MapWindow
from MainWindow.MainWindowROIList.MainWindowROIList import MainWindowROIList


class MainWindowInicialisationFlag(MainWindowROIList):
    fildParams = 0

    mapWindowObject = None

    def __init__(self, *args, **kwargs):
        super(MainWindowInicialisationFlag, self).__init__(*args, **kwargs)

        showMap = self.qActionCreate("Show Map", self.showMap)
        createMapAction = self.qActionCreate("Create Map", self.createMap)

        mapMenu = self.menu.addMenu("&MAP")
        mapMenu.addAction(showMap)
        mapMenu.addAction(createMapAction)

    def createMap(self):
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
        else:
            x = self.manipulator.x
            y = self.manipulator.y
            self.mapWindowObject.addFreame(self.camera.getFrame(), y, x)

    def showMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.move(QDesktopWidget().availableGeometry().topLeft())
            self.mapWindowObject.show()

    def setPoleRobocze(self, fildParams):
        self.fildParams = fildParams

    def crateMapObject(self):
        return MapWindow(self, self.windowSize)
