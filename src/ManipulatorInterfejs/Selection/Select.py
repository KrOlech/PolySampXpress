from src.Manipulator.SCIIPPlus.Main.MainHardwer import SCIManipulatorMain
from src.Manipulator.SCIIPPlus.Main.MainSymulator import SCIManipulatorSimulator
from src.Manipulator.Standa.StandaManipulator import StandaManipulator
from src.Manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator


class SelectManipulator:
    _manipulator = None
    _focusManipulator = None

    def resolveManipulator(self):
        self._manipulator = SCIManipulatorMain(self.windowSize, self.myStatusBar)
        if not self._manipulator.initState:
            self._manipulator = SCIManipulatorSimulator(self.windowSize, self.myStatusBar)
            # todo in the futuer SCIManipulatorSimulator

        self._focusManipulator = StandaManipulator(self.windowSize, self.myStatusBar)
        if not self._focusManipulator.manipulatorConected:
            self._focusManipulator = AbstractManipulator(self.windowSize, self.myStatusBar)
            # todo in the futuer Corect Standa Symulator

    def closeAction(self):
        if self._manipulator:
            self._manipulator.close()

        if self._focusManipulator:
            self._focusManipulator.close()
