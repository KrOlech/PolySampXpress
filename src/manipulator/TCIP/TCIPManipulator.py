import asyncio
import socket as SOCKET
import threading
from asyncio import sleep

from src.manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from src.manipulator.TCIP.TCIPUtilitiString import TCIPUtilitiString
from src.manipulator.TCIP.TCIPWorker import tcipWork
from src.utilitis.JsonRead.JsonRead import loadOffsetsJson


class TCIPManipulator(AbstractManipulator, TCIPUtilitiString):
    conn = None

    inMotion = False

    x, y, z = 25.0, 25.0, 25.0

    def __init__(self, screenSize, *args, **kwargs):
        self.xOffset, self.yOffset = loadOffsetsJson()
        self.socket = SOCKET.socket(SOCKET.AF_INET, SOCKET.SOCK_STREAM)
        self.socket.bind((self.TCP_IP, self.TCP_PORT))
        self.socket.listen(1)

        self.lock = threading.Lock()
        tcipWork(self)
        self.setSpeed(1)
        super(TCIPManipulator, self).__init__(screenSize, *args, **kwargs)

    def close(self):
        if self.conn:
            self.conn.send(self.NONe)
            self.conn.close()

    async def goto(self):
        with self.lock:
            try:
                if not self.inMotion:
                    self.conn.sendall(("x" + str(self.x)).encode("utf8"))
                    self.conn.sendall(("y" + str(self.y)).encode("utf8"))
                    await sleep(2)
                    # simplySleep(self, 2)

            except AttributeError:
                self.loger("TCIP manipulator not yet connected")
                self.x = 25.0
                self.y = 25.0

    def gotoNotAsync(self):
        with self.lock:
            try:
                if not self.inMotion:
                    self.conn.sendall(("x" + str(self.x)).encode("utf8"))
                    self.conn.sendall(("y" + str(self.y)).encode("utf8"))


            except AttributeError:
                self.loger("TCIP manipulator not yet connected")
                self.x = 25.0
                self.y = 25.0

    def validateSpeed(self, speed):
        return speed <= 1

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    @staticmethod
    async def __wait():
        await sleep(5)

    def waitForTarget(self):
        asyncio.run(self.__wait())

    def homeAxis(self):
        self.x = 0
        self.y = 0
        self.gotoNotAsync()
