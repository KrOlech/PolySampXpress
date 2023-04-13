from manipulator.SCIIPPlus.Main.Main import SCIManipulator


class SCIManipulatorSimulator(SCIManipulator):

    def __init__(self, screenSize):
        super().__init__(screenSize)
        self.setSpeed(1)
        self.handle = self.dll.acsc_OpenCommSimulator()

    def close(self):
        self.dll.acsc_CloseSimulator()
