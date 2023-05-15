import cv2
from numpy import ndarray, average

from BaseClass.Logger.Logger import Loger


class GetFrame(Loger):

    def getFrame(self) -> ndarray:  # todo Optimalisation
        # [self.loger(cc.name, cc.value) for cc in self.communicationPoints]
        ret, newFrame = self.device.read()
        return self.__white_balance(self.__resize(newFrame, self.windowSize.width(), self.windowSize.height()))

    def getGrayFrame(self):
        return cv2.cvtColor(self.getFrame(), cv2.COLOR_BGR2GRAY)

    @staticmethod
    def __resize(newFrame, width, height):
        return cv2.resize(newFrame, (width, height), interpolation=cv2.INTER_CUBIC)

    @staticmethod
    def __rotate90deg(newFrame: ndarray) -> ndarray:
        return GetFrame.__rotate(newFrame, 90)

    @staticmethod
    def __rotate(newFrame: ndarray, angle: int) -> ndarray:
        h, w = newFrame.shape[:2]
        cX, cY = (w // 2, h // 2)

        m = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
        newFrame = cv2.warpAffine(newFrame, m, (w, h))

        return newFrame

    def __white_balance(self, img):
        result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        avg_a = average(result[:, :, 1])
        avg_b = average(result[:, :, 2])
        result[:, :, 1] = result[:, :, 1] - ((avg_a - self.whiteBalance.value) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - self.whiteBalance.value) * (result[:, :, 0] / 255.0) * 1.1)
        result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return result
