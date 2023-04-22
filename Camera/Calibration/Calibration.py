import cv2 as cv
import numpy as np
from numpy import mean

from Camera.Calibration.Propertis import CalibrateProperty
from utilitis.JsonRead.JsonRead import JsonHandling


class Calibrate(JsonHandling, CalibrateProperty):

    def getGrayFrame(self):
        return cv.cvtColor(self.getFrame(), cv.COLOR_BGR2GRAY)

    def extractTemplate(self, frame):
        template = frame[self.templateLocationY:self.templateLocationY + self.templateSize,
                   self.templateLocationX:self.templateLocationX + self.templateSize]
        w, h = template.shape[::-1]
        return template, w, h

    def matchTemplate(self, template):
        return self.__lowestThreshold(cv.matchTemplate(self.getGrayFrame(), template, cv.TM_CCOEFF_NORMED))

    def __lowestThreshold(self, results):

        for threshold in np.arange(1, 0.7, -0.1):
            resultsForCurrentThreshold = np.where(results >= threshold)
            if len(resultsForCurrentThreshold[0]):
                break
        else:
            self.logError("Can't Found template for threshold ")
            return []

        return resultsForCurrentThreshold

    def calibrateX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveRight, 0)

    def calibrateY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveUp, 1)

    def calibrateNegativeX(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveLeft, 0)

    def calibrateNegativeY(self, manipulatorInterferes):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveDown, 1)

    def calibrateXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveXY, None, template0)

    def calibrateNegativeXY(self, manipulatorInterferes, template0):
        self.__calibrate(manipulatorInterferes, manipulatorInterferes.moveNegativeXY, None, template0)

    def __calibrate(self, manipulatorInterferes, movementFun, index, template=None):
        template, w, h = self.extractTemplate(self.getGrayFrame()) if template is None else template

        freame_ = self.getFrame()
        cv.rectangle(freame_, (self.templateLocationY, self.templateLocationX),
                     (self.templateLocationY + w, self.templateLocationX + h), (0, 0, 255), 2)
        cv.imwrite(str(index) + 's.png', freame_)

        movementFun()
        manipulatorInterferes.waitForTarget()

        for _ in range(100):
            self.getFrame()

        loc = self.matchTemplate(template)

        delty = [[], []]

        self.loger(loc)
        freame_ = self.getFrame()

        for pt in zip(*loc[::-1]):
            delty[0].append(1496 - pt[0])
            delty[1].append(984 - pt[1])
            cv.rectangle(freame_, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imwrite(str(index) + 'e.png', freame_)

        delty = (mean(delty[0]), mean(delty[1]))

        self.loger(delty)

        if index is not None:
            if delty[not index] > 5:
                self.logWarning("To math distortion in other axis")
                # toDo proper error

            data = self.readFile(self.configFile)

            data["0"]["offsets"][self.indexLegend[index]] = int(delty[index])

            self.loger(int(delty[index]))

            self.saveFile(self.configFile, data)

    def calibrate(self, manipulatorInterferes):

        template0 = self.extractTemplate(self.getGrayFrame())

        self.calibrateX(manipulatorInterferes)

        self.calibrateY(manipulatorInterferes)

        self.calibrateNegativeXY(manipulatorInterferes, template0)

        self.calibrateNegativeX(manipulatorInterferes)

        self.calibrateNegativeY(manipulatorInterferes)

        self.calibrateXY(manipulatorInterferes, template0)
