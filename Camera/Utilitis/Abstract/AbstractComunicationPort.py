from abc import abstractmethod

import cv2

from utilitis.Abstract import abstractmetod


class AbstractCommunicationPoint:

    def __init__(self, address: int, name: str = '', minV: int = 0, maxV: int = 1) -> None:
        self.address = address
        self.min = minV
        self.max = maxV
        self.value = 0
        self.name = name

    @abstractmethod
    def setValue(self, device: cv2.VideoCapture) -> None:
        abstractmetod()
