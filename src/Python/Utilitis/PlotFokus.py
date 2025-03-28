import os
import time

import numpy as np
import scipy
from cv2 import imread, IMREAD_GRAYSCALE
from matplotlib import patches
from scipy.signal import peak_widths

from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness, image_sharpness2, sobel, \
    fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness

import matplotlib.pyplot as plt

from scipy.interpolate import interp1d

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset


class PlotFokus:

    def __init__(self, fun, path, readOld=True, data={None: None}):
        self.executionTimes = []

        self.fun = fun

        self.funName = fun.__name__

        print(self.funName)

        self.rowPath = path

        self.path = path + f"{self.funName}_new.dat"

        if not readOld:
            self.x, self.y, self.nY, self.z = self.__resolvData()
        else:
            self.x, self.y, self.nY, self.z = self.__recalculateMetric(data)

        self.peaks = self.resolvePeeks()

        self.results_half = self.halfWidth()

        if len(self.executionTimes):
            print(f"{self.funName} Executed in {np.mean(self.executionTimes):.6f} seconds")

    def __call__(self, img, *args, **kwargs):
        start_time = time.time()
        self.value = self.fun(img)
        end_time = time.time()
        execution_time = end_time - start_time
        self.executionTimes.append(execution_time)
        return self.fun(img)

    def __resolvData(self):
        x = []
        y = []
        z = []
        with open(self.path, "r") as file:
            while line := file.readline():
                x.append(float(line[:line.find(",")]))
                y.append(float(line[line.find(",") + 1:line.rfind(",")]))
                z.append(float(line[line.rfind(",") + 1:]))

        maxY = max(y)

        try:
            nY = [w / maxY for w in y]
        except ZeroDivisionError as e:
            nY = []

        return x, y, nY, z

    def resolvePeeks(self):
        rpeaks, _ = scipy.signal.find_peaks(self.nY)

        peaks = []

        for peek in rpeaks:
            if self.nY[peek] > min(self.nY) + 0.1:
                peaks.append(peek)

        print(f"Peeks: {peaks}")

        return peaks

    def halfWidth(self):
        widths = peak_widths(self.nY, self.peaks)
        print(f"Half widths: {widths[0]}")

        if all(self.z):
            dz = self.z[1] - self.z[0]
            widths = [width * dz for width in widths]

        return widths

    def plot(self, plot):

        dictLegend = {
            "image_sharpness": "Mean-Based",
            "image_sharpness2": "Gradient-Based",
            "sobel": "Sobel Operator Variance",
            "fft_based_sharpness": "Fast Fourier Transform Variance",
            "scharr_variance": "Scharr Operator Variance",
            "edge_based_sharpness": "Canny Edge-Based",
            "lpc_based_sharpness": "Local Phase Coherence-Based"
        }

        try:
            if self.funName == "sobel":
                plot.plot(self.x, self.nY, label=dictLegend[self.funName], linewidth=2.5, linestyle="dotted")
                return

            if all(self.z) and False:
                plot.plot(self.z, self.nY, label=dictLegend[self.funName], linewidth=1)
            else:
                plot.plot(self.x, self.nY, label=dictLegend[self.funName], linewidth=1)
        except ZeroDivisionError:
            self.logError("Max focus is 0")
        except ValueError:
            pass

        # if len(self.results_half):
        #    plt.hlines(*self.results_half[1:], color="C3")

    def __recalculateMetric(self, data):

        results = {name: self(img) for name, img in data.items()}

        x = []
        y = []

        for xp, yp in sorted(results.items()):
            x.append(xp)
            y.append(yp)

        z = []
        with open(self.path, "r") as file:
            while line := file.readline():
                z.append(float(line[line.rfind(",") + 1:]))

        maxY = max(y)

        try:
            nY = [w / maxY for w in y]
        except ZeroDivisionError as e:
            nY = []

        try:
            os.remove(self.rowPath + f"{self.funName}_new.dat")
        except FileNotFoundError:
            pass

        with open(self.rowPath + f"{self.funName}_new.dat", "x") as file:
            for a, b, c, in zip(x, y, z):
                file.write(f"{a},{b},{c}\n")

        return x, y, nY, z


def loadImages(rowPath):
    files = [file for dirs in os.walk(rowPath, topdown=True)
             for file in dirs[2] if file.endswith(".png")]

    results = {}

    for file in files:

        try:
            name = int(file[file.rfind("\\") + 1:-4])
        except ValueError:
            pass
        else:

            os.chdir(rowPath)

            img = imread(file, IMREAD_GRAYSCALE)

            results[name] = img

    return results


