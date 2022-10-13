from MainWindow.MainWindowManipulatorInterfejs.MainWindowRightClickMenu.MainWindowCameraGUI.MainWindowCustomBar.qMainWindow.MainWindowCustomBar import MainWindowCustomBar
from PyQt5.QtWidgets import QAction
from abc import abstractmethod
from abc import ABCMeta
from utilitis.Abstract import abstractmetod


class MainWindowMenuBar(MainWindowCustomBar):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindowMenuBar, self).__init__(*args, **kwargs)

        self.menu = self.menuBar()

        listROI = self.qActionCreate("List ROI", self.showListOfROI)
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

    def qActionCreate(self, name: str, triggerFun) -> QAction:
        qAction = QAction(name, self)
        qAction.triggered.connect(triggerFun)
        return qAction

    @abstractmethod
    def showAllCameraSettings(self):
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
    def showROIList(self, e):
        abstractmetod()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = MainWindowMenuBar()

    window.show()

    app.exec_()
