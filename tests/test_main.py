import sys

from PyQt5.QtWidgets import QApplication

from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling

from src.Python.FrontEnd.MainWindow.Main.Main import MainWindow

from time import sleep


def test_Main_Close():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    sleep(5)

    mainWindow.TestClose()


def JsonRead():
    jsonHandler = JsonHandling()

    print(jsonHandler.getFileLocation("test"))

    jsonHandler.readFile(r"CameraConfig.json")
