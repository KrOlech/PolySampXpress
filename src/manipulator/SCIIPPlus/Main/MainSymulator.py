from src.manipulator.SCIIPPlus.Abstract.Main import SCIManipulator


class SCIManipulatorSimulator(SCIManipulator):

    def __init__(self, screenSize, *args, **kwargs):
        super().__init__(screenSize, *args, **kwargs)
        self.init(self.dll.acsc_OpenCommSimulator(), 1)

    def close(self):
        self.dll.acsc_CloseSimulator()

    def homeAxis(self):
        self.setZero()
        self.x = self.getPosition(1)
        self.y = self.getPosition(0)
        self.x0, self.y0, self.z0 = self.getPosition(1), self.getPosition(0), 0
        self.upadteLable()
