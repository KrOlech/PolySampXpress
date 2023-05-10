from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel

from src.MainWindow.Utilitis.WindowBar import MyBar
from src.utilitis.Slider.Slider import Slider


class CameraSettingsWindow(QWidget):

    def __init__(self, master, *args, **kwargs) -> None:
        super(CameraSettingsWindow, self).__init__(*args, **kwargs)

        self.master = master

        self.mainLayout = QVBoxLayout()

        for communicationPoint in self.master.camera.communicationPoints:
            self.simplyConfig = QHBoxLayout()

            self.simplyConfig.addWidget(Slider(self.master, communicationPoint))
            self.simplyConfig.addWidget(QLabel(communicationPoint.name))

            self.mainLayout.addLayout(self.simplyConfig)

        self.setLayout(self.mainLayout)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Camera Settings")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())
