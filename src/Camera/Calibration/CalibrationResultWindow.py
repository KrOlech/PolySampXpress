from src.manipulator.DialogWindow.Abstract import AbstractDialog
from src.Camera.Calibration.Propertis import CalibrateProperty
from src.utilitis.JsonRead.JsonRead import JsonHandling


class CalibrationResultsDialog(AbstractDialog, JsonHandling, CalibrateProperty):

    def __int__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        data = self.readFile(self.configFile)

        for index in range(2):
            legend = self.indexLegend[index]
            values = data["0"]["offsets"][legend]

            self.form.addRow(QLabel(f"{legend}: "), str(values))

        self.form.addRow(QLabel(""), self.okButton)
