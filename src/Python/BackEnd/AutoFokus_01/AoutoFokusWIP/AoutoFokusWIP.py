import numpy
import scipy.optimize as optimize

from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness
from Python.BaseClass.Logger.Logger import Loger


class AutoFokusNot(Loger):

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

    def run(self):
        self.loger('Optimization started')
        self.loger("Optimization function: ", image_sharpness(self.camera.getFrame()))
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

    def opt_function(self, x):
        img = self.camera.getFrame()
        self.camera_simulator(x)
        return -image_sharpness(img)

    def camera_simulator(self, x, focus_point=-3):
        self.loger("Param: ", x)
        if x < focus_point:
            self.manipulatorInterface.x -= self.__stepFokus
        if x > focus_point:
            self.manipulatorInterface.x += self.__stepFokus
        self.manipulatorInterface.gotoNotAsync()
        self.manipulatorInterface.waitForTarget()

        return numpy.array(self.master.camera.getFrame())
