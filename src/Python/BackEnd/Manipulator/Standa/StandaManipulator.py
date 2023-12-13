from ctypes import byref

from Python.BackEnd.Manipulator.Standa.InicialisationClass import StandaManipulatorInitialisation
from Python.BackEnd.Manipulator.Standa.ProducerCode.FildsClass import get_position_t


class StandaManipulator(StandaManipulatorInitialisation):

    def __init__(self, device_id_Address, screenSize, *args, **kwargs):
        super().__init__(device_id_Address, screenSize, *args, **kwargs)

        self.setSpeed(100)

        x_pos = get_position_t()
        result = self.lib.get_position(self.device_id, byref(x_pos))
        self.loger("Standa Resived Position: " + repr(result))

        try:
            pos = self.readFile(f"StandaPosition_{self.device_id}.json")
            self.x = pos["x"]
            self.y = pos["y"]
            self.z = pos["z"]
            self.gotoNotAsync()
        except FileNotFoundError as e:
            self.logError(e)
        except KeyError as e:
            self.logError(e)

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def center(self, pozycja, pozycja2):
        self.lib.command_home(self.device_id)

    def validateSpeed(self, speed):
        return True

    async def goto(self):
        self.__goto()

    def gotoNotAsync(self):
        self.__goto()

    def __goto(self):
        self.loger(self.x, self.y, self.z)
        self.lib.command_move(self.device_id, int(self.x), 0)

    def homeAxis(self):
        pass
