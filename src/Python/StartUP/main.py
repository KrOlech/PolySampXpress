import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.FrontEnd.MainWindow.Main.Main import MainWindow
from Python.BaseClass.Logger.Logger import Loger


class m(Loger):  # TODO better name
    mainWindow = None

    def __init__(self):
        pass

    def mainNoTryCahch(self):
        self.app = QApplication(sys.argv)

        self.app.setApplicationDisplayName("PolySampXpress 0.7")

        self.icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))

        self.app.setWindowIcon(self.icon)

        self.loger(
            f"res {self.app.desktop().availableGeometry().size()} {type(self.app.desktop().availableGeometry().size())}") #QSize(640, 640)

        self.mainWindow = MainWindow(self.app.desktop().availableGeometry().size())
        self.mainWindow.setWindowIcon(self.icon)

        self.mainWindow.show()

        self.app.exec_()

    def trySavingRoiList(self):
        try:
            if self.mainWindow:
                self.mainWindow.emergancysaveListOfROI()
                self.mainWindow.saveListOfROI()
            else:
                self.logWarning(
                    "ERROR During program runing unable to save ROI list")
        except Exception as e:
            self.logError(e)
            self.logWarning(
                "ERROR During program runing unable to save ROI list")

    def main(self):
        try:
            self.mainNoTryCahch()
        except Exception as e:
            self.logError(e)
            self.logWarning("ERROR During program runing trying to save ROI list")
            self.trySavingRoiList()


if __name__ == '__main__':
    m().main()
    # cProfile.run("main()", filename='my_profile.prof')
