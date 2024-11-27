from abc import ABCMeta
from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class AbstractWindow(AbstractDialogMaster):
    __metaclass__ = ABCMeta

    @property
    def windowName(self):
        return "Calibration"
