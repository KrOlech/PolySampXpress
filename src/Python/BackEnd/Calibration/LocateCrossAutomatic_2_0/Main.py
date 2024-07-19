import numpy as np
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import array, transpose, linspace
from scipy.optimize import curve_fit
from scipy.stats import norm

from Python.BaseClass.Logger.Logger import Loger
from matplotlib import pyplot as plt


class LocateCross(Loger):
    x, y = 0, 0
    dataX, dataY = None, None

    def __init__(self, master, name=""):
        self.master = master
        self.name = name

    def locateCross(self, negation=False):
        photo = self.master.camera.getFrame()

        gsc = cvtColor(photo, COLOR_BGR2GRAY)

        self.x, self.dataX, self.fitX = self.analyzePhotoX(gsc, negation)
        self.y, self.dataY, self.fitY = self.analyzePhotoY(gsc, negation)

        self.loger(
            f"position of the marker point: {self.x} px, {self.y}px  for zoom:{self.master.zoom} with name: {self.name}")  # todo when Zoom implemented add zoom value

        self.__crateAndSaveResults(self.markSpot(photo))

        return self.x, self.y

    @staticmethod
    def analyzePhotoX(photo, negation=False):
        return LocateCross.__analyzePhoto(photo, negation)

    @staticmethod
    def analyzePhotoY(photo: array, negation=False):
        return LocateCross.__analyzePhoto(transpose(photo), negation)

    @staticmethod
    def __analyzePhotoOld(photo, negation=False):
        rowValue = [sum(row) for row in photo]
        mValue = max(rowValue)
        if negation:
            return rowValue.index(max(rowValue)), [v / mValue for v in rowValue]
        else:
            return rowValue.index(min(rowValue)), [v / mValue for v in rowValue]

    @staticmethod
    def __analyzePhoto(photo, negation=False):
        rowValue = [sum(row) for row in photo]
        mValue = max(rowValue)
        rowValue = [v / mValue for v in rowValue]

        xS = np.linspace(0, len(rowValue), len(rowValue))

        popt, pcov = curve_fit(LocateCross.func, xS, rowValue)

        if negation:
            return int(popt[-1]), rowValue, [LocateCross.func(x, *popt) for x in xS]
        else:
            return int(popt[-1]), rowValue, [LocateCross.func(x, *popt) for x in xS]

    @staticmethod
    def furier(photo):
        rowValue = [sum(row) for row in photo]
        mValue = max(rowValue)
        row = [v / mValue for v in rowValue]

        fft_result = np.fft.fft(row)
        # Compute the frequencies
        sampling_frequency = 1  # Sampling frequency
        frequencies = np.fft.fftfreq(len(row), d=1 / sampling_frequency)

        plt.figure()
        plt.plot(frequencies, np.abs(fft_result))  # Plot magnitude of FFT result
        plt.xlabel('Frequency')
        plt.ylabel('Magnitude')
        plt.title('FFT Result')
        plt.grid()
        plt.show()

    @staticmethod
    def func(x, a, b, c):
        return 1 / np.sqrt(2 * np.pi * a * a) * np.exp(-(x - b) * (x - b) / (2 * a * a)) + c

    def markSpot(self, photo):
        for i in range(max(0, self.x - 6), min(self.x + 5, len(photo))):
            for j in range(max(0, self.y - 6), min(self.y + 5, len(photo[0]))):
                photo[i][j] = [1., 0., 0.]
        return photo

    def __crateAndSaveResults(self, photo):
        fig, axs = plt.subplots(2, 2, figsize=(6, 6))

        axs[0, 0].imshow(photo)

        x = len(self.dataX)
        y = len(self.dataY)

        axs[0, 1].plot(self.dataX, linspace(0, x, x))
        axs[1, 0].plot(linspace(0, y, y), self.dataY)
        axs[0, 1].plot(self.fitX, linspace(0, x, x))
        axs[1, 0].plot(linspace(0, y, y), self.fitY)

        axs[0, 1].invert_xaxis()
        axs[0, 1].invert_yaxis()

        axs[0, 0].axis('off')
        axs[1, 1].axis('off')

        plt.savefig(f"{self.name}.png")


if __name__ == "__main__":
    from Python.BackEnd.Calibration.LocateCrossAutomatic_2_0.dumyCamera import dumyCamera

    main = dumyCamera()
    loc = LocateCross(main)
    loc.locateCross()
