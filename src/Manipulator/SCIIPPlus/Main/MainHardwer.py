import asyncio

from src.Manipulator.SCIIPPlus.Abstract.Main import SCIManipulator
from src.BaseClass.JsonRead.JsonRead import JsonHandling


class SCIManipulatorMain(SCIManipulator, JsonHandling):

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.init(self.dll.acsc_OpenCommEthernetTCP(self.IP, 701), 1)
        self.x0, self.y0 = self.getPosition(1), self.getPosition(0)
        self.upadteLable()
        self.__readPositionFromFile()

    def homeAxis(self):
        self.x, self.y = -200, -200

        asyncio.run(self.goto())

        self.setZero()

        self.x0, self.y0 = self.getPosition(1), self.getPosition(0)

        self.upadteLable()

    def __readPositionFromFile(self):
        x, y = self.readManipulatorPosition()
        self.setPositions({1: x, 0: y})
        self.upadteLable()

    def close(self):
        self.disableAllAxis()  # toDo checck in producent code if its ok or I need to do more - works ok for now
