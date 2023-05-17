from abc import ABCMeta

from src.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog


class AbstractDialogManipulator(AbstractDialog):
    __metaclass__ = ABCMeta

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.manipulator = manipulator

    def cancelPressed(self):
        self.manipulator.stop()
        self.accept()
