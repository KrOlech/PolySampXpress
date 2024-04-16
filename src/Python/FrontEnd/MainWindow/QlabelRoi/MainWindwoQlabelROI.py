from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Python.FrontEnd.MainWindow.CamerGUI.CameraGUI import CameraGUI
from Python.FrontEnd.MainWindow.Utilitis.QlabelExtendetManipulatorMenu import QlabelRightClickMenu


class CameraGUIExtension(CameraGUI):
    windowSize = None

    def __init__(self, *args, **kwargs) -> None:
        super(CameraGUIExtension, self).__init__(*args, **kwargs)

        #self.setFixedSize(self.windowSize)

        self.setGeometry(QRect(0,1080,0,1920))

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.cameraView = QlabelRightClickMenu(self)
        #self.cameraView.setFixedSize(self.windowSize)
        self.cameraView.setGeometry(QRect(0,1080,0,1920))

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
