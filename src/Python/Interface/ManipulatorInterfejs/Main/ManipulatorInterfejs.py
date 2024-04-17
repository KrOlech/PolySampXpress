import cv2
from PyQt5.QtCore import Qt
from cv2 import cvtColor, COLOR_BGR2GRAY, imwrite

from Python.BackEnd.SzarpnesCalculation.Main import SzarpnesCalculation
from Python.Interface.ManipulatorInterfejs.Abstract.AbstractManipulatroInterfejs import \
    AbstractManipulatorInterferes
from Python.Interface.ManipulatorInterfejs.Selection.Select import SelectManipulator

import matplotlib.pyplot as plt
import numpy
import scipy.optimize as optimize


class ManipulatorInterfere(AbstractManipulatorInterferes, SelectManipulator):

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, windowSize, myStatusBar, *args, **kwargs)

        # keyboard = [Qt.Key_W, Qt.Key_A, Qt.Key_D, Qt.Key_S]
        keyboard2 = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        # [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]
        [a.setShortcut(k) for a, k in zip(self.actions, keyboard2)]

        [a.setShortcutContext(Qt.WindowShortcut) for a in self.actions]

        [self.master.addAction(a) for a in self.actions]

        # self.autoFokus()

    def __calcucateFokus(self):
        image = self.master.camera.getFrame()
        return cv2.Laplacian(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()

    def autoFokus(self):
        SzarpnesCalculation(self, self.master.camera).show()

    def autoFokusOld(self):

        treshold = self.__calcucateFokus()
        self._focusManipulator.x -= 1
        self._focusManipulator.gotoNotAsync()

        while True:
            focusMetric = self.__calcucateFokus()

            if focusMetric < treshold:
                self._focusManipulator.x -= 1
            if focusMetric > treshold:
                self._focusManipulator.x += 1
            self._focusManipulator.gotoNotAsync()

            newTreshold = self.__calcucateFokus()

            self.loger(treshold, newTreshold)

            if round(newTreshold - treshold, 2) == 0:
                break
            else:
                treshold = newTreshold

    def autoFokusFilmik(self):
        for i in range(-10000, 10000, 100):
            self._focusManipulator.x = i
            self._focusManipulator.gotoNotAsync()
            self._focusManipulator.waitForTarget()
            imwrite(f"1_{i}_{self.image_sharpness(self.master.camera.getFrame())}.png", self.master.camera.getFrame())

    def fokusUp(self):
        self._focusManipulator.x += 100
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    def fokus0(self):
        self._focusManipulator.x = -10000
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    def autoFokusNot(self):
        self.focusPoints = []
        self.focusPointsLocation = []

        self._focusManipulator.home()
        self._focusManipulator.waitForTarget()

        for i in range(-10000, 10000, 100):
            self.focusPointsLocation.append(i)
            self._focusManipulator.x = i
            self._focusManipulator.gotoNotAsync()
            self._focusManipulator.waitForTarget()
            self.focusPoints.append(self.image_sharpness(self.master.camera.getFrame()))

        self.loger(self.focusPoints)
        self.loger(self.focusPointsLocation)

        i = self.focusPointsLocation[numpy.array(self.focusPoints).argmax()]
        self.loger("end point ", i)
        self._focusManipulator.x = i
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

        plt.scatter(self.focusPointsLocation, self.focusPoints)

        self.focusPoints1 = []
        self.focusPointsLocation1 = []

        self._focusManipulator.home()
        self._focusManipulator.waitForTarget()

        self._focusManipulator.x = i - 800
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

        for j in range(i - 400, i + 400, 1):
            self.focusPointsLocation1.append(j)
            self._focusManipulator.x = j
            self._focusManipulator.gotoNotAsync()
            self._focusManipulator.waitForTarget()
            self.focusPoints1.append(self.image_sharpness(self.master.camera.getFrame()))

        i = self.focusPointsLocation1[numpy.array(self.focusPoints1).argmax()]
        self._focusManipulator.x = i
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()
        self.master.camera.getFrame()

        self.loger("end point ", i)

        self.loger(self.focusPoints1)
        self.loger(self.focusPointsLocation1)

        plt.scatter(self.focusPointsLocation1, self.focusPoints1, marker='+')
        plt.show()

    def autoFokusWIP(self):
        self.loger('Optimization started')
        self.loger("Optimization function: ", self.image_sharpness(self.master.camera.getFrame()))
        for stepFokus in [100, 50, 10, 5, 1, 0.5, 0.1]:
            self.__stepFokus = stepFokus
            self.__autoFokus()

        self.loger('Optimization ended')

    def __autoFokus(self):

        tolerance = 0.01
        max_iteration = 15

        fun = lambda x: self.opt_function(x)
        res = optimize.minimize(fun, x0=[1], bounds=[(-5, 5)], method='COBYLA', tol=tolerance,
                                options={'maxiter': max_iteration})
        self.loger(res["message"])
        self.loger(res)

    @staticmethod
    def image_sharpness(img):
        img = cvtColor(img, COLOR_BGR2GRAY)
        img = numpy.asarray(img, dtype=numpy.float64)
        m = numpy.mean(img)
        img_s = numpy.add(-m, img)
        img_sq = numpy.multiply(img_s, img_s)
        r = numpy.sum(img_sq)
        return r

    def opt_function(self, x):
        img = self.master.camera.getFrame()
        self.camera_simulator(x)
        return -self.image_sharpness(img)

    def camera_simulator(self, x, focus_point=-3):
        self.loger("Param: ", x)
        if x < focus_point:
            self._focusManipulator.x -= self.__stepFokus
        if x > focus_point:
            self._focusManipulator.x += self.__stepFokus
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

        return numpy.array(self.master.camera.getFrame())
