from ctypes import Structure, c_int, c_longlong, byref

from src.Manipulator.Standa.InicialisationClass import StandaManipulatorInitialisation


class StandaManipulator(StandaManipulatorInitialisation):
    class get_position_t(Structure):
        _fields_ = [
            ("Position", c_int),
            ("uPosition", c_int),
            ("EncPosition", c_longlong),
        ]

    def __init__(self, screenSize, *args, **kwargs):
        super().__init__(self, screenSize, *args, **kwargs)
        # self.lib.command_home(self.device_id)
        self.setSpeed(100)

        x_pos = self.get_position_t()
        result = self.lib.get_position(self.device_id, byref(x_pos))
        self.loger("Standa Resived Position: " + repr(result))

    def getCurrentPosition(self):
        return self.x, self.y, self.z

    def center(self, pozycja, pozycja2):  # toDo uncorect Functionality implemented only for test purpuse
        self.lib.command_home(self.device_id)

    def validateSpeed(self, speed):
        return True  # TODO

    async def goto(self):
        self.loger(self.x, self.y, self.z)
        self.lib.command_move(self.device_id, self.x, 0)

    def gotoNotAsync(self):
        self.lib.command_move(self.device_id, int(self.x), 0)

    def homeAxis(self):
        pass  # toDo
