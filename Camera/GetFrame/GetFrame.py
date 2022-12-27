import cv2
from numpy import ndarray

class GetFrame:

    def getFrame(self) -> ndarray:
        ret, newFrame = self.device.read()
        return self.resize(newFrame, 2560, 1440)

    def resize(self, newFrame, width, height):
        return cv2.resize(newFrame, (width, height), interpolation=cv2.INTER_CUBIC)

    def rotate90deg(self, newFrame: ndarray) ->ndarray:
        return self._rotete(newFrame, 90)

    def _rotete(self, newFrame: ndarray, angle: int) -> ndarray:
        h, w = newFrame.shape[:2]
        cX, cY = (w // 2, h // 2)

        m = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
        newFrame = cv2.warpAffine(newFrame, m, (w, h))

        return newFrame