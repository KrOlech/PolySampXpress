from abc import ABCMeta
from numpy import where, arange
import cv2

from Python.BaseClass.Logger.Logger import Loger


class TemplateMatching(Loger):
    __metaclass__ = ABCMeta

    def __lowestThreshold(self, results):

        for threshold in arange(1, 0.7, -0.01):
            resultsForCurrentThreshold = where(results >= threshold)
            if len(resultsForCurrentThreshold[0]):
                self.loger(f"Found matches for template with threshold {threshold}")
                break
        else:
            self.logError("Can't Found template for threshold ")
            return None

        return resultsForCurrentThreshold

    def matchTemplate(self, template, frame=None):
        if frame is None:
            frame = self.getGrayFrame()
        return self.__lowestThreshold(cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED))
