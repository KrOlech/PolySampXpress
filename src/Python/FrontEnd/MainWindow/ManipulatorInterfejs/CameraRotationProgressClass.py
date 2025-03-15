from Python.Utilitis.GenericProgressClass import GenericProgressClass


class CameraRotationProgressClass(GenericProgressClass):

    def end(self):
        self.accept()
        self.master.showResultsRotationCalculation()
