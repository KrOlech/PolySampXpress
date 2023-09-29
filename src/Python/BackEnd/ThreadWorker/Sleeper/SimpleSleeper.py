import asyncio
from asyncio import sleep

from PyQt5.QtCore import pyqtSignal, QThread

from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleThreadWorker import Worker


class SimpleSleeper(Worker):
    finished = pyqtSignal()

    def __init__(self, master, time, *args, **kwargs):
        super(SimpleSleeper, self).__init__(master, *args, **kwargs)
        self.time = time

    def run(self):
        asyncio.run(self.runAsync())

    async def runAsync(self):
        self.loger(f"[THREAD CONNECT] - [SimpleSleeper WORKER] START")
        try:
            self.loger(f"[THREAD CONNECT] - [SimpleSleeper WORKER] master in motion")
            self.master.inMotion = True
            self.loger(f"[THREAD CONNECT] - [SimpleSleeper WORKER] START SLEEP {self.time}s")
            await sleep(self.time)
            self.loger("[THREAD CONNECT] - [SimpleSleeper WORKER] SLEEP END")
            self.master.inMotion = False
            self.loger(f"[THREAD CONNECT] - [SimpleSleeper WORKER] master not in motion")
        except Exception as e:
            self.logError(e)

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
    with master.lock:
        try:
            master.thread.start()
        except Exception as e:
            print(e)
