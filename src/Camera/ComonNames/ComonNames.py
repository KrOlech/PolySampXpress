from functools import cache

import cv2

from src.Camera.ComunicationPoint.ComonComunicationPoint.CommonCommunicationPoint import \
    CommonCommunicationPoint as OCCPoint
from src.Camera.ComunicationPoint.OpenCvComunicationPort.OpenCVComunicationPort import \
    OpenCVCCommunicationPoint as CCPoint

from src.utilitis.JsonRead.JsonRead import JsonHandling


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

        WHITEBALANCE = "WHITE BALANCE"
        self.whiteBalance = CCPoint(WHITEBALANCE, self.parametersDictionary[WHITEBALANCE])

        self.communicationPoints = [self.brightness, self.saturation, self.hue, self.sharpness, self.gamma,
                                    self.exposure, self.gain, self.whiteBalance]

    def saveConfig(self):
        self.saveFile(self.settingsFileName, self.parametersDictionary)
