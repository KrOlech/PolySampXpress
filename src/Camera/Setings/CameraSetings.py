from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, QPushButton

from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Camera.Setings.CameraSetingsFromProducent import CameraSettingsFromProducent
from src.Camera.Slider.SliderCommunicationPoint import SliderCommunicationPoint
from src.MainWindow.Utilitis.WindowBar import MyBar
from src.BaseClass.Logger.Logger import Loger

class CameraSettingsWindow(QWidget, CameraSettingsFromProducent, Loger):

    def __init__(self, master, *args, **kwargs) -> None:
        super(CameraSettingsWindow, self).__init__(*args, **kwargs)

        self.master = master

        self.form = QFormLayout(self)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Camera Settings")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))
        self.setWindowIcon(icon)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def show(self):
        try:
            if self.master.camera.isConnectionEstablished:
                self.showProducentSettings()
            elif self.master.camera.device is not None:
                for communicationPoint in self.master.camera.communicationPoints:
                    self.form.addRow(QLabel(communicationPoint.name), SliderCommunicationPoint(self.master, communicationPoint))

                self.setLayout(self.form)
                super().show()
        except AttributeError as e:
            self.logError(e)
