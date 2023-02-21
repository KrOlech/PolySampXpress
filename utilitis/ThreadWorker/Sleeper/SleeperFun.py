from time import sleep

from PyQt5.QtCore import pyqtSignal, QThread

from utilitis.ThreadWorker.Sleeper.SimpleSleeper import SimpleSleeper


class SleeperFun(SimpleSleeper):
    finished = pyqtSignal()

    def __init__(self, master, time, *args, **kwargs):
        super(SleeperFun, self).__init__(master, time, *args, **kwargs)

    def run(self):
        print(f"[THREAD DELAY] - [SleeperFun WORKER] START SLEEP {self.time}s")
        sleep(self.time)
        print("[THREAD DELAY] - [SimpleSleeper WORKER] SLEEP END")
        self.finished.emit()

def logStart(fun):
    print(f"[THREAD DELAY] - [FunWorker] START {fun.func_name}")

def logEnd(fun):
    print(f"[THREAD DELAY] - [FunWorker] END {fun.func_name}")

def createSleeperFun(master, time, fun=None):
    master.thread = QThread()
    master.worker = SleeperFun(master, time)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.thread.started.connect(logStart)
    master.worker.finished.connect(logEnd)
    master.worker.finished.connect(fun)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workSleeperFun(master, time, fun=None):
    createSleeperFun(master, time, fun)
    with master.lock:
        master.thread.start()

