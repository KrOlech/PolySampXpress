from abc import ABCMeta
from abc import abstractmethod

from MainWindow.CustomBar.MainWindowCustomBar import MainWindowCustomBar
from MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract
from utilitis.Abstract import abstractmetod


class MainWindowMenuBar(MainWindowCustomBar, MainWindowAbstract):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindowMenuBar, self).__init__(*args, **kwargs)

        self.menu = self.menuBar()

        listROI = self.qActionCreate("List ROI", self.showROIListButton)
        loadROI = self.qActionCreate("Save ROI List", self.loadListOfROI)
        SaveROI = self.qActionCreate("Load ROI list", self.saveListOfROI)

        fileMenu = self.menu.addMenu("&File")
        fileMenu.addAction(listROI)
        fileMenu.addAction(loadROI)
        fileMenu.addAction(SaveROI)

        undo = self.qActionCreate("Undo", self.WIP)
        redo = self.qActionCreate("Redo", self.WIP)
        editMenu = self.menu.addMenu("&Edit")
        editMenu.addAction(undo)
        editMenu.addAction(redo)

        cameraSettings = self.qActionCreate("&All settings", self.showAllCameraSettings)
        cameraMenu = self.menu.addMenu("&Camera settings")
        cameraMenu.addAction(cameraSettings)

        cameraCalibration = self.qActionCreate("&Calibration", self.calibrate)
        cameraMenu.addAction(cameraCalibration)

    @abstractmethod
    def showAllCameraSettings(self):
        abstractmetod()

    @abstractmethod
    def calibrate(self):
        abstractmetod()

    @abstractmethod
    def showListOfROI(self):
        abstractmetod()

    @abstractmethod
    def loadListOfROI(self):
        abstractmetod()

    @abstractmethod
    def saveListOfROI(self):
        abstractmetod()

    def WIP(self):
        pass

    @abstractmethod
    def showROIListButton(self, e):
        abstractmetod()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = MainWindowMenuBar()

    window.show()

    app.exec_()
