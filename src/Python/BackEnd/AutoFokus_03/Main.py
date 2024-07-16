from Python.BackEnd.SzarpnesCalculation.CalculateAndSaveResults import CalculateAndSaveResults
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import edge_based_sharpness
from cv2 import cvtColor, COLOR_BGR2GRAY, IMREAD_GRAYSCALE, imwrite, imread
from Python.BaseClass.Logger.Logger import Loger

from scipy.optimize import minimize
class AutoFokus03(Loger):
    fun = edge_based_sharpness

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

        self.metricCalculation = CalculateAndSaveResults(self.fun)

    def run(self):
        rez = minimize(self.handleFokus, 2000, bounds=[(2000, 3000)], method='COBYLA', tol=0.005,
                       options={"rhobeg": 100}
                       )

        self.loger(f"calculated Fokus rez = {rez}")

        self.loger(f"calculated Fokus min = {rez.x[0]} low = {rez.x}")

        self.manipulatorInterface.fokusGoTo(rez.x[0])

    def handleFokus(self, i):
        self.manipulatorInterface.fokusGoTo(i[0])
        rez = -self.calcFokus(self.metricCalculation)
        return rez

    def calcFokus(self, fun):
        imwrite("temp.png", self.camera.getFrame())
        img = imread("temp.png", IMREAD_GRAYSCALE)
        r = fun(img)
        self.loger(f"Data {r}")
        return r