def plotAll(data=("Qr code", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\FilmikV4 - u")):
    funs = [image_sharpness, image_sharpness2, sobel, fft_based_sharpness, scharr_variance, edge_based_sharpness,
            lpc_based_sharpness]

    # funs = [edge_based_sharpness]

    # dane = loadImages(data[1] + "\\")
    dane = None

    factors = [PlotFokus(fun, data[1] + "\\", readOld=False, data=dane) for fun in funs]

    fig, ax = plt.subplots(figsize=(5, 5))

    for factor in factors:
        factor.plot(ax)

    plt.title(data[0], loc="left", fontsize=16, pad=10)

    ax.set_xlabel("Relative Focus position")
    ax.set_ylabel("Normalise Focus value")

    # leaf
    # ax_inset = fig.add_axes([0.53, 0.5, 0.45, 0.45])

    # nigra qr
    # ax_inset = fig.add_axes([0.54, 0.1, 0.45, 0.45])

    # for factor in factors:
    #    factor.plot(ax_inset)

    # leaf
    # zoom_x_start, zoom_x_end = 40, 80
    # zoom_y_start, zoom_y_end = 0.6, 1.05

    # nigra
    # zoom_x_start, zoom_x_end = 15, 35
    # zoom_y_start, zoom_y_end = 0.7, 1.05

    # qr
    # zoom_x_start, zoom_x_end = 35, 52
    # zoom_y_start, zoom_y_end = 0.6, 1.05

    # ax_inset.set_xlim(zoom_x_start, zoom_x_end)
    # ax_inset.set_ylim(zoom_y_start, zoom_y_end)

    # ax_inset.set_xticks([])
    # ax_inset.set_yticks([])
    # ax_inset.set_xticklabels([])
    # ax_inset.set_yticklabels([])

    # rect = patches.Rectangle(
    #    (zoom_x_start, zoom_y_start),  # Bottom-left corner
    #    zoom_x_end - zoom_x_start,  # Width
    #    zoom_y_end - zoom_y_start,  # Height
    #    linewidth=1.5, edgecolor="gray", linestyle="dashed", facecolor="none"
    # )
    # ax.add_patch(rect)

    # leaf
    # ax.set_xlim(0, 80)
    # ax.set_ylim(0, 1.4)

    # nigra
    # ax.set_xlim(0, 100)
    # ax.set_ylim(0, 1.4)

    # ax.set_xlim(0, 130)
    # ax.set_ylim(0, 1.4)

    # ax.set_xlim(15, 155)
    # ax.set_ylim(0, 1.4)

    # leaf
    # ax.legend(loc='lower right')

    # nigra
    ax.set_xlim(17, 37)
    ax.set_ylim(0.9, 1.01)

    # nigra
    # ax.legend(loc="lower left")#loc='lower right')#loc='lower center')#loc='upper right')

    ax.set_aspect(abs((ax.get_xlim()[1]- ax.get_xlim()[0]) / (ax.get_ylim()[1]- ax.get_ylim()[0])))
    #fig.savefig(data[0] + "main_zoom.eps", format='eps' )
    #fig.savefig(data[0] + "main.eps", format='eps')
    #fig.show()

    handles, labels = ax.get_legend_handles_labels()

    # Get legend handles and labels
    handles1, labels1 = handles[:3], labels[:3]
    handles2, labels2 = handles[3:], labels[3:]
    plt.close(fig)

    fig1 = plt.figure()
    ax1 = fig1.add_axes([0, 0, 1, 1])  # Use full figure space
    ax1.legend(handles1, labels1, loc="center")
    ax1.axis("off")  # Hide axes
    plt.savefig(data[0] + "Legend1.eps", format='eps')

    # Create second legend figure
    fig2 = plt.figure()
    ax2 = fig2.add_axes([0, 0, 1, 1])  # Use full figure space
    ax2.legend(handles2, labels2, loc="center")
    ax2.axis("off")  # Hide axes


    plt.savefig(data[0] + "Legend2.eps", format='eps')

    #plt.show()


if __name__ == "__main__":
    qr1 = ("Qr code", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\FilmikV4 - u")
    qr2 = ("Qr code 2", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\21_Luty_Scan_13_QR")
    ngra = ("NIGRA", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\21_Luty_Scan_3_125011_NIGRA") # - artefakty
    liscV1 = ("Leaf", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\liscV1")
    tau = ("nw0", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\21_Luty_Scan_12_124867") # - klej na szkle
    nw = ("nw", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\21_Luty_Scan_7_125011") # Jondra komurek glejowych jakby zeskanwac raz jesce to by byly neurony dopaminergiczne istoty czarnej
    tauW = ("TAU", r"C:\Users\Zenbook\Documents\AryKuły\Fokus\Data\21_Luty_Scan_2_124898_TAU") # - nie wybarwiona tkanka

    #data = [qr1, qr2, ngra, liscV1, tau, nw, tauW]
    #For d in data:
    #    plotAll(d)
    plotAll(tauW)
