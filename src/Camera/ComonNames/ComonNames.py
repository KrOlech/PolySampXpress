import cv2

from src.Camera.Utilitis.ComonComunicationPoint.CommonCommunicationPoint import CommonCommunicationPoint as CCPoint
from src.Camera.Utilitis.OpenCvComunicationPort.OpenCVComunicationPort import OpenCVCCommunicationPoint as OCCPoint
from src.utilitis.JsonRead.JsonRead import JsonHandling


class CommonNames(JsonHandling):
    # Strings:
    __BRIGHTNESS = "BRIGHTNESS"
    __SATURATION = "SATURATION"
    __HUE = "HUE"
    __SHARPNESS = "SHARPNESS"
    __GAMMA = "GAMMA"
    __EXPOSURE = "EXPOSURE"
    __GAIN = "GAIN"
    __whiteBalance = "WHITE BALANCE"

    settingsFileName = "CameraSetings.json"

    # Non Configurable Values
    _HEIGHT = OCCPoint(cv2.CAP_PROP_FRAME_HEIGHT)
    _WIDTH = OCCPoint(cv2.CAP_PROP_FRAME_WIDTH)
    _FPS = OCCPoint(cv2.CAP_PROP_FPS)

    def __init__(self):
        self.parametersDictionary = self.readFile(self.settingsFileName)

        self._BRIGHTNESS = OCCPoint(self.__BRIGHTNESS, self.parametersDictionary[self.__BRIGHTNESS])
        self._SATURATION = OCCPoint(self.__SATURATION, self.parametersDictionary[self.__SATURATION])
        self._HUE = OCCPoint(self.__HUE, self.parametersDictionary[self.__HUE])
        self._SHARPNESS = OCCPoint(self.__SHARPNESS, self.parametersDictionary[self.__SHARPNESS])

        self._GAMMA = OCCPoint(self.__GAMMA, self.parametersDictionary[self.__GAMMA])
        self._EXPOSURE = OCCPoint(self.__EXPOSURE, self.parametersDictionary[self.__EXPOSURE])
        self._GAIN = OCCPoint(self.__GAIN, self.parametersDictionary[self.__GAIN])
        self._whiteBalance = CCPoint(self.__whiteBalance, self.parametersDictionary[self.__whiteBalance])

        self.COMMUNICATIONPOINTS = [self._BRIGHTNESS, self._SATURATION, self._HUE, self._SHARPNESS, self._GAMMA,
                                    self._EXPOSURE, self._GAIN, self._whiteBalance]


    def saveConfig(self):
        self.saveFile(self.settingsFileName, self.parametersDictionary)
