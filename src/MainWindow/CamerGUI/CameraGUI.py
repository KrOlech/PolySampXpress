from PyQt5 import QtWidgets, QtCore

from src.Camera.Main.Camera import Camera
from src.Camera.Setings.CameraSetings import CameraSettingsWindow
from src.MainWindow.CustomBar.MainWindowMenuBar import MainWindowMenuBar
from src.Calibration.main.Main import MainCalibrate
from examples.View import SimpleView


class CameraGUI(MainWindowMenuBar):

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUI, self).__init__(*args, **kwargs)

        self.camera = Camera(self.windowSize)

        self.view = SimpleView(self)

        self.setCentralWidget(self.view)

        self.cameraSetingsWidget = CameraSettingsWindow(self)

    def showAllCameraSettings(self) -> None:
        self.cameraSetingsWidget.show()

    def calibrate(self):
        MainCalibrate(self.camera).calibrate(self.manipulatorInterferes)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    window = CameraGUI()

    window.show()

    app.exec_()
