import cv2

from Camera.Utilitis.Abstract.AbstractComunicationPort import AbstractCommunicationPoint


class CommonCommunicationPoint(AbstractCommunicationPoint):

    def setValue(self, device: cv2.VideoCapture) -> None:
        self.value = 90
