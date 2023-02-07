from PyQt5.QtWidgets import QDesktopWidget
from MAP.Main.MapWindow import MapWindow
from MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from utilitis.Depracation.DepractionFactory import deprecated


class MainWindowMapInterfejs(MainWindowInicialisationFlag):

    selectedManipulatorZoom = 0

    def __init__(self, *args, **kwargs):
        super(MainWindowMapInterfejs, self).__init__(*args, **kwargs)

        showMap = self.qActionCreate("Show Map", self.showMap)
        createMapAction = self.qActionCreate("Create Map", self.createMap)

        mapMenu = self.menu.addMenu("&MAP")
        mapMenu.addAction(showMap)
        mapMenu.addAction(createMapAction)
        # TODO workFieald Change during operation

    @deprecated("old Map cration manual")
    def createMapManual(self):
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
        else:
            x = self.manipulator.x
            y = self.manipulator.y
            self.mapWindowObject.addFrame(self.camera.getFrame(), y, x)

    def createMap(self):
        if not self.mapWindowObject:
            self.mapWindowObject = self.crateMapObject()
            self.mapWindowObject.mapCreate()
        else:
            print("do you wont to ower ride created Map?")
            # ToDo implement Correct in the future

    def showMap(self):
        if self.mapWindowObject:
            self.mapWindowObject.move(QDesktopWidget().availableGeometry().topLeft())
            self.mapWindowObject.show()

    def crateMapObject(self):
        return MapWindow(self, self.windowSize, self.manipulator)
