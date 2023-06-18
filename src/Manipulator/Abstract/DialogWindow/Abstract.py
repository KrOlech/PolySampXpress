from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QDoubleSpinBox, QLabel

from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.BaseClass.Logger.Logger import Loger
from src.MainWindow.Utilitis.WindowBar import MyBar


class AbstractDialog(QDialog, Loger):
    __metaclass__ = ABCMeta

    accepted = pyqtSignal(dict)

    @property
    @abstractmethod
    def windowName(self):
        return ""

    @property
    def okName(self):
        return "ok"

    @property
    def CancelName(self):
        return "Stop"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))
        self.setWindowIcon(icon)

        self.titleBar = MyBar(self, self.windowName)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.form = QFormLayout(self)

        self.okButton = QPushButton(self.okName)
        self.okButton.clicked.connect(self.okPressed)

        self.cancelButton = QPushButton(self.CancelName)
        self.cancelButton.clicked.connect(self.cancelPressed)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def finaliseGUI(self):
        self.form.addRow(self.okButton, self.cancelButton)

    @abstractmethod
    def okPressed(self):
        self.accept()

    @abstractmethod
    def cancelPressed(self):
        self.accept()

    @staticmethod
    def createQSpinBox(value, min=0, max=200):
        spinBox = QDoubleSpinBox()
        spinBox.setValue(value)
        spinBox.setRange(min, max)
        return spinBox

    def createWaitingLabel(self):
        self.form.addRow(QLabel("Waiting for Manipulator"))
