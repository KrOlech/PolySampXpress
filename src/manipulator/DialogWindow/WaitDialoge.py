from src.manipulator.DialogWindow.Abstract import AbstractDialog
from src.utilitis.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class HomeAxisDialog(AbstractDialog):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.createWaitingLabel()

    def run(self):
        workFunWorker(self, self.manipulator.homeAxis, self.end)

    def end(self):
        self.accept()
