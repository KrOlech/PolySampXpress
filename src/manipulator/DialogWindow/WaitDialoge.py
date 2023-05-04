from src.manipulator.DialogWindow.AbstractM import AbstractDialogManipulator
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class HomeAxisDialog(AbstractDialogManipulator):

    @property
    def windowName(self):
        return "Homing"

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.createWaitingLabel()

    def run(self):
        workFunWorker(self, self.manipulator.homeAxis, self.end)

    def end(self):
        self.accept()
