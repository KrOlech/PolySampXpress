import asyncio

from PyQt5.QtCore import Qt

from Python.BaseClass.Slider.LabeledSlider import LabeledSlider


class ZoomSlider(LabeledSlider):
    minV = 0
    maxV = 10

    __change = False

    labels = (0.8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    labelsDictionary = {0: 0.85, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    def __init__(self, master, widget):
        super().__init__(self.minV, self.maxV, orientation=Qt.Vertical, parent=widget, labels=self.labels)

        self.master = master

        self.sl.valueChanged[int].connect(self.change)

        self.setFixedWidth(50)
        self.setFixedHeight(200)

    def change(self, value):

        if self.__change:
            self.__change = False
            return

        if not self.master.zoomChange:
            self.master.zoomValueChange()

        if not self.master.zoomChange:
            self.__change = True
            self.sl.setValue(0)
        else:
            self.sl.setValue(value)
            asyncio.run(self.master.zoomManipulator.zoomManipulatorChange(value))
            self.master.zoomLabel.setText(str(self.labelsDictionary[value]))
