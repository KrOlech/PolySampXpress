import cv2

from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class CameraSimulator:

    def __init__(self):
        pass

    @staticmethod
    def read():
        #fileName = JsonHandling.getFileLocation("sym.png")
        fileName = JsonHandling.getFileLocation('crosv2.png')
        return True, cv2.imread(fileName)

    def set(self, *param):
        pass
