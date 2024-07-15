from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class MoveByValue(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Move By Value"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.valueX = self.createQSpinBox(0)
        self.valueY = self.createQSpinBox(0)

        self.form.addRow(f'X: {self.master.x}+ ', self.valueX)
        self.form.addRow(f'Y: {self.master.y}+ ', self.valueY)

        self.finaliseGUI()
        self.setFixedWidth(180)

    def okPressed(self):
        self.createWaitingLabel()
        workFunWorker(self, self.goToThreadFun, self.endThread)

    def goToThreadFun(self):
        self.master.goToCords(x=self.valueX.value(), y=self.valueY.value())

    def endThread(self):
        self.accept()
