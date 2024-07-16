from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class ZoomInfoWindow(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Zoom in progress"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow("", self.okButton)

        self.setMinimumWidth(150)

    def run(self):
        workFunWorker(self, self.master.zoomChangeAction, self.end)

    def end(self):
        self.accept()
