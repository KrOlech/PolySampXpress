from abc import ABCMeta

import cv2
from numpy import ndarray, average, mean, clip, uint8

from src.Camera.GetFrame.AbstractGetFream import AbstractGetFrame


class GetFrame(AbstractGetFrame):
    __metaclass__ = ABCMeta

    def getFrame(self) -> ndarray:  # todo Optimalisation
        # [self.loger(cc.name, cc.value) for cc in self.communicationPoints]
        ret, newFrame = self.device.read()
        return self.__white_balance(self.__resize(newFrame, self.windowSize.width(), self.windowSize.height()))

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

    @staticmethod
    def __white_balance(img):
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        # result = self.autoWhiteBalance(img)
        # result = self.__balanceColor(img, 128)  # Blue
        # result = self.__balanceColor(img, self.whiteBalanceBlue.value)  # Blue
        # result = self.__balanceColor(result, self.whiteBalanceGreen.value, [1, 0, 2])  # Green
        # result = self.__balanceColor(result, self.whiteBalanceRed.value, [2, 0, 1])  # Red
        # result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return img

    @staticmethod
    def __balanceColor(result, balance, color=None):
        if color is None:
            color = range(3)
        avg_a = average(result[:, :, color[1]])
        avg_b = average(result[:, :, color[2]])
        result[:, :, color[1]] = result[:, :, color[1]] - ((avg_a - balance) * (result[:, :, color[0]] / 255.0) * 1.1)
        result[:, :, color[2]] = result[:, :, color[2]] - ((avg_b - balance) * (result[:, :, color[0]] / 255.0) * 1.1)
        return result

    @staticmethod
    def autoWhiteBalance(image):
        l, a, b = cv2.split(image)

        lm = mean(l)
        am = mean(a)
        bm = mean(b)

        ls = lm / 128
        ass = am / 128
        bs = bm / 128

        l = clip(l * ls, 0, 255).astype(uint8)
        a = clip(a * ass, 0, 255).astype(uint8)
        b = clip(b * bs, 0, 255).astype(uint8)

        img = cv2.merge([l, a, b])

        return img
