from abc import ABCMeta
from src.manipulator.DialogWindow.AbstractM import AbstractDialogManipulator


class AbstractWindow(AbstractDialogManipulator):
    __metaclass__ = ABCMeta

    @property
    def windowName(self):
        return "Calibration"
