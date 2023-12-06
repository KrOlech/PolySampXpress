from PyQt5.QtCore import QThread

from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import FunWorker


class SimpleMasterFunWorker(FunWorker):
    def run(self):
        self.loger(f"[THREAD FUN]  START {self.fun.__name__}")
        self.fun(self.master)
        self.loger(f"[THREAD FUN] END {self.fun.__name__}")
        self.finished.emit()


def createFunWorkerMaste(master, fun, funEnd):
    master.thread = QThread()
    master.worker = SimpleMasterFunWorker(master, fun)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(funEnd)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workFunWorkerMaster(master, fun, funEnd=None):
    if funEnd is None:
        funEnd = lambda x=0: x
    createFunWorkerMaste(master, fun, funEnd)
    master.thread.start()
