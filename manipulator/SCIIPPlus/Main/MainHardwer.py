from ctypes import c_char_p

from manipulator.SCIIPPlus.Abstract.Main import SCIManipulator


class SCIManipulatorMain(SCIManipulator):

    def __init__(self, screenSize, label, *args, **kwargs):
        super().__init__(screenSize, label, *args, **kwargs)
        self.init(self.dll.acsc_OpenCommEthernetTCP(c_char_p(b"10.0.0.100"), 701), 1)
        self.x = self.getPosition(1)
        self.y = self.getPosition(0)
        self.x0, self.y0, self.z0 = self.getPosition(1), self.getPosition(0), 0
        self.upadteLable()

    def close(self):
        self.disableAllAxis()
