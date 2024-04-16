from abc import ABCMeta
from ctypes import CDLL

from Python.BackEnd.Manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from Python.BackEnd.Manipulator.SCIIPPlus.CPPClasys.DllFunction.DllFunction import DllFunctions


class SCIManipulator(AbstractManipulator, DllFunctions):
    __metaclass__ = ABCMeta

    handle = -1

    yMovment = None

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.dll = CDLL(self.getFileLocation("Dlls\ACSCL_x64.dll"))

    def init(self, handle, speed):
        self.setSpeed(speed)
        self.handle = handle
        if self.handle == -1:
            self.logError("no master Connected Error during Connection")
            return -1
        self.enableAllAxis()

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def validateSpeed(self, speed):
        # Not needed for now full readability on Manipulator own speed
        return True

    async def goto(self):
        self.goToMain()

    def gotoNotAsync(self):
        self.goToMain()
        super().gotoNotAsync()

    def goToMain(self):
        if not self.getMotorStateM([1, 0]):

            self.loger('SCI Standard', {1: self.x, 0: self.y})

            self.__goToMain()

            self.loger('SCI Corrected', {1: self.x, 0: self.y})
            self.waitForTarget()
            self.x = self.getPosition(1)
            self.y = self.getPosition(0)
            self.loger({1: self.x, 0: self.y})
        else:
            self.logError("Manipulator in motion?")

        if self.checkAxisStateM():
            self.x = self.getPosition(1)
            self.y = self.getPosition(0)

    def __goToMain(self):
        if self.yMovment:
            self.x -= (self.deltaY * 20649 * pow(10, -7))

        self.goToPointM({1: self.x, 0: self.y})

    def waitForTarget(self):
        while self.getMotorStateM([0, 1]):
            pass
        return None

    def stop(self):
        self.stopAllAxis()

    def up(self):
        self.yMovment = True
        self.deltaY = 1
        super().up()
        self.yMovment = False

    def down(self):
        self.yMovment = True
        self.deltaY = -1
        super().down()
        self.yMovment = False

    def goToCords(self, x=None, y=None, z=None):
        self.yMovment = self.y != y and y
        if self.yMovment:
            self.deltaY = y - self.y
        super().goToCords(x, y, z)
        self.yMovment = False

    def goToCordsAsync(self, x=None, y=None, z=None):
        self.yMovment = self.y != y and y
        if self.yMovment:
            self.deltaY = y - self.y
        super().goToCordsAsync(x, y, z)
        self.yMovment = False
