import os
import re
import cv2

from Python.BackEnd.SzarpnesCalculation.CalculateAndSaveResults import CalculateAndSaveResults
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness, image_sharpness2, sobel, \
    fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness

import matplotlib.pyplot as plt


class SzarpnesCalculation:
    funs = [image_sharpness, image_sharpness2, sobel, fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness]

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

        self.factors = [CalculateAndSaveResults(fun) for fun in self.funs]

    def run(self):
        self.manipulatorInterface.fokus0()

        for i in range(100):
            img = self.camera.getFrame()
            for factor in self.factors:
                factor.saveResults(img, i)
            self.manipulatorInterface.fokusUp()

        self.show()
    @staticmethod
    def extract_integer(filename):
        match = re.search(r"1_([+-]?[0-9.]+)_([0-9.]+)\.([0-9.]+)\.png", filename)
        if match:
            return int(match.group(1))
        else:
            return None

    def runFile(self):

        files = os.listdir(r"C:\Users\Administrator\Desktop\Filmik")
        png_files = sorted([file for file in files if file.endswith('.png')], key=self.extract_integer)

        for i, file in enumerate(png_files):
            print(i)
            img = cv2.imread("C:\\Users\\Administrator\\Desktop\\Filmik\\" + file, cv2.IMREAD_GRAYSCALE)
            for factor in self.factors:
                factor.saveResults(img, i)

        self.show()

    def show(self):
        for factor in self.factors:
            factor.show(plt)

        plt.legend()
        plt.show()
