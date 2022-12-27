from PyQt5.QtCore import QThread

from utilitis.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class FunWorker(Worker):

    def __init__(self, master, fun, *args, **kwargs):
        super(FunWorker, self).__init__(master, *args, **kwargs)
        self.fun = fun

    def run(self):
        self.fun()
        self.finished.emit()


def createFunWorker(master, fun):
    master.thread = QThread()
    master.worker = FunWorker(master, fun)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def workFunWorker(master, fun):
    createFunWorker(master, fun)
    master.thread.start()
