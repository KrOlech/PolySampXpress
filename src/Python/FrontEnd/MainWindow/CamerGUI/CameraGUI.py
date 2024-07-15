import cv2 as cv
from PyQt5.QtWidgets import QFileDialog

from PyQt5 import QtWidgets, QtCore

from Python.BackEnd.Camera.Main.Camera import Camera
from Python.BackEnd.Camera.Setings.CameraSetings import CameraSettingsWindow
from Python.FrontEnd.MainWindow.CustomBar.MainWindowMenuBar import MainWindowMenuBar
from Python.BackEnd.Calibration.main.Main import MainCalibrate
from Python.BackEnd.Camera.SimpleViue.View import SimpleView


class CameraGUI(MainWindowMenuBar):

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUI, self).__init__(*args, **kwargs)

        self.camera = Camera(self.windowSize)

        self.view = SimpleView(self)

        self.setCentralWidget(self.view)

        self.cameraSettingsWidget = CameraSettingsWindow(self)

    def showAllCameraSettings(self) -> None:
        self.cameraSettingsWidget.show()

    def saveCurrentFrame(self):
        folderPath, _ = QFileDialog.getSaveFileName(self, "Select Location to save Current Frame", "",
                                                    "BitMap Files (*.png)")
        self.loger(folderPath)
        if folderPath:
            cv.imwrite(folderPath, self.camera.getFrame())

    def calibrate(self):
        MainCalibrate(self.camera, self).calibrate(self.manipulatorInterferes)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QFileDialog
    import sys

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    window = CameraGUI()

    window.show()

    app.exec_()
