import asyncio

from PyQt5.QtCore import QThread

from src.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class FunWorkerAsync(Worker):

    def __init__(self, master, fun, *args, **kwargs):
        super(FunWorkerAsync, self).__init__(master, *args, **kwargs)
        self.fun = fun

    def run(self):
        self.loger(f"[THREAD FUN] - [FunWorker] START {self.fun.__name__}")
        asyncio.run(self.fun())
        self.loger(f"[THREAD FUN] - [FunWorker] END {self.fun.__name__}")
        self.finished.emit()


def createFunWorker(master, fun):
    master.thread = QThread()
    master.worker = FunWorkerAsync(master, fun)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workFunWorkerAsync(master, fun):
    createFunWorker(master, fun)
    master.thread.start()
