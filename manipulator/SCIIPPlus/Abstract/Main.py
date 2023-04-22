from abc import ABCMeta
from ctypes import CDLL

from manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from manipulator.SCIIPPlus.CPPClasys.DllFunction.DllFunction import DllFunctions


class SCIManipulator(AbstractManipulator, DllFunctions):
    __metaclass__ = ABCMeta

    handle = -1

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.dll = CDLL(r"C:\Windows\System32\ACSCL_x64.dll")

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
        self.checkAxisStateM()
        super().goto()

    def gotoNotAsync(self):
        self.goToMain()
        self.checkAxisStateM()
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

    def waitForTarget(self):
        while self.getMotorStateM([0, 1]):
            pass
        return None
