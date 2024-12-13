from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal


class WorkerQObject(QObject):
    finished = pyqtSignal()

    def __init__(self, mainWindow, *args, **kwargs):
        super(WorkerQObject, self).__init__(*args, **kwargs)
        self.mainWindow = mainWindow

    def run(self):
        sleep(0.01)
        self.mainWindow.hideRightClickButtons()
        self.finished.emit()