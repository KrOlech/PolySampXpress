import cv2

from src.Python.Interface.ComunicationPoint.Abstract.AbstractComunicationPort import AbstractCommunicationPoint


class OpenCVCCommunicationPoint(AbstractCommunicationPoint):

    def setValue(self, device: cv2.VideoCapture) -> None:
        device.set(self.address, self.value)
