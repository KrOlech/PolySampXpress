from abc import ABCMeta
import cv2 as cv
from numpy import mean

from src.Python.BackEnd.Calibration.Abstract.TemplateMatching import TemplateMatching
from src.Python.BackEnd.Calibration.Propertis.Propertis import CalibrateProperty
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class AbstractCalibrate(JsonHandling, CalibrateProperty, TemplateMatching):
    __metaclass__ = ABCMeta

    manipulatorInterferes = None
    template0 = None
    calibrationDialog = None

    def __init__(self, camera):
        self.camera = camera

    def getGrayFrame(self):
        return cv.cvtColor(self.camera.getFrame(), cv.COLOR_BGR2GRAY)

    def extractTemplate(self, frame):
        template = frame[self.templateLocationY:self.templateLocationY + self.templateSize,
                         self.templateLocationX:self.templateLocationX + self.templateSize]
        w, h = template.shape[::-1]
        return template, w, h

    def saveFrameWithTemplate(self, fileName, frame, Location):
        cv.rectangle(frame, Location, (Location[0] + self.templateSize, Location[1] + self.templateSize), (0, 0, 255),
                     2)
        cv.imwrite(fileName + '.png', frame)

    def findTemplates(self, loc, fileName):

        delta = [[], []]

        frame_ = self.camera.getFrame()

        for pt in zip(*loc[::-1]):
            delta[0].append(self.templateLocationX - pt[0])
            delta[1].append(self.templateLocationY - pt[1])
            cv.rectangle(frame_, pt, (pt[0] + self.templateSize, pt[1] + self.templateSize), (0, 0, 255), 2)

        cv.imwrite(str(fileName) + 'e.png', frame_)

        delta = (mean(delta[0]), mean(delta[1]))

        return delta

    def saveCalibrationResults(self, delta, index):

        data = self.readFile(self.configFile)
        try:
            data["0"]["offsets"][self.indexLegend[index]] = int(delta[index]/2)
        except ValueError as e:
            self.logError(e)
        else:
            self.loger(int(delta[index]))

            self.saveFile(self.configFile, data)
