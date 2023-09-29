from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from src.Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class GoToCordsDialog(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Go To Cords"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.master.x)
        self.valueY = self.createQSpinBox(self.master.y)

        self.form.addRow('X:', self.valueX)
        self.form.addRow('Y:', self.valueY)

        self.finaliseGUI()
        self.setFixedWidth(180)

    def okPressed(self):
        self.createWaitingLabel()
        workFunWorker(self, self.goToThreadFun, self.endThread)

    def goToThreadFun(self):
        self.master.goToCords(x=self.valueX.value(), y=self.valueY.value())

    def endThread(self):
        self.accept()
