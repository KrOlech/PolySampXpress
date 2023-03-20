import asyncio
from asyncio import sleep

from PyQt5.QtCore import QThread

from utilitis.Logger.Logger import Loger
from utilitis.ThreadWorker.Sleeper.SimpleSleeper import simplySleep
from utilitis.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class TCIPWorker(Worker):

    async def runasync(self):
        self.loger("[THREAD CONNECT] START CONNECTION")
        self.master.conn, self.master.addr = self.master.socket.accept()
        self.loger("[THREAD CONNECT] CONNECTION STARTED")
        await sleep(4)
        self.loger("[THREAD CONNECT] THREAD END")
        self.finished.emit()

    def run(self):
        asyncio.run(self.runasync())


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
    with master.lock:
        master.thread.start()
