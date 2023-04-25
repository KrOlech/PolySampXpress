from time import sleep

from PyQt5.QtCore import QObject, QThread, pyqtSignal

from src.MainWindow.Utilitis.QlabelROI import QlabelROI


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, mainwindow, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.mainWindow = mainwindow

    def run(self):
        sleep(0.01)
        self.mainWindow.hideRightClickButtons()
        self.finished.emit()


class QlabelRightClickMenu(QlabelROI):

    def right_menu(self, pos):
        self.mainWindow.rightMenu(pos)

        super(QlabelRightClickMenu, self).right_menu(pos)

    def hideRightClickButtons(self):
        self.thread = QThread()
        self.worker = Worker(self.mainWindow)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
