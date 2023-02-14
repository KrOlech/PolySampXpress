from PySide2.QtCore import QThread

from utilitis.ThreadWorker.Sleeper.SimpleSleeper import simplySleep
from utilitis.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class TCIPWorker(Worker):

    def run(self):
        self.master.conn, self.master.addr = self.master.socket.accept()
        simplySleep(self.master, 4)
        self.finished.emit()


def createTCIPWorker(master):
    master.thread = QThread()
    master.worker = TCIPWorker(master)

    master.worker.moveToThread(master.thread)

    master.thread.started.connect(master.worker.run)
    master.worker.finished.connect(master.thread.quit)
    master.worker.finished.connect(master.worker.deleteLater)
    master.thread.finished.connect(master.thread.deleteLater)


def tcipWork(master):
    createTCIPWorker(master)
    master.thread.start()
