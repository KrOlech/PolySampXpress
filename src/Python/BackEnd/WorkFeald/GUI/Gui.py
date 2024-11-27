from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QDialog

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.FrontEnd.MainWindow.Utilitis.WindowBar import MyBar
from Python.BackEnd.WorkFeald.Label.Label import WorkFaldLabel


class WorkFilledGui(QDialog):
    valueSet = False
    fildParameters = None

    def __init__(self, workFields, windowSize, *args, **kwargs):
        super(WorkFilledGui, self).__init__(*args, **kwargs)

        self.fildLabels = [WorkFaldLabel(workField, self, windowSize) for workField in workFields]

        self.layout = QHBoxLayout(self)

        [self.layout.addWidget(label) for label in self.fildLabels]
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self, "Work Fild")
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))
        self.setWindowIcon(icon)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

    def setFildParams(self, fildParams):
        self.hide()
        self.valueSet = True
        self.fildParameters = fildParams


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from tests import loadPolaRoboczeJson

    app = QApplication(sys.argv)

    window = WorkFilledGui(loadPolaRoboczeJson())

    window.show()

    app.exec_()
