from abc import abstractmethod

import cv2

from src.Python.BaseClass.Logger.Logger import Loger


class AbstractCommunicationPoint(Loger):

    def __init__(self, name, CommunicationPointDTO=None) -> None:
        if isinstance(CommunicationPointDTO, dict):
            self.address = CommunicationPointDTO["address"]
            self.min = CommunicationPointDTO["min"]
            self.max = CommunicationPointDTO["max"]
            self.value = CommunicationPointDTO["value"]
            self.name = name
        else:
            self.address = name
            self.min = 0
            self.max = 1
            self.value = 0

    @abstractmethod
    def setValue(self, device: cv2.VideoCapture) -> None:
        self.abstractmetod()
