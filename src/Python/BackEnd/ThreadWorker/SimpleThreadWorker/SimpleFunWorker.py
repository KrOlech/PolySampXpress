from PyQt5.QtCore import QThread

from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class FunWorker(Worker):

    def __init__(self, master, fun, *args, **kwargs):
        super(FunWorker, self).__init__(master, *args, **kwargs)
        self.fun = fun

    def run(self):
        self.loger(f"[THREAD FUN]  START {self.fun.__name__}")
        self.fun()
        self.loger(f"[THREAD FUN] END {self.fun.__name__}")
        self.finished.emit()


def createFunWorker(master, fun, funEnd):
    master.thread = QThread()
    master.worker = FunWorker(master, fun)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(funEnd)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workFunWorker(master, fun, funEnd=None):
    if funEnd is None:
        funEnd = lambda x=0: x
    createFunWorker(master, fun, funEnd)
    master.thread.start()
