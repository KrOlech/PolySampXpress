from abc import abstractmethod, ABCMeta

import cv2
from numpy import ndarray, zeros_like, uint8

from src.BaseClass.Abstract import abstractmetod
from src.BaseClass.Logger.Logger import Loger


class AbstractGetFrame(Loger):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getFrame(self) -> ndarray:
        abstractmetod(self)
        return zeros_like([640, 480, 3], dtype=uint8)

    def getGrayFrame(self):
        return cv2.cvtColor(self.getFrame(), cv2.COLOR_BGR2GRAY)
