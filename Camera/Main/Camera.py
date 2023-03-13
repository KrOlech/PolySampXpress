import cv2

from Camera.Calibration.Calibration import Calibrate
from Camera.ComonNames.ComonNames import CommonNames
from Camera.Configuration.Configuration import Configuration
from Camera.GetFrame.GetFrame import GetFrame
from utilitis.JsonRead.JsonRead import loadNativeCameraResolutionJson


class Camera(CommonNames, GetFrame, Configuration,Calibrate):
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    WIDTH, HEIGHT, FPS = loadNativeCameraResolutionJson()

    def __init__(self):

        self.device = cv2.VideoCapture(0)

        self.testCameraCommunication()

        self.set(self.WIDTH, self.HEIGHT, self.FPS)

        self.readValues()

    def readValues(self) -> None:
        [communicationPoint.setValue(self.device) for communicationPoint in self.COMMUNICATIONPOINTS]

    def testCameraCommunication(self) -> None:
        try:
            ret, _ = self.device.read()
            if not ret:
                raise TypeError  # TODO Proper Custom error
        except TypeError:
            print("Error During camera initialisation check it connection or if any other software is using it.")



