from PyQt5.QtCore import QPoint

from Python.Zoom.Interface.ZoomInterface import ZoomInterface
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowZoom(MainWindowAbstract):
    __zoomSlider = None

    def createZoomSlider(self):
        self.zoomInterface = ZoomInterface(self)

        self.__zoomSlider = self.zoomInterface.createZoomSlider()

        self.__zoomSlider.move(self.geometry().bottomRight()
                               - self.__zoomSlider.geometry().bottomRight()
                               - QPoint(5, 35))

        self.__zoomSlider.show()
