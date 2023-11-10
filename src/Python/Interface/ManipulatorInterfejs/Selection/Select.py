from src.Python.BackEnd.Manipulator.SCIIPPlus.Main.MainHardwer import SCIManipulatorMain
from src.Python.BackEnd.Manipulator.Standa.StandaManipulator import StandaManipulator
from src.Python.BackEnd.Manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator


class SelectManipulator:
    _manipulator = None
    _focusManipulator = None

    FOCUS_MANIPULATOR_ADDRESS = "xi-com:\\\.\COM3".encode()
    ZOOM_MANIPULATOR_ADDRESS = "xi-com:\\\.\COM4".encode()

    def resolveManipulator(
            self):  # todo corect resolution of non apstract Manipulators som Wariable set to run Code in symulator mode.
        self._manipulator = SCIManipulatorMain(self.windowSize, self.myStatusBar)
        if not self._manipulator.initState:
            self._manipulator = AbstractManipulator(self.windowSize, self.myStatusBar)
            # todo in the futuer SCIManipulatorSimulator

        self._focusManipulator = StandaManipulator(self.FOCUS_MANIPULATOR_ADDRESS, self.windowSize, self.myStatusBar)
        if not self._focusManipulator.manipulatorConected:
            self._focusManipulator = AbstractManipulator(self.windowSize, self.myStatusBar)
            # todo in the futuer Corect Standa Symulator

        self._zoomManipulator = StandaManipulator(self.ZOOM_MANIPULATOR_ADDRESS, self.windowSize, self.myStatusBar)
        if not self._zoomManipulator.manipulatorConected:
            self._zoomManipulator = AbstractManipulator(self.windowSize, self.myStatusBar)
            # todo in the futuer Corect Standa Symulator

    def closeAction(self):
        if self._manipulator:
            self._manipulator.close()

        if self._focusManipulator:
            self._focusManipulator.close()

        if self._zoomManipulator:
            self._zoomManipulator.close()
