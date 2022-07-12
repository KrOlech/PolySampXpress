import cv2
import numpy


class _OpenCVCCommunicationPoint:

    def __init__(self, address: int, name: str = '', minV: int = 0, maxV: int = 1) -> None:
        self.address = address
        self.min = minV
        self.max = maxV
        self.value = 0
        self.name = name

    def setValue(self, device: cv2.VideoCapture) -> None:
        self.value = device.get(self.address)


class Camera:
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    _HEIGHT = _OpenCVCCommunicationPoint(cv2.CAP_PROP_FRAME_HEIGHT)
    _WIDTH = _OpenCVCCommunicationPoint(cv2.CAP_PROP_FRAME_WIDTH)
    _FPS = _OpenCVCCommunicationPoint(cv2.CAP_PROP_FPS)

    _BRIGHTNESS = _OpenCVCCommunicationPoint(cv2.CAP_PROP_BRIGHTNESS, "BRIGHTNESS", 0, 4000)
    _SATURATION = _OpenCVCCommunicationPoint(cv2.CAP_PROP_SATURATION, "SATURATION", 0, 200)
    _HUE = _OpenCVCCommunicationPoint(cv2.CAP_PROP_HUE, "HUE", -112, 175)
    _SHARPNESS = _OpenCVCCommunicationPoint(cv2.CAP_PROP_SHARPNESS, "SHARPNESS", 1, 14)
    _GAMMA = _OpenCVCCommunicationPoint(cv2.CAP_PROP_GAMMA, "GAMMA", 0, 500)
    _EXPOSURE = _OpenCVCCommunicationPoint(cv2.CAP_PROP_EXPOSURE, "EXPOSURE", -15, 0)
    _GAIN = _OpenCVCCommunicationPoint(cv2.CAP_PROP_GAIN, "GAIN", 0, 500)

    COMMUNICATIONPOINTS = [_BRIGHTNESS, _SATURATION, _HUE, _SHARPNESS, _GAMMA, _EXPOSURE, _GAIN]

    HEIGHT = 2160
    WIDTH = 3840
    FPS = 60

    def __init__(self) -> None:

        self.device = cv2.VideoCapture(0)

        try:
            ret, _ = self.device.read()
            if not ret:
                raise TypeError
        except TypeError:
            print("Error During camera initialisation check it connection or if any other software is using it.")

        self.set(self.WIDTH, self.HEIGHT, self.FPS)

        self.setBritnes(100)

        self.readValues()

    def readValues(self) -> None:
        [communicationPoint.setValue(self.device) for communicationPoint in self.COMMUNICATIONPOINTS]

    def setBritnes(self, value: int = 200) -> None:
        self._setValue(self._BRIGHTNESS.address, value)

    def set(self, width: int = 640, height: int = 480, fps: int = 25):
        self.setWidth(width)
        self.setHight(height)
        self.setFps(fps)

    def setWidth(self, width: int) -> None:
        self._setValue(self._WIDTH.address, width)

    def setHight(self, height: int) -> None:
        self._setValue(self._HEIGHT.address, height)

    def setFps(self, fps: int) -> None:
        self._setValue(self._FPS.address, fps)

    def _setValue(self, propertyID: int, value: int) -> None:
        self.device.set(propertyID, value)

    def getFrame(self) -> numpy.ndarray:
        ret, newFrame = self.device.read()

        return cv2.resize(self.rotate90deg(newFrame),(1920,1080))

    def rotate90deg(self, newFrame: numpy.ndarray) -> numpy.ndarray:
        return self._rotete(newFrame, 90)

    def _rotete(self, newFrame: numpy.ndarray, angle: int) -> numpy.ndarray:
        h, w = newFrame.shape[:2]
        cX, cY = (w // 2, h // 2)

        m = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
        newFrame = cv2.warpAffine(newFrame, m, (w, h))

        return newFrame


if __name__ == '__main__':

    kam = Camera()

    while True:
        frame = kam.getFrame()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    kam.device.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
