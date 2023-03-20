import cv2

from Camera.Utilitis.ComonComunicationPoint.CommonCommunicationPoint import CommonCommunicationPoint as CCPoint
from Camera.Utilitis.OpenCvComunicationPort.OpenCVComunicationPort import OpenCVCCommunicationPoint as OCCPoint


class CommonNames:
    # Strings:
    __BRIGHTNESS = "BRIGHTNESS"
    __SATURATION = "SATURATION"
    __HUE = "HUE"
    __SHARPNESS = "SHARPNESS"
    __GAMMA = "GAMMA"
    __EXPOSURE = "EXPOSURE"
    __GAIN = "GAIN"
    __whiteBalance = "WHITE BALANCE"

    # Non Configurable Values
    _HEIGHT = OCCPoint(cv2.CAP_PROP_FRAME_HEIGHT)
    _WIDTH = OCCPoint(cv2.CAP_PROP_FRAME_WIDTH)
    _FPS = OCCPoint(cv2.CAP_PROP_FPS)

    # Configurable Values
    _BRIGHTNESS = OCCPoint(cv2.CAP_PROP_BRIGHTNESS, __BRIGHTNESS, 0, 4000)
    _SATURATION = OCCPoint(cv2.CAP_PROP_SATURATION, __SATURATION, 0, 200)
    _HUE = OCCPoint(cv2.CAP_PROP_HUE, __HUE, -112, 175)
    _SHARPNESS = OCCPoint(cv2.CAP_PROP_SHARPNESS, __SHARPNESS, 1, 14)
    _GAMMA = OCCPoint(cv2.CAP_PROP_GAMMA, __GAMMA, 0, 500)
    _EXPOSURE = OCCPoint(cv2.CAP_PROP_EXPOSURE, __EXPOSURE, -15, 0)
    _GAIN = OCCPoint(cv2.CAP_PROP_GAIN, __GAIN, 0, 500)
    _whiteBalance = CCPoint(cv2.CAP_PROP_WB_TEMPERATURE, __whiteBalance, 0, 255)

    COMMUNICATIONPOINTS = [_BRIGHTNESS, _SATURATION, _HUE, _SHARPNESS, _GAMMA, _EXPOSURE, _GAIN, _whiteBalance]
