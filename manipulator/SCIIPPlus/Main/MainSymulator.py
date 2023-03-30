from manipulator.SCIIPPlus.Main.Main import SCIManipulator


class SCIManipulatorSimulator(SCIManipulator):

    def __init__(self, screenSize):
        super().__init__(screenSize)
        self.OpenCommSimulator()

    def close(self):
        self.closeSimulator()
