from PyQt5.QtWidgets import QWidget, QVBoxLayout

from MAP.GUI.MapLabel import MapLabel


class MapWindow(QWidget):
    mapPQ = []  # mapa w Pyqt
    map = []  # mapa jako tablica numpy

    def __init__(self, master, windowSize, *args, **kwargs):
        super(MapWindow, self).__init__(*args, **kwargs)

        self.master = master

        self.mapViue = MapLabel(self)

        self.setFixedSize(windowSize)
        self.mapViue.setFixedSize(windowSize)

        self.mapPQ = master.cameraView.getFrame()


        leyout = QVBoxLayout()
        leyout.addWidget(self.mapViue)
        self.setLayout(leyout)
