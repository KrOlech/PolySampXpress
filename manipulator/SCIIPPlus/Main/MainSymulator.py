from manipulator.SCIIPPlus.Abstract.Main import SCIManipulator


class SCIManipulatorSimulator(SCIManipulator):

    def __init__(self, screenSize):
        super().__init__(screenSize)
        self.init(self.dll.acsc_OpenCommSimulator(), 1)

    def close(self):
        self.dll.acsc_CloseSimulator()
