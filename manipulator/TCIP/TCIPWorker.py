import asyncio
from asyncio import sleep

from PyQt5.QtCore import QThread

from utilitis.ThreadWorker.Sleeper.SimpleSleeper import simplySleep
from utilitis.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class TCIPWorker(Worker):

    async def runasync(self):
        print("[THREAD CONNECT] - [TCIP WORKER] START CONNECTION")
        self.master.conn, self.master.addr = self.master.socket.accept()
        print("[THREAD CONNECT] - [TCIP WORKER] CONNECTION STARTED")
        await sleep(4)
        print("[THREAD CONNECT] - [TCIP WORKER] THREAD END")
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
