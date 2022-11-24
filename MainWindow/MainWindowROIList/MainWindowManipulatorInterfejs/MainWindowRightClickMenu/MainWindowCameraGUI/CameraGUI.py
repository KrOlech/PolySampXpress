from Camera.Camera import Camera
from Camera.CameraSetings import CameraSettingsWindow
from utilitis.examples.View import SimpleView
from PyQt5 import QtWidgets, QtCore
from MainWindow.MainWindowROIList.MainWindowManipulatorInterfejs.MainWindowRightClickMenu.MainWindowCameraGUI.MainWindowCustomBar.MainWindowMenuBar import \
    MainWindowMenuBar


class CameraGUI(MainWindowMenuBar):

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUI, self).__init__(*args, **kwargs)

        self.camera = Camera()

        self.view = SimpleView(self)

        self.setCentralWidget(self.view)

        self.cameraSetingsWidget = CameraSettingsWindow(self)

    def showAllCameraSettings(self) -> None:
        self.cameraSetingsWidget.show()


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
