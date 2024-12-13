from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Python.FrontEnd.MainWindow.CamerGUI.CameraGUI import CameraGUI
from Python.FrontEnd.MainWindow.RightClickMenu.QlabelRightClickMenu import QlabelRightClickMenu


class CameraGUIExtension(CameraGUI):
    windowSize = None

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUIExtension, self).__init__(*args, **kwargs)

        self.setFixedSize(self.windowSize)
        self.move(QPoint(0,0))

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.cameraView = QlabelRightClickMenu(self)

        self.layout_box = QVBoxLayout(self.widget)
        self.layout_box.setContentsMargins(0, 0, 0, 0)
        self.layout_box.addWidget(self.cameraView)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = CameraGUIExtension(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
