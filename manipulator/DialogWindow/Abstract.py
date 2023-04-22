from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QSpinBox

from MainWindow.Utilitis.WindowBar import MyBar


class AbstractDialog(QDialog):
    __metaclass__ = ABCMeta

    accepted = pyqtSignal(dict)

    @property
    @abstractmethod
    def windowName(self):
        return ""

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.manipulator = manipulator

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, self.windowName)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.form = QFormLayout(self)

        self.okButton = QPushButton('OK')
        self.okButton.clicked.connect(self.okPressed)

        self.cancelButton = QPushButton('Cancel')
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
        spinBox = QSpinBox()
        spinBox.setValue(value)
        spinBox.setRange(0, 20)
        return spinBox
