import sys
import os
from datetime import datetime

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from PyQt6.uic.properties import QtGui

from Python.BackEnd.Manipulator.Abstract.DialogWindow.InsertSampleDialog import InsertSampleDialog
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger
from Python.FrontEnd.MainWindow.Main.Main import MainWindow


class m(Loger):  # TODO better name
    mainWindow = None

    def __init__(self):
        pass

    def mainNoTryCahch(self):

        self.app = QApplication(sys.argv)

        self.app.setApplicationDisplayName("PolySampXpress 0.7.3")

        self.icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))

        self.app.setWindowIcon(self.icon)

        screenSize = self.app.primaryScreen().availableGeometry().size()

        self.loger(f"res {screenSize} {type(screenSize)}")  # QSize(640, 640)

        self.mainWindow = MainWindow(screenSize)
        self.mainWindow.setWindowIcon(self.icon)

        self.mainWindow.showMaximized()

        self.mainWindow.show()

        InsertSampleDialog(self.mainWindow).exec()

        self.app.exec()

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

        workDir = f"{os.path.expanduser('~')}\\Documents\\PolySampXpress\\{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"
        try:
            os.mkdir(workDir)
        except FileExistsError:
            pass
        os.chdir(workDir + "\\")
        self.mainNoTryCahch()


if __name__ == '__main__':
    m().main()
    # cProfile.run("main()", filename='my_profile.prof')
