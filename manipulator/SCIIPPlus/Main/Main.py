from abc import ABCMeta
from ctypes import CDLL

from manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from manipulator.SCIIPPlus.CPPClasys.NewDllFunction.DllFunction import DllFunctions


class SCIManipulator(AbstractManipulator, DllFunctions):
    __metaclass__ = ABCMeta

    def __init__(self, screenSize):
        super().__init__(screenSize)
        self.dll = CDLL(r"C:\Windows\System32\ACSCL_x64.dll")

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def validateSpeed(self, speed):
        self.loger("to Implement")
        return True

    async def goto(self):
        if not self.getMotorState():
            self.getPosition()
            self.getPosition(1)
            print(self.getCurrentPosition())
            self.goToPoint(self.x, axis=0)
            self.goToPoint(self.y, axis=1)
        else:
            print("erorre")

    def gotoNotAsync(self):
        if not self.getMotorState():
            self.getPosition()
            self.getPosition(1)
            print(self.getCurrentPosition())
            self.goToPoint(self.x, axis=0)
            self.goToPoint(self.y, axis=1)
        else:
            print("erorre")

    def waitForTarget(self):
        while self.getMotorState():
            pass
