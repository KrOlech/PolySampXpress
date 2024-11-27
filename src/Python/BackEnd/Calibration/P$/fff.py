import numpy as np


class resolveFurier:

    def __init__(self, data):
        self.data = data
        self.time_values = range(len(data))

    def fff(self):
        fft_result = np.fft.fft(self.data)

        # Compute the frequencies
        sampling_frequency = 1
        frequencies = np.fft.fftfreq(len(self.time_values), d=1 / sampling_frequency)

        # Find index of maximum amplitude in FFT result (excluding DC component at index 0)
        max_index = np.argmax(np.abs(fft_result[1:])) + 1

        return np.abs(fft_result[max_index]) / len(self.data), frequencies[max_index], np.angle(fft_result[max_index])
