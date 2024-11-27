import cv2

from Python.BaseClass.Logger.Logger import Loger


class AutoFokusOld(Loger):

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

    def run(self):

        treshold = self.__calcucateFokus()
        self.manipulatorInterface.x -= 1
        self.manipulatorInterface.gotoNotAsync()

        while True:
            focusMetric = self.__calcucateFokus()

            if focusMetric < treshold:
                self.manipulatorInterface.x -= 1
            if focusMetric > treshold:
                self.manipulatorInterface.x += 1
            self.manipulatorInterface.gotoNotAsync()

            newTreshold = self.__calcucateFokus()

            self.loger(treshold, newTreshold)

            if round(newTreshold - treshold, 2) == 0:
                break
            else:
                treshold = newTreshold

    def __calcucateFokus(self):
        image = self.camera.getFrame()
        return cv2.Laplacian(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()
