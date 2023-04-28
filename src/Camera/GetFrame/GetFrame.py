import cv2
from numpy import ndarray, average


class GetFrame:

    def getFrame(self) -> ndarray: #todo Optimalisation
        ret, newFrame = self.device.read()
        return self.white_balance(self.resize(newFrame, 1920, 1080)) #toDo read from system trey

    @staticmethod
    def resize(newFrame, width, height):
        return cv2.resize(newFrame, (width, height), interpolation=cv2.INTER_CUBIC)

    def rotate90deg(self, newFrame: ndarray) -> ndarray:
        return self._rotete(newFrame, 90)

    @staticmethod
    def _rotete(newFrame: ndarray, angle: int) -> ndarray:
        h, w = newFrame.shape[:2]
        cX, cY = (w // 2, h // 2)

        m = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
        newFrame = cv2.warpAffine(newFrame, m, (w, h))

        return newFrame

    def white_balance(self, img):
        result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        avg_a = average(result[:, :, 1])
        avg_b = average(result[:, :, 2])
        result[:, :, 1] = result[:, :, 1] - ((avg_a - self._whiteBalance.value) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - self._whiteBalance.value) * (result[:, :, 0] / 255.0) * 1.1)
        result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return result
