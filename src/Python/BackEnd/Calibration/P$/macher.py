import csv

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



class Fitter:

    data = None

    sampling_frequency = 1

    def __init__(self, file_path):
        self.filePath = file_path

        self.rowData = self.__read_csv_file()

        self.data = self.__resolvData()

        self.time_values = range(len(self.data))



    def __read_csv_file(self):
        # Open the CSV file in read mode
        with open(self.filePath, 'r') as file:
            table = [row for row in csv.reader(file)]

        np.array(table, dtype=float)

        return table


    def __resolvData(self):
        return [np.argmax(self.rowData[i, :]) for i in range(self.rowData.shape[0])]

    def fit(self):
        fft_result = np.fft.fft(self.data)

        frequencies = np.fft.fftfreq(len(self.data), d=1 / self.sampling_frequency)

        max_index = np.argmax(np.abs(fft_result[1:])) + 1

        initial_amplitude_guess = np.abs(fft_result[max_index]) / len(self.data)
        initial_frequency_guess = frequencies[max_index]
        initial_phase_guess = np.angle(fft_result[max_index])

    def __fit(self, sinusoidal_function):
        return curve_fit(sinusoidal_function, time_values, amplitude_values,
                               p0=[initial_amplitude_guess, initial_frequency_guess, initial_phase_guess])

    @staticmethod
    def sinusoidal_function(t, amplitude, frequency, phase):
        return amplitude * np.sin(2 * np.pi * frequency * t + phase)



    @staticmethod
    def plotImshow(data_array):
        plt.imshow(data_array, cmap='gray')
        plt.show()