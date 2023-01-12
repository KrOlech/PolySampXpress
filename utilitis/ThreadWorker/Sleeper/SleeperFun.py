from time import sleep

from PyQt5.QtCore import pyqtSignal, QThread

from utilitis.ThreadWorker.Sleeper.SimpleSleeper import SimpleSleeper


class SleeperFun(SimpleSleeper):
    finished = pyqtSignal()

    def __init__(self, master, time, fun=None, *args, **kwargs):
        super(SleeperFun, self).__init__(master, *args, **kwargs)
        self.time = time
        self.fun = fun

    def run(self):
        sleep(self.time)
        if self.fun is not None:
            self.fun()
        else:
            self.master.takphoto()
        self.finished.emit()


def createSleeperFun(master, time, fun=None):
    master.thread = QThread()
    master.worker = SleeperFun(master, time, fun)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workSleeperFun(master, time, fun=None):
    createSleeperFun(master, time, fun)
    master.thread.start()
