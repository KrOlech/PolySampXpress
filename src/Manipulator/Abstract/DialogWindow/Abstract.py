from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QDoubleSpinBox, QLabel

from src.MainWindow.Utilitis.WindowBar import MyBar


class AbstractDialog(QDialog):
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
        return "Cancel"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, self.windowName)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.form = QFormLayout(self)

        self.okButton = QPushButton(self.okName)
        self.okButton.clicked.connect(self.okPressed)

        self.cancelButton = QPushButton(self.CancelName)
        self.cancelButton.clicked.connect(self.cancelPressed)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def finaliseOutput(self):
        self.form.addRow(self.okButton, self.cancelButton)

    def okPressed(self):
        self.accept()

    def cancelPressed(self):
        self.accept()

    @staticmethod
    def createQSpinBox(value):
        spinBox = QDoubleSpinBox()
        spinBox.setValue(value)
        spinBox.setRange(0, 200)
        return spinBox

    def createWaitingLabel(self):
        self.form.addRow(QLabel("Waiting for Manipulator to reach position"))
