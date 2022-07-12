from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class _Slider(QSlider):

    maxSlider = 1000

    def __init__(self, mainWindow, minV, maxV, value=int(25), *args, **kwargs):
        super(_Slider, self).__init__(Qt.Horizontal, *args, **kwargs)
        self.mainWindow = mainWindow

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

    def change(self, value):
        self.value = self.conversion(value)
        self.mainWindow.manipulaor.przesun_x(self.conversion(value))

    def set_min_max(self, minV, maxV):
        self.max, self.min = int(maxV), int(minV)
        self.setValue(self.reconversion(self.value))


class Slider(_Slider):

    def __init__(self, mainWindow, cP, *args, **kwargs):
        self.communicationPoint = cP
        super(Slider, self).__init__(mainWindow, cP.min, cP.max, cP.value, *args, **kwargs)

    def change(self, value) -> None:
        self.value = self.conversion(value)
        self.mainWindow.camera.device.set(self.communicationPoint.address, self.value)


if __name__ == '__main__':
    # test nie aktualny testuje klase _Slider nie Slider
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

    okno.setCentralWidget(_Slider(okno, -1, 1))

    okno.show()

    app.exec_()
