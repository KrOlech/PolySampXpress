import cv2 as cv
import numpy as np
from numpy import mean

from utilitis.JsonRead.JsonRead import JsonHandling


class Calibrate(JsonHandling):

    @property
    def indexLegend(self):
        return {0: "x", 1: "y"}

    @property
    def configFile(self):
        return "test.json"  # TODo przełoczyc na poprawny plik konfiguracyjy

    @property
    def threshold(self):
        return 0.95

    @property
    def templateLocationX(self):
        return 1496

    @property
    def templateLocationY(self):
        return 984

    @property
    def templateSize(self):
        return 80

    def getGrayFrame(self):
        frame = self.getFrame()
        return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    def extractTemplate(self, frameGray):
        template = frameGray[self.templateLocationY:self.templateLocationY + self.templateSize,
                   self.templateLocationX:self.templateLocationX + self.templateSize]
        w, h = template.shape[::-1]
        return template, w, h

    def matchTemplate(self, template):
        res = cv.matchTemplate(self.getGrayFrame(), template, cv.TM_CCOEFF_NORMED)

        return np.where(res >= self.threshold)

    def calibrateX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveLeft, 0)

    def calibrateY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveUp, 1)

    def __calibrate(self, manipulatorInterferes, movementFun, index):
        template, w, h = self.extractTemplate(self.getGrayFrame())

        movementFun()

        manipulatorInterferes.waitForTarget()  # TODo test if works ok implemented without manipulator

        # for _ in range(100): # todo mey be needed correct camera refresh
        #    self.getFrame()

        loc = self.matchTemplate(template)

        delty = [[], []]

        for pt in zip(*loc[::-1]):
            delty[0].append(1496 - pt[0])
            delty[1].append(984 - pt[1])

        delty = (mean(delty[0]), mean(delty[1]))

        if delty[not index] > 5:
            self.logWarning("To math distortion in other axis")
            # toDo proper error

        data = self.readFile(self.configFile)

        data["0"]["offsets"][self.indexLegend[index]] = int(delty[index])

        self.saveFile(self.configFile, data)

    def calibrate(self, manipulatorInterferes):
        self.calibrateX(manipulatorInterferes)

        self.calibrateY(manipulatorInterferes)
