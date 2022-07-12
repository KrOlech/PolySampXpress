from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from Camera import Camera
from CameraSetings import CameraSettingsWindow
from View import SimpleView
from PyQt5 import QtWidgets, QtCore
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.camera = Camera()

        self.view = SimpleView(self)

        self.setCentralWidget(self.view)

        self.widget = CameraSettingsWindow(self)

        menu = self.menuBar()

        cameraSettings = self.qActionCreate("&All settings", self.showAllCameraSettings)
        file_menu = menu.addMenu("&Camera settings")
        file_menu.addAction(cameraSettings)

        self.showMaximized()

    def showAllCameraSettings(self, a) -> None:
        self.widget.show()

    def qActionCreate(self, name: str, triggerFun) -> QAction:
        qAction = QAction(name, self)
        qAction.triggered.connect(triggerFun)
        return qAction


if __name__ == '__main__':

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    kam = Camera()

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec_()
