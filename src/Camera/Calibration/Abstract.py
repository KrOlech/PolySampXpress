from abc import ABCMeta
import cv2 as cv
import numpy as np
from numpy import mean

from src.Camera.Calibration.Propertis import CalibrateProperty
from src.utilitis.JsonRead.JsonRead import JsonHandling


class AbstractCalibrate(JsonHandling, CalibrateProperty):
    __metaclass__ = ABCMeta

    manipulatorInterferes = None
    template0 = None
    calibrationDialog = None

    def getGrayFrame(self):
        return cv.cvtColor(self.getFrame(), cv.COLOR_BGR2GRAY)

    def extractTemplate(self, frame):
        template = frame[self.templateLocationY:self.templateLocationY + self.templateSize,
                   self.templateLocationX:self.templateLocationX + self.templateSize]
        w, h = template.shape[::-1]
        return template, w, h

    def __lowestThreshold(self, results):

        for threshold in np.arange(1, 0.7, -0.01):
            resultsForCurrentThreshold = np.where(results >= threshold)
            if len(resultsForCurrentThreshold[0]):
                self.loger(f"Found maches for template with threshold {threshold}")
                break
        else:
            self.logError("Can't Found template for threshold ")
            return None

        return resultsForCurrentThreshold

    def matchTemplate(self, template):
        return self.__lowestThreshold(cv.matchTemplate(self.getGrayFrame(), template, cv.TM_CCOEFF_NORMED))

    def saveFrameWithTemplate(self, fileName, frame, Location):
        cv.rectangle(frame, Location, (Location[0] + self.templateSize, Location[1] + self.templateSize), (0, 0, 255),
                     2)
        cv.imwrite(fileName + '.png', frame)

    def findTemplates(self, loc, fileName):

        delty = [[], []]

        frame_ = self.getFrame()

        for pt in zip(*loc[::-1]):
            delty[0].append(self.templateLocationX - pt[0])
            delty[1].append(self.templateLocationY - pt[1])
            cv.rectangle(frame_, pt, (pt[0] + self.templateSize, pt[1] + self.templateSize), (0, 0, 255), 2)

        cv.imwrite(str(fileName) + 'e.png', frame_)

        delty = (mean(delty[0]), mean(delty[1]))

        return delty

    def saveCalibrationResults(self, delty, index):

        data = self.readFile(self.configFile)
        try:
            data["0"]["offsets"][self.indexLegend[index]] = int(delty[index])
        except ValueError as e:
            self.logError(e)
        else:
            self.loger(int(delty[index]))

            self.saveFile(self.configFile, data)
