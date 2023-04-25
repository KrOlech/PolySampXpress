import sys

from PyQt5.QtWidgets import QApplication

from MainWindow.Main.Main import MainWindow


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    app.exec_()


def CameraSettingTest():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    mainWindow.showAllCameraSettings()

    app.exec_()
