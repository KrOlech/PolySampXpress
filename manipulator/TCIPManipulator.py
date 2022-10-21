import socket as SOCKET
from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from manipulator.AbstractManipulator import AbstractManipulator


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, master, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.master = master

    def run(self):
        self.master.conn, self.master.addr = self.master.socket.accept()
        self.finished.emit()

class TCIPManipulator(AbstractManipulator):
    TCP_IP = '172.30.254.65'
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

    def close(self):
        self.conn.send(self.NONe)
        self.conn.close()

    def goto(self, x, y, z):
        self.conn.send(("x" + str(x)).encode("utf8"))
        self.conn.send(("y" + str(y)).encode("utf8"))

    def validateSpeed(self, speed):
        return speed <= 10

    def center(self, pozycja):
        self.conn.send("x25.0".encode("utf8"))
        self.conn.send("y25.0".encode("utf8"))
        self.conn.send("z25.0".encode("utf8"))

    def getCurentPosytion(self):
        return self.x, self.y, self.z


