from PyQt5.QtCore import Qt

from src.BaseClass.Slider.Slider import Slider


class ZoomSlider(Slider):
    minV = 0
    maxV = 1

    __change = False

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.minV, self.maxV, *args, orientation=Qt.Vertical, **kwargs)

        self.setFixedWidth(20)
        self.setFixedHeight(150)

    def change(self, value):

        if self.__change:
            self.__change = False
            return

        if not self.master.zoomChange:
            self.master.zoomValueChange()
        elif not self.master.zoomChange:
            self.__change = True
            self.setValue(self.value)
        else:
            super().change(value)
            self.master.zoomManipulator.zoomManipulatorChange(self.value)
            self.master.zoomLabel.setText(str(self.value))
