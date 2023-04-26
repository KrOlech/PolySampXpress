import cv2

from src.Camera.Calibration.Calibration import Calibrate
from src.Camera.ComonNames.ComonNames import CommonNames
from src.Camera.Configuration.Configuration import Configuration
from src.Camera.GetFrame.GetFrame import GetFrame
from src.utilitis.JsonRead.JsonRead import loadNativeCameraResolutionJson
from src.utilitis.Logger.Logger import Loger


class Camera(CommonNames, GetFrame, Configuration, Calibrate, Loger):
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    WIDTH, HEIGHT, FPS = loadNativeCameraResolutionJson()

    def __init__(self):
        super().__init__()

        self.device = cv2.VideoCapture(0)

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
                raise TypeError  # TODO Proper Custom error
        except TypeError:
            self.logError(
                "Error During camera initialisation check it connection or if any other software is using it.")

    def setNewValueForCommunicationPoint(self, communicationPoint):
        self.device.set(communicationPoint.address, communicationPoint.value)
        self.parametersDictionary[communicationPoint.name]["value"] = communicationPoint.value
        self.saveConfig()
