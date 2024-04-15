import asyncio

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QComboBox, QLabel

from Python.BaseClass.Depracation.DepractionFactory import deprecated
from Python.Zoom.Interface.ZoomInterface import ZoomInterface
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowZoom(MainWindowAbstract):
    __zoomSlider = None
    zoom = 0.85

    # todo Unificacja
    labelsDictionary = {0: 0.85, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    def createZoom(self):
        self.zoomInterface = ZoomInterface(self)

        self.zooms = QComboBox()
        self.zooms.setFocusPolicy(Qt.NoFocus)
        self.zooms.activated.connect(self.zoomChangeActionMenu)

        self.toolBar.addWidget(QLabel("ZOOM: "))
        self.toolBar.addWidget(self.zooms)

        self.zooms.addItems([str(i) for i in [0.85, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    @deprecated("old unrealable metode")
    def createZoomSlider(self):
        self.__zoomSlider = self.zoomInterface.createZoomSlider()

        self.__zoomSlider.move(self.geometry().bottomRight()
                               - self.__zoomSlider.geometry().bottomRight()
                               - QPoint(5, 35))

        self.__zoomSlider.show()

    def zoomChangeActionMenu(self, i):
        self.zoom = float(self.zooms.itemText(i))

        asyncio.run(self.manipulatorInterferes.zoomManipulatorChange(self.zoom))
        self.zoomInterface.zoomLabel.setText(str(self.labelsDictionary[self.zoom]))
