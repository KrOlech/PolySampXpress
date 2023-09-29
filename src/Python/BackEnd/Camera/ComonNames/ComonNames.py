from functools import cache

import cv2

from src.Python.Interface.ComunicationPoint.ComonComunicationPoint.CommonCommunicationPoint import \
    CommonCommunicationPoint as CCPoint
from src.Python.Interface.ComunicationPoint.OpenCvComunicationPort.OpenCVComunicationPort import \
    OpenCVCCommunicationPoint as OCCPoint

from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class CommonNames(JsonHandling):

    @property
    def settingsFileName(self):
        return "CameraSetings.json"

    @property
    @cache
    def height(self):
        return OCCPoint(cv2.CAP_PROP_FRAME_HEIGHT)

    @property
    @cache
    def width(self):
        return OCCPoint(cv2.CAP_PROP_FRAME_WIDTH)

    @property
    @cache
    def fps(self):
        return OCCPoint(cv2.CAP_PROP_FPS)

    def __init__(self):
        self.parametersDictionary = self.readFile(self.settingsFileName)

        BRIGHTNESS = "BRIGHTNESS"
        self.brightness = OCCPoint(BRIGHTNESS, self.parametersDictionary[BRIGHTNESS])

        SATURATION = "SATURATION"
        self.saturation = OCCPoint(SATURATION, self.parametersDictionary[SATURATION])

        HUE = "HUE"
        self.hue = OCCPoint(HUE, self.parametersDictionary[HUE])

        SHARPNESS = "SHARPNESS"
        self.sharpness = OCCPoint(SHARPNESS, self.parametersDictionary[SHARPNESS])

        GAMMA = "GAMMA"
        self.gamma = OCCPoint(GAMMA, self.parametersDictionary[GAMMA])

        EXPOSURE = "EXPOSURE"
        self.exposure = OCCPoint(EXPOSURE, self.parametersDictionary[EXPOSURE])

        GAIN = "GAIN"
        self.gain = OCCPoint(GAIN, self.parametersDictionary[GAIN])

        WHITEBALANCEBLUE = "WHITE BALANCE BLUE"
        self.whiteBalanceBlue = CCPoint(WHITEBALANCEBLUE, self.parametersDictionary[WHITEBALANCEBLUE])

        WHITEBALANCEGREEN = "WHITE BALANCE GREEN"
        self.whiteBalanceGreen = CCPoint(WHITEBALANCEGREEN, self.parametersDictionary[WHITEBALANCEGREEN])

        WHITEBALANCERED = "WHITE BALANCE RED"
        self.whiteBalanceRed = CCPoint(WHITEBALANCERED, self.parametersDictionary[WHITEBALANCERED])

        self.communicationPoints = [self.brightness, self.saturation, self.hue, self.sharpness, self.gamma,
                                    self.exposure, self.gain, self.whiteBalanceBlue, self.whiteBalanceGreen,
                                    self.whiteBalanceRed]

    def saveConfig(self):
        self.saveFile(self.settingsFileName, self.parametersDictionary)
