import matplotlib.pyplot as plt
import numpy
from cv2 import cvtColor, COLOR_BGR2GRAY, IMREAD_GRAYSCALE, imwrite, imread

from Python.BackEnd.SzarpnesCalculation.CalculateAndSaveResults import CalculateAndSaveResults
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness, image_sharpness2, sobel, \
    fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness
from Python.BaseClass.Logger.Logger import Loger

from scipy.optimize import minimize


class AutoFokus02(Loger):
    funs = [image_sharpness, image_sharpness2, sobel, fft_based_sharpness, scharr_variance, edge_based_sharpness,
            lpc_based_sharpness]

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

        # self.metricCalculation = CalculateAndSaveResults(edge_based_sharpness)
        # self.metricCalculation = [CalculateAndSaveResults(fun) for fun in self.funs]
        self.metricCalculation = [CalculateAndSaveResults(self.funs[0])]

    def run(self):
        self.loger('Optimization started')
        self.manipulatorInterface.fokusGoTo(-10000)  # zerowanei fokusu

        self.manipulatorInterface.fokusGoTo(1000)  # osiongniecie potecialnego fokusu

        self.guess()
        # self.scan()

        self.loger('Optimization ended')

    def guess(self):
        self.fokusData = []
        self.fokusDataX = []

        rez = minimize(self.fokusFromValue, 2000, bounds=[(2000, 3000)], method='COBYLA', tol=0.005,
                       options={"rhobeg": 100}
                       )

        self.loger(f"calculated Fokus rez = {rez}")

        self.loger(f"calculated Fokus min = {rez.x[0]} low = {rez.x}")

        self.manipulatorInterface.fokusGoTo(rez.x[0])

        #plt.scatter(self.fokusDataX, self.fokusData)
        #plt.show()

    def scan(self):

        self.fokusData = [[] for _ in range(len(self.metricCalculation))]

        for i in range(50):
            self.manipulatorInterface.fokusUp(50)
            for it, fun in enumerate(self.metricCalculation):
                self.fokusData[it].append(self.calcFokus(fun))
            self.loger(f"calculated Fokus metric = {self.fokusData[-1]}")

        for fData in self.fokusData:
            # maxY = max(fData)
            # plt.plot([w / maxY for w in fData])
            plt.plot([1000 + i * 50 for i in range(50)], fData)
        plt.show()

    def calcFokus(self, fun):
        imwrite("temp.png", self.camera.getFrame())
        img = imread("temp.png", IMREAD_GRAYSCALE)
        r = fun(img)
        self.loger(f"Data {r}")
        return r

    def wraperOnTable(self, x):
        return -self.fokusData[int(x)]

    def fokusFromValue(self, i):
        self.manipulatorInterface.fokusGoTo(i[0])
        rez = -self.calcFokus(self.metricCalculation[0])
        self.fokusData.append(rez)
        self.fokusDataX.append(i[0])
        return rez
