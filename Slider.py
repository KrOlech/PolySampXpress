from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class Slider(QSlider):
    '''
    Obiekt dziedzicacy z Qslidera umozliwiajacy obsluge osi x
    manipulatora odpowiadajacego za przyblizenie kamery
    '''
    max_slidera = 1000

    def __init__(self, mainwinow, min, max, value=int(25), *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        self.mainwindow = mainwinow

        # wartosci na slajderze
        self.max, self.min, self.value = max, min, value

        # przpisanie funkcji do zmiany wartosci na sliderze
        self.valueChanged[int].connect(self.zmiana)

        # ustawienia wygladu i parametrow slidera
        self.setFocusPolicy(Qt.StrongFocus)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setTickInterval(100)
        self.setSingleStep(10)
        self.setMaximum(self.max_slidera)
        self.setMinimum(0)
        self.setValue(self.rekonwersja(self.value))

    def konwersja(self, wartosc):
        '''
        konwersja wartosci z wartosci w przestrzeni
        slidera na wartosc rzeczywista
        :param wartosc: wartosc w przestrzeni slidera
        :return: wartosc w przestrzeni rzeczywistej
        '''
        wynik = wartosc / self.max_slidera
        wynik *= (self.max - self.min)
        wynik += self.min
        return wynik

    def rekonwersja(self, wartosc):
        '''
        konwersja wartosci z przestrzeni rzeczywistej
        na przestrzen slidera
        :param wartosc: wartosc w przestrzeni rzeczywistej
        :return: wartosc w przestrzeni slidera
        '''
        wynik = (wartosc - self.min)
        wynik /= (self.max - self.min)
        wynik *= self.max_slidera
        return int(wynik)

    def zmiana(self, wartosc):
        self.value = self.konwersja(wartosc)
        self.mainwindow.manipulaor.przesun_x(self.konwersja(wartosc))

    def ustaw_min_max(self, min, max):
        self.max, self.min = int(max), int(min)
        self.setValue(self.rekonwersja(self.value))


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
