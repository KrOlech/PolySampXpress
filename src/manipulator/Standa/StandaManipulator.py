from asyncio import sleep

from src.manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from src.manipulator.Standa.InicialisationClass import StandaManipulatorInitialisation


class StandaManipulator(AbstractManipulator, StandaManipulatorInitialisation):

    def __init__(self, screenSize, *args, **kwargs):
        AbstractManipulator.__init__(self, screenSize, *args, **kwargs)
        StandaManipulatorInitialisation.__init__(self)
        self.lib.command_home(self.device_id)
        self.setSpeed(100)
        self.__x = 0

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def center(self, pozycja, pozycja2):  # toDo uncorect Functionality implemented only for test purpuse
        self.lib.command_home(self.device_id)

    def validateSpeed(self, speed):
        return True  # TODO

    async def goto(self):
        self.loger(self.x, self.y, self.z)
        self.lib.command_move(self.device_id, self.x, 0)
        await sleep(2)

    def gotoNotAsync(self):
        self.lib.command_move(self.device_id, self.x, 0)

    def homeAxis(self):
        pass  # toDo
