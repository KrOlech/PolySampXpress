import os
import re
import cv2
import cv2 as cv
from PyQt5.QtWidgets import QFileDialog

from Python.BackEnd.SzarpnesCalculation.CalculateAndSaveResults import CalculateAndSaveResults

import matplotlib.pyplot as plt

from Python.BaseClass.Logger.Logger import Loger


class SzarpnesCalculation(Loger):
    steps = 100
    focusStep = 1
    focusCenter = 2035

    focusMax = focusCenter + (steps // 2 * focusStep)

    folderPath = None

    factors: list = []

    def __init__(self, manipulatorInterface, camera, master):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera
        self.master = master

    def addFactor(self, fun):
        self.factors.append(fun)

    def setParamiters(self, steps, focusStep, focusCenter):
        self.steps = steps
        self.focusStep = focusStep
        self.focusCenter = focusCenter

        self.focusMax = focusCenter + (steps // 2 * focusStep)

    def __runPreconditions(self):

        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folderPath = QFileDialog.getExistingDirectory(self.master, "Select Directory", "", options)

        folderPath = os.path.normpath(folderPath)
        folderPath += "\\"
        self.loger(folderPath)

        return folderPath

    def runAlgo(self):
        self.__run(True)

    def runNoAlgo(self):
        self.__run(False)

    def __run(self, algo=False):

        self.loger(f"focus scann Start")

        self.folderPath = self.__runPreconditions()

        if not self.folderPath:
            self.loger("focus scann End No path provided")
            return False

        self.manipulatorInterface.fokus0(self.focusMax)

        if algo:
            self.__runAlgo()
        else:
            self.__runNOAlgo()

        self.loger(f"focus scann End")

    def __runNOAlgo(self):

        for i in range(self.steps):
            cv.imwrite(self.folderPath + str(i) + ".png", self.camera.getFrame())

            self.manipulatorInterface.fokusDown(self.focusStep)

            self.loger(f"focus scann progres: {int((i / self.steps) * 100)}%")

    def __runAlgo(self):

        for factor in self.factors:
            factor.cleanFiles()

        for i in range(self.steps):
            img = self.camera.getFrame()

            cv.imwrite(self.folderPath + str(i) + ".png", img)

            for factor in self.factors:
                factor.saveResults(img, i, self.manipulatorInterface.fokusPos, self.folderPath)

            self.manipulatorInterface.fokusDown(self.focusStep)

            self.loger(f"focus scann progres: {int((i / self.steps) * 100)}%")

        self.show(self.folderPath)

    @staticmethod
    def extract_integer(filename):
        match = re.search(r"1_([+-]?[0-9.]+)_([0-9.]+)\.([0-9.]+)\.png", filename)
        if match:
            return int(match.group(1))
        else:
            return None

    def runFilm(self):

        files = os.listdir(r"C:\Users\Administrator\Desktop\Filmik")
        png_files = sorted([file for file in files if file.endswith('.png')], key=self.extract_integer)

        for i, file in enumerate(png_files):
            print(i)
            img = cv2.imread("C:\\Users\\Administrator\\Desktop\\Filmik\\" + file, cv2.IMREAD_GRAYSCALE)
            for factor in self.factors:
                factor.saveResults(img, i)

        self.show()

    def show(self, path=None):
        for factor in self.factors:
            factor.show(plt)

        if path:
            plt.savefig(path + "Main_Plot.png")

    def fokusForCurrentFrame(self):
        img = self.camera.getFrame()
        for factor in self.factors:
            factor.logResults(img, self.manipulatorInterface.fokusPos)
