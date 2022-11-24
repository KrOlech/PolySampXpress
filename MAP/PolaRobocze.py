from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtCore import Qt
from MAP.GUI.PolaRoboczeGUI import PoleRoboczeGui
from utilitis.JsonRead.JsonRead import loadPolaRoboczeJson


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, master, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.master = master

    def run(self):
        while True:
            if self.master.GUI.walueSet:
                self.master.showmain()
                self.finished.emit()
                break


class ReadPoleRobocze:

    def __init__(self, mainWindow):

        self.mainWindow = mainWindow

        workFields = loadPolaRoboczeJson()

        self.GUI = PoleRoboczeGui(workFields)
        self.GUI.setWindowFlag(Qt.Popup)

        self.thread = QThread()
        self.worker = Worker(self)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()


    def show(self):

        self.GUI.show()


    def showmain(self):
        self.mainWindow.setPoleRobocze(self.GUI.fildParamiters)
        self.mainWindow.cameraView.afterInitialisation = True