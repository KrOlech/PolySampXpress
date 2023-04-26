import sys

from PyQt5.QtWidgets import QApplication

from src.utilitis.JsonRead.JsonRead import JsonHandling

from src.MainWindow.Main.Main import MainWindow

from time import sleep


def test_Main_Close():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    sleep(5)

    mainWindow.TestClose()



def test_JsonRead():
    jsonHandler = JsonHandling()

    print(jsonHandler.getFileLocation("test"))

    jsonHandler.readFile(r"CameraConfig.json")
