from PyQt6.QtCore import Qt

from Python.BaseClass.Slider.Slider import Slider


class ManipulatorSlider(Slider):
    minV = -10
    maxV = 21000

    def __init__(self, master, value, *args, **kwargs):
        super().__init__(master, self.minV, self.maxV, value, *args, orientation=Qt.Orientation.Vertical, **kwargs)

        self.setFixedWidth(20)
        self.setFixedHeight(self.parent().geometry().height() - 100 - 200)

    def setMaster(self, master):

        self.master = master

    def change(self, value):
        super().change(value)
        if self.master:
            self.master.goToCords(self.value)
