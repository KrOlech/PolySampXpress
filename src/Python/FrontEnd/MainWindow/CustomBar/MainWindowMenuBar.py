from abc import ABCMeta
from abc import abstractmethod

from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract
from Python.FrontEnd.MainWindow.CustomBar.MainWindowCustomBar import MainWindowCustomBar


class MainWindowMenuBar(MainWindowCustomBar, MainWindowAbstract):
    __metaclass__ = ABCMeta

    def __init__(self, windowSize, *args, **kwargs) -> None:
        super(MainWindowMenuBar, self).__init__(*args, **kwargs)

        self.menu = self.menuBar()

        self.windowSize = windowSize

        #listROI = self.qActionCreate("List ROI", self.showROIListButton) #todo extra info window on ROIs
        loadROI = self.qActionCreate("Save ROI List", self.saveListOfROI)
        SaveROI = self.qActionCreate("Load ROI list", self.loadListOfROI)

        fileMenu = self.menu.addMenu("&File")
        # fileMenu.addAction(listROI) #todo extra info window on ROIs
        fileMenu.addAction(loadROI)
        fileMenu.addAction(SaveROI)

        cameraSettings = self.qActionCreate("&All settings", self.showAllCameraSettings)
        self.cameraMenu = self.menu.addMenu("&Camera settings")
        self.cameraMenu.addAction(cameraSettings)

        cameraCalibration = self.qActionCreate("&Calibration", self.calibrate)
        self.cameraMenu.addAction(cameraCalibration)

        saveCurrentFrame = self.qActionCreate("&Save Current Frame", self.saveCurrentFrame)
        self.cameraMenu.addAction(saveCurrentFrame)

    @abstractmethod
    def showAllCameraSettings(self):
        self.abstractmetod()

    @abstractmethod
    def calibrate(self):
        self.abstractmetod()

    @abstractmethod
    def saveCurrentFrame(self):
        self.abstractmetod("saveCurrentFrame")

    @abstractmethod
    def showListOfROI(self):
        self.abstractmetod()

    @abstractmethod
    def loadListOfROI(self):
        self.abstractmetod()

    @abstractmethod
    def saveListOfROI(self):
        self.abstractmetod()

    def WIP(self):
        pass

    @abstractmethod
    def showROIListButton(self, e):
        self.abstractmetod()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = MainWindowMenuBar()

    window.show()

    app.exec_()
