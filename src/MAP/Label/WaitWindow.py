from src.Manipulator.Abstract.DialogWindow.WaitDialoge import HomeAxisDialog
from src.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class WaitWindow(HomeAxisDialog):

    @property
    def windowName(self):
        return "Go to Selected location"

    def run(self, event):
        workFunWorker(self, lambda : self.master.threadFun(event), self.end)
