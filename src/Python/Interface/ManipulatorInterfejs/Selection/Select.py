from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Python.BackEnd.Manipulator.SCIIPPlus.Main.MainHardwer import SCIManipulatorMain
from src.Python.BackEnd.Manipulator.Standa.StandaManipulator import StandaManipulator
from src.Python.BackEnd.Manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator


class SelectManipulator:
    _manipulator = None
    _focusManipulator = None

    FOCUS_MANIPULATOR_ADDRESS = "xi-com:\\\.\COM3".encode()
    ZOOM_MANIPULATOR_ADDRESS = "xi-com:\\\.\COM4".encode()

    def resolveManipulator(self):

        self.zoom_Position = JsonHandling.loadZoomLocationJson()
        self.fokus_Position = JsonHandling.loadFokusLocationJson()

        #self._manipulator = SCIManipulatorMain(self.windowSize, self.myStatusBar)
        #if not self._manipulator.initState:
        self._manipulator = AbstractManipulator(self.windowSize, self.myStatusBar)

        #self._focusManipulator = StandaManipulator(self.FOCUS_MANIPULATOR_ADDRESS, self.windowSize, self.myStatusBar)
        #if not self._focusManipulator.manipulatorConnected:
        self._focusManipulator = AbstractManipulator(self.windowSize, self.myStatusBar)

        #self._zoomManipulator = StandaManipulator(self.ZOOM_MANIPULATOR_ADDRESS, self.windowSize, self.myStatusBar)
        #if not self._zoomManipulator.manipulatorConnected:
        self._zoomManipulator = AbstractManipulator(self.windowSize, self.myStatusBar)

    def closeAction(self):
        if self._manipulator:
            self._manipulator.close()

        if self._focusManipulator:
            JsonHandling.saveFokusLocationJson(self._focusManipulator.x)
            self._focusManipulator.close()

        if self._zoomManipulator:
            try:
                JsonHandling.saveZoomLocationJson(
                    self._zoomManipulator.StepZoomsMap[self._zoomManipulator.x])
            except AttributeError as e:
                print(e)
            self._zoomManipulator.close()
