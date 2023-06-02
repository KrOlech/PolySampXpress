from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, QPushButton

from src.Camera.Setings.CameraSetingsFromProducent import CameraSettingsFromProducent
from src.Camera.Slider.Slider import Slider
from src.MainWindow.Utilitis.WindowBar import MyBar


class CameraSettingsWindow(QWidget, CameraSettingsFromProducent):

    def __init__(self, master, *args, **kwargs) -> None:
        super(CameraSettingsWindow, self).__init__(*args, **kwargs)

        self.master = master

        self.form = QFormLayout(self)

        for communicationPoint in self.master.camera.communicationPoints:
            self.form.addRow(QLabel(communicationPoint.name), Slider(self.master, communicationPoint))

        self.button = QPushButton(self)
        self.button.released.connect(self.hide)
        self.button.released.connect(self.showProducentSettings)
        self.button.setText("Producent Settings")
        self.form.addRow(QLabel(""), self.button)

        self.setLayout(self.form)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Camera Settings")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.setWhiteBalanceAuto()

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def show(self):
        self.showProducentSettings()
        #for communicationPoint in self.master.camera.communicationPoints:
        #    communicationPoint.setValue(self.master.camera.device)
        #super().show()
