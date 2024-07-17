from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker
from PyQt5.QtWidgets import QLabel


class GenericProgressClass(AbstractDialogMaster):

    @property
    def windowName(self):
        return self._windowName

    @windowName.setter
    def windowName(self, value):
        self._windowName = value

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, value):
        self._function = value

    def __init__(self, name, fun, size, *args, **kwargs):
        self.windowName = name

        super().__init__(*args, **kwargs)

        self.function = fun

        self.form.addRow(self.windowName, QLabel(""))

        self.setMinimumWidth(size)

    def run(self):
        workFunWorker(self, self.function, self.end)

    def end(self):
        self.accept()

    def okPressed(self):
        pass
