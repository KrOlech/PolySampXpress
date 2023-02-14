from time import sleep

from PySide2.QtCore import pyqtSignal, QThread

from utilitis.ThreadWorker.Sleeper.SimpleSleeper import SimpleSleeper


class SleeperFun(SimpleSleeper):
    finished = pyqtSignal()

    def __init__(self, master, time, *args, **kwargs):
        super(SleeperFun, self).__init__(master, time, *args, **kwargs)

    def run(self):
        sleep(self.time)
        self.finished.emit()


def createSleeperFun(master, time, fun=None):
    master.thread = QThread()
    master.worker = SleeperFun(master, time)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(fun)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workSleeperFun(master, time, fun=None):
    with master.lock:
        createSleeperFun(master, time, fun)
        master.thread.start()

