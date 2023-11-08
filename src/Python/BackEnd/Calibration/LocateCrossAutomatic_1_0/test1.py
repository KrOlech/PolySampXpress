import numpy as np
from numpy import ones

from src.Python.BackEnd.Calibration.LocateCrossAutomatic_1_0.DataBase.CalibrationPointDataBase import CalibrationPointDataBase
from src.Python.BackEnd.Calibration.Abstract.TemplateMatching import TemplateMatching


class LocateCross(TemplateMatching):
    patternWithe = 1

    patternSize = 100

    entryInDataBase = True

    patternSizeMax = 500
    patternWitheMax = 20

    def __init__(self, zoom):

        dataBase = CalibrationPointDataBase()
        if str(zoom) in dataBase:
            self.patternSize = dataBase.getCrossSize(zoom)
            self.patternWithe = dataBase.getCrossWidthInPx(zoom)

        else:
            self.entryInDataBase = False
            for zoomM in range(int(zoom), 0, -1):
                if zoomM in dataBase:
                    self.patternSize = dataBase.getCrossSize(zoomM)
                    self.patternWithe = dataBase.getCrossWidthInPx(zoomM)
                    break

            for zoomM in range(int(zoom), max([int(z) for z in dataBase])):
                if zoomM in dataBase:
                    self.patternSizeMax = dataBase.getCrossSize(zoomM)
                    self.patternWitheMax = dataBase.getCrossWidthInPx(zoomM)
                    break

        self.createCrosTemplate()
        [self.widenThePattern() for _ in range(self.patternWithe)]

    def locateCross(self):
        fream = self.getGrayFrame()

    def createCrosTemplate(self):
        self.patern = ones((self.patternSize, self.patternSize)) * 255

        for i in range(self.patternSize):
            self.patern[self.patternSize // 2, i] = 0
            self.patern[i, self.patternSize // 2] = 0

    def widenThePattern(self):

        for i in range(self.patternSize):
            self.patern[self.patternSize // 2 + self.patternWithe, i] = 0
            self.patern[self.patternSize // 2 - self.patternWithe, i] = 0

            self.patern[i, self.patternSize // 2 + self.patternWithe] = 0
            self.patern[i, self.patternSize // 2 - self.patternWithe] = 0
        self.patternWithe += 1

    def findeTemplate(self, frame):

        for i in range(self.patternSize, self.patternSizeMax, 10):
            tempPatern = cv2.resize(self.patern.astype(np.uint8), (i, i), interpolation=cv2.INTER_CUBIC)

            mach = self.matchTemplate(tempPatern.astype(np.uint8), frame)

            if mach is not None:
                print(mach)
                print(i)
                print(self.patternWithe)
                if len(mach[0]) > 5:
                    for pt in zip(*mach[::-1]):
                        cv2.rectangle(frame, pt, (pt[0] + i, pt[1] + i), (0, 0, 255), 2)
                        cv2.line(frame, (pt[0], pt[1] + i // 2), (pt[0] + i, pt[1] + i // 2), (255, 0, 0),
                                 2 * self.patternWithe + 1)
                        cv2.line(frame, (pt[0] + i // 2, pt[1]), (pt[0] + i // 2, pt[1] + i), (255, 0, 0),
                                 2 * self.patternWithe + 1)
                    cv2.imwrite("test.png", frame)
                    break

        else:
            if self.patternWithe > self.patternWitheMax:
                self.logError("Pattern Matching Have Failed to Found Pattern Make sure that Pater in wie")
                return

            self.widenThePattern()
            self.findeTemplate(frame)


if __name__ == "__main__":
    import cv2
    from time import time

    test = LocateCross(1)

    image = cv2.imread("FullFreame.png")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # patern = cv2.cvtColor(test.patern, cv2.COLOR_BGR2GRAY)
    t0 = time()
    test.findeTemplate(image)
    print(time() - t0)
    # cv2.imwrite("test.png", test.patern)
