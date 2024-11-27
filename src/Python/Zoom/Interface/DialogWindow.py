from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class ZoomChangeDialogWindow(AbstractDialogMaster):


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.finaliseGUI()
    @property
    def windowName(self):
        return "Zoom change"

    @property
    def okName(self):
        return "Yes"

    @property
    def CancelName(self):
        return "No"

    def okPressed(self):
        self.master.zoomChange = True
        self.accept()

    def cancelPressed(self):
        self.master.zoomChange = False
        self.accept()
