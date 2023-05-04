import cv2

from src.Camera.Symulator.CameraSymulator import CameraSymulator
from src.Camera.Calibration.Main import MainCalibrate
from src.Camera.ComonNames.ComonNames import CommonNames
from src.Camera.Configuration.Configuration import Configuration
from src.Camera.GetFrame.GetFrame import GetFrame
from src.utilitis.JsonRead.JsonRead import JsonHandling
from src.utilitis.Logger.Logger import Loger
from src.utilitis.CustomExceptions.Exceptions import NoCammeraConected


class Camera(CommonNames, GetFrame, Configuration, MainCalibrate, Loger):
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    WIDTH, HEIGHT, FPS = JsonHandling.loadNativeCameraResolutionJson()

    def __init__(self, windowSize):
        super().__init__()

        self.device = cv2.VideoCapture(0)

        self.windowSize = windowSize

        self.testCameraCommunication()

        self.set(self.WIDTH, self.HEIGHT, self.FPS)

        self.device.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        self.device.set(cv2.CAP_PROP_EXPOSURE, -2)

        self.readValues()

    def readValues(self) -> None:
        [communicationPoint.setValue(self.device) for communicationPoint in self.COMMUNICATIONPOINTS]

    def testCameraCommunication(self) -> None:
        try:
            ret, _ = self.device.read()
            if not ret:
                raise NoCammeraConected
        except NoCammeraConected:

            self.device = CameraSymulator()

    def setNewValueForCommunicationPoint(self, communicationPoint):
        self.device.set(communicationPoint.address, communicationPoint.value)
        self.parametersDictionary[communicationPoint.name]["value"] = communicationPoint.value
        self.saveConfig()
