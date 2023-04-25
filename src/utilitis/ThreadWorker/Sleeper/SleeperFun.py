from time import sleep

from PyQt5.QtCore import pyqtSignal, QThread

from src.utilitis.ThreadWorker.Sleeper.SimpleSleeper import SimpleSleeper


class SleeperFun(SimpleSleeper):
    finished = pyqtSignal()

    def __init__(self, master, time, *args, **kwargs):
        super(SleeperFun, self).__init__(master, time, *args, **kwargs)

    def run(self):
        self.loger(f"[THREAD DELAY] - [SleeperFun WORKER] START SLEEP {self.time}s")
        sleep(self.time)
        self.loger("[THREAD DELAY] - [SimpleSleeper WORKER] SLEEP END")
        self.finished.emit()

    def logStart(self, fun):
        self.loger(f"[THREAD DELAY] - START {fun.func_name}")

    def logEnd(self, fun):
        self.loger(f"[THREAD DELAY] - END {fun.func_name}")


def createSleeperFun(master, time, fun=None):
    master.thread = QThread()
    master.worker = SleeperFun(master, time)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.thread.started.connect(master.worker.logStart)
    master.worker.finished.connect(master.worker.logEnd)
    master.worker.finished.connect(fun)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workSleeperFun(master, time, fun=None):
    createSleeperFun(master, time, fun)
    with master.lock:
        master.thread.start()
