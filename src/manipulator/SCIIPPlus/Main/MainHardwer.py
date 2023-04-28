import asyncio
from ctypes import c_char_p

from src.manipulator.SCIIPPlus.Abstract.Main import SCIManipulator
from src.utilitis.JsonRead.JsonRead import JsonHandling


class SCIManipulatorMain(SCIManipulator, JsonHandling):

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.init(self.dll.acsc_OpenCommEthernetTCP(c_char_p(b"10.0.0.100"), 701), 1)
        self.x = self.getPosition(1)
        self.y = self.getPosition(0)
        self.x0, self.y0, self.z0 = self.getPosition(1), self.getPosition(0), 0
        self.upadteLable()
        self.__readPositionFromFile()

    def homeAxis(self):
        self.x = -200
        self.y = -200
        asyncio.run(self.goto())
        self.setZero()
        self.x = self.getPosition(1)
        self.y = self.getPosition(0)
        self.x0, self.y0, self.z0 = self.getPosition(1), self.getPosition(0), 0
        self.upadteLable()

    def __readPositionFromFile(self):
        x, y = self.readManipulatorPosition()
        self.setPositions({1: x, 0: y})
        self.upadteLable()

    def close(self):
        self.disableAllAxis()
