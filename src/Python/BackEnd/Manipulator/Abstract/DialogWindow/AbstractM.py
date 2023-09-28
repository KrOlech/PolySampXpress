from abc import ABCMeta

from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog


class AbstractDialogMaster(AbstractDialog):
    __metaclass__ = ABCMeta

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.master = master

    def cancelPressed(self): #TODO may be Uncorect not allweys master is manipulator and master have a manipulator to stop is ok handled but need beter implementation
        try:
            self.master.stop()
        except AttributeError as e:
            self.logError(e)

        try:
            self.master.manipulatorInterferes.stop()
        except AttributeError as e:
            self.logError(e)

        self.accept()
