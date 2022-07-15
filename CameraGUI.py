from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QVBoxLayout
from Camera import Camera
from CameraSetings import CameraSettingsWindow
from View import SimpleView
from PyQt5 import QtWidgets, QtCore, QtGui
from MainWindowMenuBar import MainWindowMenuBar

import sys


class MainWindow(MainWindowMenuBar):

    def __init__(self,  *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.camera = Camera()

        self.view = SimpleView(self)

        self.setCentralWidget(self.view)

        self.widget = CameraSettingsWindow(self)

        self.showMaximized()


    def showAllCameraSettings(self) -> None:
        self.widget.show()


if __name__ == '__main__':

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec_()
