import cv2

from Python.Interface.ComunicationPoint.Abstract.AbstractComunicationPort import AbstractCommunicationPoint


class CommonCommunicationPoint(AbstractCommunicationPoint):

    def setValue(self, device: cv2.VideoCapture) -> None:
        pass
