from PyQt5.QtCore import Qt

from src.BaseClass.Slider.Slider import Slider


class ManipulatorSlider(Slider):
    minV = -10000
    maxV = 10000

    def __init__(self, master, value, *args, **kwargs):
        super().__init__(master, self.minV, self.maxV, value, *args, orientation=Qt.Vertical, **kwargs)

        self.setFixedWidth(20)
        self.setFixedHeight(150)

    def change(self, value):
        super().change(value)
        self.master.x = self.value
        self.master.gotoNotAsync()
