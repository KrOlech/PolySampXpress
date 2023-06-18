from abc import abstractmethod, ABCMeta

from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt

from src.BaseClass.Abstract import abstractmetod


class Slider(QSlider):
    __metaclass__ = ABCMeta

    maxSlider = 1000

    def __init__(self, master, minV, maxV, value=int(25), orientation=Qt.Horizontal, widget=None, *args, **kwargs):
        super(Slider, self).__init__(orientation, widget, *args, **kwargs)
        self.master = master

        self.max, self.min, self.value = maxV, minV, value

        self.valueChanged[int].connect(self.change)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setTickInterval(100)
        self.setSingleStep(10)
        self.setMaximum(self.maxSlider)
        self.setMinimum(0)
        self.setValue(self.reconversion(self.value))

    def conversion(self, value):
        value = value / self.maxSlider
        value *= (self.max - self.min)
        value += self.min
        return value

    def reconversion(self, value):
        value = (value - self.min)
        value /= (self.max - self.min)
        value *= self.maxSlider
        return int(value)

    @abstractmethod
    def change(self, value):
        self.value = self.conversion(value)

    def set_min_max(self, minV, maxV):
        self.max, self.min = int(maxV), int(minV)
        self.setValue(self.reconversion(self.value))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QMainWindow, QApplication
    import sys as sys


    class Obiekt_tymczasowy:
        def __int__(self):
            pass

        def przesun_x(self, *args, **kwargs):
            pass


    class MainWindow(QMainWindow):
        manipulaor = Obiekt_tymczasowy()


    app = QApplication(sys.argv)

    okno = MainWindow()

    okno.setCentralWidget(Slider(okno, -1, 1))

    okno.show()

    app.exec_()
