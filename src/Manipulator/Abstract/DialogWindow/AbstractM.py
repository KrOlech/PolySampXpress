from abc import ABCMeta

from src.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog


class AbstractDialogMaster(AbstractDialog):
    __metaclass__ = ABCMeta

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.master = master

    def cancelPressed(self):
        self.master.stop()
        self.accept()
