from time import sleep

from PySide2.QtCore import Signal, QThread

from utilitis.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class SimpleSleeper(Worker):
    finished = Signal()

    def __init__(self, master, time, *args, **kwargs):
        super(SimpleSleeper, self).__init__(master, *args, **kwargs)
        self.time = time

    def run(self):
        self.master.inMotion = True
        sleep(self.time)
        self.master.inMotion = False
        self.finished.emit()


def createSimpleSleeper(master, time):
    master.thread = QThread()
    master.worker = SimpleSleeper(master, time)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)

def simplySleep(master, time):
    createSimpleSleeper(master, time)
    master.thread.start()
