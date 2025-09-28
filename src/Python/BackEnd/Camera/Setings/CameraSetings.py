from Python.BaseClass.Depracation.DepractionFactory import deprecated
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QFormLayout

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BackEnd.Camera.Setings.CameraSetingsFromProducent import CameraSettingsFromProducent
from Python.BackEnd.Camera.Slider.SliderCommunicationPoint import SliderCommunicationPoint
#from Python.FrontEnd.MainWindow.Utilitis.WindowBar import MyBar
from Python.BaseClass.Logger.Logger import Loger

class CameraSettingsWindow(QWidget, CameraSettingsFromProducent, Loger):

    def __init__(self, master, *args, **kwargs) -> None:
        super(CameraSettingsWindow, self).__init__(*args, **kwargs)

        self.master = master

        self.form = QFormLayout(self)

        #self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        #self.titleBar = MyBar(self, "Camera Settings")
        #self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))
        self.setWindowIcon(icon)

    @deprecated
    def resizeEvent_depracated(self, event):
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
