import cv2

from src.utilitis.JsonRead.JsonRead import JsonHandling


class CameraSimulator:

    def __init__(self):
        pass

    @staticmethod
    def read():
        fileName = JsonHandling.getFileLocation("sym.png")
        return True, cv2.imread(fileName)

    def set(self, *param):
        pass
