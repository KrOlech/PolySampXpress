import cv2
from PyQt5.QtCore import Qt

from Python.Interface.ManipulatorInterfejs.Abstract.AbstractManipulatroInterfejs import \
    AbstractManipulatorInterferes
from Python.Interface.ManipulatorInterfejs.Selection.Select import SelectManipulator
from PIL import Image, ImageFilter
import numpy
import scipy.optimize as optimize
import matplotlib.pyplot as plt
import time

class ManipulatorInterfere(AbstractManipulatorInterferes, SelectManipulator):

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, windowSize, myStatusBar, *args, **kwargs)

        # keyboard = [Qt.Key_W, Qt.Key_A, Qt.Key_D, Qt.Key_S]
        keyboard2 = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        # [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]
        [a.setShortcut(k) for a, k in zip(self.actions, keyboard2)]

        [a.setShortcutContext(Qt.WindowShortcut) for a in self.actions]

        [self.master.addAction(a) for a in self.actions]

        # self.autoFokus()

    def __calcucateFokus(self):
        image = self.master.camera.getFrame()
        return cv2.Laplacian(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()

    def autoFokusOld(self):

        treshold = self.__calcucateFokus()
        self._focusManipulator.x -= 1
        self._focusManipulator.gotoNotAsync()

        while True:
            focusMetric = self.__calcucateFokus()

            if focusMetric < treshold:
                self._focusManipulator.x -= 1
            if focusMetric > treshold:
                self._focusManipulator.x += 1
            self._focusManipulator.gotoNotAsync()

            newTreshold = self.__calcucateFokus()

            self.loger(treshold, newTreshold)

            if round(newTreshold - treshold, 2) == 0:
                break
            else:
                treshold = newTreshold

    def autoFokus(self):
        input_image = Image.open('..\\cell.jpg')

        plt.ion()
        fig, ax = plt.subplots()
        display = ax.imshow(numpy.array(input_image))
        fig.canvas.draw()

        min_focus = -5
        max_focus = 5
        initial_focus = 2.5
        tolerance = 0.05
        max_iteration = 15

        fun = lambda x: self.opt_function(x)
        res = optimize.minimize(fun, x0=[1], bounds=[(-5, 5)], method='COBYLA', tol=tolerance,
                                options={'maxiter': max_iteration})
        print(res)

    @staticmethod
    def image_sharpness(img):
        m = numpy.mean(img)
        img_s = numpy.add(-m, img)
        img_sq = numpy.multiply(img_s, img_s)
        r = numpy.sum(img_sq)
        return r


    def opt_function(self,x):
        img = self.camera_simulator(x)
        print(x)
        return (-self.image_sharpness(img))


    def camera_simulator(self,x, focus_point=-2.43):
        gauss_image = self.input_image.filter(ImageFilter.GaussianBlur(abs(x - focus_point)))
        img = numpy.array(gauss_image)
        display.set_data(img)
        fig.canvas.draw()
        plt.pause(0.1)
        return (img)
