from PySide2.QtWidgets import QWidget, QVBoxLayout
from MainWindow.CamerGUI.CameraGUI import CameraGUI
from MainWindow.Utilitis.QlabelExtendetManipulatorMenu import QlabelRightClickMenu


class CameraGUIExtension(CameraGUI):

    windowSize = None

    def __init__(self, windowSize, *args, **kwargs) -> None:
        super(CameraGUIExtension, self).__init__(*args, **kwargs)

        self.windowSize = windowSize

        self.setFixedSize(windowSize)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.cameraView = QlabelRightClickMenu(self)
        self.cameraView.setFixedSize(windowSize)

        self.layout_box = QVBoxLayout(self.widget)
        self.layout_box.setContentsMargins(0, 0, 0, 0)
        self.layout_box.addWidget(self.cameraView)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = CameraGUIExtension(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
