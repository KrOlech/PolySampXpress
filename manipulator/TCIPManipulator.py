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
        self.finished.emit()

class Worker1(QObject):
    finished = pyqtSignal()

    def __init__(self, master, *args, **kwargs):
        super(Worker1, self).__init__(*args, **kwargs)
        self.master = master

    def run(self):
        data = self.master.socket.recv(self.master.BUFFER_SIZE)
        print(data.decode('utf8'))
        if data.decode('utf8') == "ok":
            print("end of movement")
            self.finished.emit()



class TCIPManipulator(AbstractManipulator):
    TCP_IP = "172.30.254.65"  # SOCKET.gethostbyname(SOCKET.gethostname())
    TCP_PORT = 22
    BUFFER_SIZE = 1024

    NON = "non"
    NONe = NON.encode("utf8")

    conn = None

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
                self.conn.send(("x" + str(self.x)).encode("utf8"))
                self.conn.send(("y" + str(self.y)).encode("utf8"))

                thread = QThread()
                worker = Worker1(self)

                worker.moveToThread(thread)

                thread.started.connect(worker.run)
                worker.finished.connect(thread.quit)
                worker.finished.connect(worker.deleteLater)
                thread.finished.connect(thread.deleteLater)

                thread.start()

            except AttributeError:
                print("TCIP manipulator not yet connected")
                self.x = 25.0
                self.y = 25.0



    def validateSpeed(self, speed):
        return speed <= 10

    def getCurrentPosition(self):
        return self.x, self.y, self.z
