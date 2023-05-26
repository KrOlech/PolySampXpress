from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogManipulator
from src.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class GoToCordsDialog(AbstractDialogManipulator):

    @property
    def windowName(self):
        return "Go To Cords"

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.manipulator.x)
        self.valueY = self.createQSpinBox(self.manipulator.y)

        self.form.addRow('X:', self.valueX)
        self.form.addRow('Y:', self.valueY)

        self.finaliseOutput()
        self.setFixedWidth(180)

    def okPressed(self):
        self.createWaitingLabel()
        workFunWorker(self, self.goToThreadFun, self.endThread)

    def goToThreadFun(self):
        self.manipulator.goToCords(x=self.valueX.value(), y=self.valueY.value())

    def endThread(self):
        super(GoToCordsDialog, self).okPressed()
