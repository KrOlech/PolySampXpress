import asyncio
from abc import ABCMeta
from ctypes import CDLL

from src.manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from src.manipulator.SCIIPPlus.CPPClasys.DllFunction.DllFunction import DllFunctions


class SCIManipulator(AbstractManipulator, DllFunctions):
    __metaclass__ = ABCMeta

    handle = -1

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.dll = CDLL(r"C:\Windows\System32\ACSCL_x64.dll")
        self.xOffset, self.yOffset = self.loadOffsetsJson()

    def init(self, handle, speed):
        self.setSpeed(speed)
        self.handle = handle
        if self.handle == -1:
            self.logError("no Manipulator Connected Error during Connection")
        self.enableAllAxis()

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def validateSpeed(self, speed):
        self.loger("to Implement")
        return True

    async def goto(self):
        self.goToMain()

    def gotoNotAsync(self):
        self.goToMain()
        super().gotoNotAsync()

    def goToMain(self):
        if not self.getMotorStateM([1, 0]):
            self.goToPointM({1: self.x, 0: self.y})
            self.loger({1: self.x, 0: self.y})
            self.waitForTarget()
            self.x = self.getPosition(1)
            self.y = self.getPosition(0)
            self.loger({1: self.x, 0: self.y})
        else:
            self.loger("erorre")

        if self.checkAxisStateM():
            self.x = self.getPosition(1)
            self.y = self.getPosition(0)

    def waitForTarget(self):
        while self.getMotorStateM([0, 1]):
            pass
        return None
