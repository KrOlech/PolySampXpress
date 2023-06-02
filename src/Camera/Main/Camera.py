import cv2

from src.Camera.FromProducent.Main import GetFrameFromProducent
from src.Symulators.CameraSymulator.CameraSimulator import CameraSimulator
from src.Camera.ComonNames.ComonNames import CommonNames
from src.Camera.Configuration.Configuration import Configuration
from src.Camera.GetFrame.GetFrame import GetFrame
from src.BaseClass.JsonRead.JsonRead import JsonHandling
from src.ErrorHandling.CustomExceptions.Exceptions import NoCammeraConected


class Camera(CommonNames, Configuration, GetFrameFromProducent):
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    WIDTH, HEIGHT, FPS = JsonHandling.loadNativeCameraResolutionJson()

    def __init__(self, windowSize):
        GetFrameFromProducent.__init__(self)
        super().__init__()

        self.device = cv2.VideoCapture(0)

        self.windowSize = windowSize

        self.__testCameraCommunication()

        self.configurationSetUp(self.WIDTH, self.HEIGHT, self.FPS)

        self.__readValues()

    def __readValues(self) -> None:
        [communicationPoint.setValue(self.device) for communicationPoint in self.communicationPoints]

    def __testCameraCommunication(self) -> None:
        try:
            ret, _ = self.device.read()
            if not ret:
                raise NoCammeraConected
        except NoCammeraConected:

            self.device = CameraSimulator()

    def setNewValueForCommunicationPoint(self, communicationPoint) -> None:
        self.device.set(communicationPoint.address, communicationPoint.value)
        self.parametersDictionary[communicationPoint.name]["value"] = communicationPoint.value
        self.saveConfig()
