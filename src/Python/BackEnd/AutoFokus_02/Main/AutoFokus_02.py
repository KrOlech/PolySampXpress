import matplotlib.pyplot as plt
from numpy import sum, mean, array
from cv2 import cvtColor, COLOR_BGR2GRAY, IMREAD_GRAYSCALE, imwrite, imread

from Python.BackEnd.SzarpnesCalculation.CalculateAndSaveResults import CalculateAndSaveResults
from Python.BaseClass.Logger.Logger import Loger

from scipy.optimize import minimize, curve_fit

from Python.Utilitis.SimpleStartEndWrapper import simpleStartEndWrapper


class AutoFokus02(Loger):
    window = None
    fokusQuality = None

    def __init__(self, manipulatorInterface, camera, fun):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

        self.fun = fun

        self.metricCalculator = CalculateAndSaveResults(fun)

    @simpleStartEndWrapper(text="Optimization")
    def run(self):
        self.manipulatorInterface.fokusGoTo(1000)  # ToDo potecial fokus from file not hardCoded

        self.guess()

        while self.fokusQuality:
            self.manipulatorInterface.fokusUp()
            self.guess()

    def guess(self, plot=True):

        if plot:
            plt.close()
            plt.cla()
            plt.clf()

        self.manipulatorInterface.fokusUp(50)

        self.fokusData = []
        self.fokusDataX = []

        rez = minimize(self.fokusFromValue, 2000, bounds=[(2000, 3000)], method='COBYLA', tol=0.005,
                       options={"rhobeg": 100}
                       )

        self.loger(f"calculated Fokus rez = {rez}")
        self.loger(f"calculated Fokus min = {rez.x[0]} low = {rez.x}")

        self.manipulatorInterface.fokusGoTo(rez.x[0])

        maxY = max(self.fokusData)
        self.normalizedRoad = array([w / maxY for w in self.fokusData])

        self.calculateFocusGoodness()

        if plot:
            plt.scatter(self.fokusDataX, self.normalizedRoad, marker='.',
                        label=self.metricCalculator.funName)

    def calcFokus(self, fun):
        imwrite("temp.png", self.camera.getFrame())
        img = imread("temp.png", IMREAD_GRAYSCALE)
        r = fun(img)
        # r = fun(img[img.shape[0] // 2 - 100:img.shape[0] // 2 + 100, img.shape[1] // 2 - 100:img.shape[1] // 2 + 100])
        self.loger(f"Data {r}")
        return r

    def wraperOnTable(self, x):
        return -self.fokusData[int(x)]

    def fokusFromValue(self, i):
        self.manipulatorInterface.fokusGoTo(i[0])
        rez = -self.calcFokus(self.metricCalculator)
        self.fokusData.append(-rez)
        self.fokusDataX.append(i[0])
        return rez

    def calculateFocusGoodness(self):

        line = lambda x, a, b: a * x + b
        parabolic = lambda x, a, b, c: a * x * x + b * x + c

        linePopt, _ = curve_fit(line, self.fokusDataX, self.normalizedRoad)

        poptParabolic, _ = curve_fit(parabolic, self.fokusDataX, self.normalizedRoad)

        # Predict y values for both models
        y_predLine = array([line(x, *linePopt) for x in self.fokusDataX])
        y_predParabolic = array([parabolic(x, *poptParabolic) for x in self.fokusDataX])

        # Calculate RSS
        rssLine = sum((self.normalizedRoad - y_predLine) ** 2)
        rss1 = sum((self.normalizedRoad - y_predParabolic) ** 2)

        # Calculate R-squared
        r2_line = 1 - (rssLine / sum((self.normalizedRoad - mean(self.normalizedRoad)) ** 2))
        r2_Parabolic = 1 - (rss1 / sum((self.normalizedRoad - mean(self.normalizedRoad)) ** 2))

        self.loger(f"Line {r2_line}")
        self.loger(f"Parabola {r2_Parabolic}")

        self.fokusQuality = r2_line > r2_Parabolic
