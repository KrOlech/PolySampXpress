import asyncio

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QComboBox, QLabel

from Python.BaseClass.Depracation.DepractionFactory import deprecated
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.Utilitis.GenericProgressClass import GenericProgressClass
from Python.Zoom.Interface.ZoomInterface import ZoomInterface
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowZoom(MainWindowAbstract):
    __zoomSlider = None
    autoZoomMode = None
    zoom = 0.85

    # todo Unificacja
    labelsDictionary = {0.85: 0.85, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}


    def createZoom(self):
        self.zoomInterface = ZoomInterface(self)

        self.zooms = QComboBox()
        self.zooms.setFocusPolicy(Qt.NoFocus)
        self.zooms.activated.connect(self.zoomChangeActionMenu)

        self.toolBar.addWidget(QLabel("ZOOM: "))
        self.toolBar.addWidget(self.zooms)

        self.zooms.addItems([str(i) for i in [0.85, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

        self.zoom = str(int(JsonHandling.loadZoomLocationJson()))
        self.loger(f"readed zoom {self.zoom}")
        self.zooms.setCurrentText(self.zoom)

    def zoomChangeActionMenu(self, i):
        self.zoom = float(self.zooms.itemText(i))

        if self.autoZoomMode:
            self.manipulatorInterferes.syncZoomManipulatorChange(i)
            return

        self.setStepSize(i)

        window = GenericProgressClass("Zoom in progress", self.zoomChangeAction, 150, self)
        window.run()
        window.exec_()

    def zoomChangeAction(self):
        asyncio.run(self.manipulatorInterferes.zoomManipulatorChange(self.zoom))
