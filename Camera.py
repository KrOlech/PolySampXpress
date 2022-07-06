# import the opencv library
import cv2


class _OpenCVComunicationPoint:

    def __int__(self, adres, min=0, max=1):
        self.adres = adres
        self.min = min
        self.max = max
        self.value = 0

    def setValue(self, device):
        self.value = device.getValue(self.adres)


class Camera:
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    _HIGHT = _OpenCVComunicationPoint(cv2.CAP_PROP_FRAME_HEIGHT)
    _WIDTH = _OpenCVComunicationPoint(cv2.CAP_PROP_FRAME_WIDTH)
    _FPS = _OpenCVComunicationPoint(cv2.CAP_PROP_FPS)

    _BRIGHTNESS = _OpenCVComunicationPoint(cv2.CAP_PROP_BRIGHTNESS)
    _SATURATION = _OpenCVComunicationPoint(cv2.CAP_PROP_SATURATION)
    _HUE = _OpenCVComunicationPoint(cv2.CAP_PROP_HUE)
    _SHARPNESS = _OpenCVComunicationPoint(cv2.CAP_PROP_SHARPNESS)
    _GAMMA = _OpenCVComunicationPoint(cv2.CAP_PROP_GAMMA)
    _EXPOSURE = _OpenCVComunicationPoint(cv2.CAP_PROP_EXPOSURE)  # dziala dla mniejszych wartosci niz -5 wlocznie

    # _CONTRAST = cv2.CAP_PROP_CONTRAST #nope mozliwe ze sie da ale nier aguje
    # _GAIN = cv2.CAP_PROP_GAIN#na wycziucie martywy
    # _TEMPERATURE = cv2.CAP_PROP_TEMPERATURE #nope mozliwe ze sie da ale nier aguje
    # _WHITE_BALANCE_RED_V = cv2.CAP_PROP_WHITE_BALANCE_RED_V
    # _ZOOM = cv2.CAP_PROP_ZOOM
    # _FOCUS = cv2.CAP_PROP_FOCUS
    # _AUTOFOCUS = cv2.CAP_PROP_AUTOFOCUS
    COMUNICATIONPOINTS = [_HIGHT, _WIDTH, _FPS, _BRIGHTNESS, _SATURATION, _HUE, _SHARPNESS, _GAMMA, _EXPOSURE]

    def __init__(self):

        self.device = cv2.VideoCapture(0)

        try:
            ret, frame = self.device.read()
            if not ret:
                raise TypeError
        except TypeError:
            print(
                "Blond inicializacji Kamery zobacz cy jest poprawnie połonczona i nie uzywana przez inne urzadzenia")

        self.set(2160, 3840, 60)

        self.setBritnes(100)

        self.readValues()

    def readValues(self):
        [communicationPoint.setValue(self.device) for communicationPoint in self.COMUNICATIONPOINTS]

    def setBritnes(self, value=200):
        self._setValue(self._BRIGHTNESS.adres, value)

    def set(self, width=640, height=480, fps=25):
        self.setWidth(width)
        self.setHight(height)
        self.setFps(fps)

    def setWidth(self, width):
        self._setValue(self._WIDTH.adres, width)

    def setHight(self, hight):
        self._setValue(self._HIGHT.adres, hight)

    def setFps(self, fps):
        self._setValue(self._FPS.adres, fps)

    def _setValue(self, propertyID, value):
        self.device.set(propertyID, value)

    def getFrame(self):
        ret, frame = self.device.read()

        h, w = frame.shape[:2]
        cX, cY = (w // 2, h // 2)

        m = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
        frame = cv2.warpAffine(frame, m, (w, h))

        return frame

    def rotete(self):
        pass


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
