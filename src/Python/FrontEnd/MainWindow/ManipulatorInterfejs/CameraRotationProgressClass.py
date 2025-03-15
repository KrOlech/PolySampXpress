from Python.Utilitis.GenericProgressClass import GenericProgressClass


class CameraRotationProgressClass(GenericProgressClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.finaliseGUISingleButtonCancel()

    def end(self):
        self.accept()
        self.master.showResultsRotationCalculation()

    def cancelPressed(self):
        self.master.StopTheRotationCalculation = True
        self.accept()
