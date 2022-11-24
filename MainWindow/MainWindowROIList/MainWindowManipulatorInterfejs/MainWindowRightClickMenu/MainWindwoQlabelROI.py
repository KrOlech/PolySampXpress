from PyQt5.QtWidgets import QWidget, QVBoxLayout
from MainWindow.MainWindowROIList.MainWindowManipulatorInterfejs.MainWindowRightClickMenu.MainWindowCameraGUI.CameraGUI import CameraGUI
from MainWindow.MainWindowROIList.MainWindowManipulatorInterfejs.QlabelExtendetManipulatorMenu import QlabelRightClickMenu


class CameraGUIextention(CameraGUI):

    windowSize = None

    def __init__(self, windowsize, *args, **kwargs) -> None:
        super(CameraGUIextention, self).__init__(*args, **kwargs)

        self.windowSize = windowsize

        self.setFixedSize(windowsize)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.cameraView = QlabelRightClickMenu(self)
        self.cameraView.setFixedSize(windowsize)

        self.layout_box = QVBoxLayout(self.widget)
        self.layout_box.setContentsMargins(0, 0, 0, 0)
        self.layout_box.addWidget(self.cameraView)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = CameraGUIextention(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
