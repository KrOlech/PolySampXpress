import socket as SOCKET
from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from manipulator.AbstractManipulator import AbstractManipulator

import threading


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, master, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.master = master

    def run(self):
        self.master.conn, self.master.addr = self.master.socket.accept()
        self.master.wait(4)
        self.finished.emit()


class sleeper(QObject):
    finished = pyqtSignal()

    def __init__(self, master, time, *args, **kwargs):
        super(sleeper, self).__init__(*args, **kwargs)
        self.master = master
        self.time = time

    def run(self):
        self.master.inMotion = True
        sleep(self.time)
        self.master.inMotion = False
        self.finished.emit()


class TCIPManipulator(AbstractManipulator):
    TCP_IP = "172.30.254.65"  # SOCKET.gethostbyname(SOCKET.gethostname())
    TCP_PORT = 22
    BUFFER_SIZE = 1024

    NON = "non"
    NONe = NON.encode("utf8")

    conn = None

    inMotion = True

    def __init__(self):
        self.socket = SOCKET.socket(SOCKET.AF_INET, SOCKET.SOCK_STREAM)
        self.socket.bind((self.TCP_IP, self.TCP_PORT))
        self.socket.listen(1)

        self.thread = QThread()
        self.worker = Worker(self)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        super(TCIPManipulator, self).__init__()

        self.lock = threading.Lock()

    def close(self):
        if self.conn:
            self.conn.send(self.NONe)
            self.conn.close()

    def goto(self):
        with self.lock:
            try:
                if not self.inMotion:
                    self.conn.sendall(("x" + str(self.x)).encode("utf8"))
                    self.conn.sendall(("y" + str(self.y)).encode("utf8"))
                    self.wait(2)

            except AttributeError:
                print("TCIP manipulator not yet connected")
                self.x = 25.0
                self.y = 25.0


    def validateSpeed(self, speed):
        return speed <= 1

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def wait(self, time):

        self.thread1 = QThread()
        self.worker1 = sleeper(self, time)

        self.worker1.moveToThread(self.thread1)

        self.thread1.started.connect(self.worker1.run)
        self.worker1.finished.connect(self.thread1.quit)
        self.worker1.finished.connect(self.worker1.deleteLater)
        self.thread1.finished.connect(self.thread1.deleteLater)

        self.thread1.start()
