from PyQt5.QtCore import QObject, pyqtSignal, QThread
from abc import abstractmethod

from Python.BaseClass.Logger.Logger import Loger


class Worker(QObject, Loger):
    finished = pyqtSignal()
    master = None

    def __init__(self, master, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.master = master

    @abstractmethod
    def run(self):
        self.abstractmetod()


def createWorker(master):
    master.thread = QThread()
    master.worker = Worker(master)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def work(master):
    createWorker(master)
    master.thread.start()
