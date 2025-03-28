from Python.Utilitis.GenericProgressClass import GenericProgressClass


class SampleAccessProgressWindow(GenericProgressClass):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.finaliseGUISingleButtonCancel()

    def cancelPressed(self):
        self.master.manipulatorInterferes.stop()
