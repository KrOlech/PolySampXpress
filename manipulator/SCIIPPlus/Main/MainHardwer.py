from ctypes import c_char_p

from manipulator.SCIIPPlus.Main.Main import SCIManipulator


class SCIManipulatorMain(SCIManipulator):

    def __init__(self, screenSize):
        super().__init__(screenSize)
        self.setSpeed(1)
        self.handle = self.dll.acsc_OpenCommEthernetTCP(c_char_p(b"10.0.0.100"), 701)

    def close(self):
        self.dll.acsc_CloseSimulator()
