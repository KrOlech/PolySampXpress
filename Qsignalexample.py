from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget


class example(QWidget):
    newROISignal = pyqtSignal()

    def __init__(self):
        super(example, self).__init__()

    @pyqtSlot()
    def newROISlot(self):
        print("WIP")


if __name__ == '__main__':
    temp = example.newROISignal.emit()
