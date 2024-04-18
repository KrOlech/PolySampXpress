import numpy
from matplotlib import pyplot as plt

from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness
from Python.BaseClass.Logger.Logger import Loger


class AutoFokusNot(Loger):

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

    def run(self):
        self.focusPoints = []
        self.focusPointsLocation = []

        self.manipulatorInterface.home()
        self.manipulatorInterface.waitForTarget()

        for i in range(-10000, 10000, 100):
            self.focusPointsLocation.append(i)
            self.manipulatorInterface.x = i
            self.manipulatorInterface.gotoNotAsync()
            self.manipulatorInterface.waitForTarget()
            self.focusPoints.append(image_sharpness(self.camera.getFrame()))

        self.loger(self.focusPoints)
        self.loger(self.focusPointsLocation)

        i = self.focusPointsLocation[numpy.array(self.focusPoints).argmax()]
        self.loger("end point ", i)
        self.manipulatorInterface.x = i
        self.manipulatorInterface.gotoNotAsync()
        self.manipulatorInterface.waitForTarget()

        plt.scatter(self.focusPointsLocation, self.focusPoints)

        self.focusPoints1 = []
        self.focusPointsLocation1 = []

        self.manipulatorInterface.home()
        self.manipulatorInterface.waitForTarget()

        self.manipulatorInterface.x = i - 800
        self.manipulatorInterface.gotoNotAsync()
        self.manipulatorInterface.waitForTarget()

        for j in range(i - 400, i + 400, 1):
            self.focusPointsLocation1.append(j)
            self.manipulatorInterface.x = j
            self.manipulatorInterface.gotoNotAsync()
            self.manipulatorInterface.waitForTarget()
            self.focusPoints1.append(image_sharpness(self.camera.getFrame()))

        i = self.focusPointsLocation1[numpy.array(self.focusPoints1).argmax()]
        self.manipulatorInterface.x = i
        self.manipulatorInterface.gotoNotAsync()
        self.manipulatorInterface.waitForTarget()
        self.camera.getFrame()

        self.loger("end point ", i)

        self.loger(self.focusPoints1)
        self.loger(self.focusPointsLocation1)

        plt.scatter(self.focusPointsLocation1, self.focusPoints1, marker='+')
        plt.show()
