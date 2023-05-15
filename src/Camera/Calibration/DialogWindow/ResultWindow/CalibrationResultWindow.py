from PyQt5.QtWidgets import QLabel

from src.Camera.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow
from src.Camera.Calibration.Propertis.Propertis import CalibrateProperty

from src.utilitis.JsonRead.JsonRead import JsonHandling


class CalibrationResultsDialog(AbstractWindow, JsonHandling, CalibrateProperty):

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        data = self.readFile(self.configFile)

        for index in range(2):
            legend = self.indexLegend[index]
            values = data["0"]["offsets"][legend]

            self.form.addRow(QLabel(f"{legend}: "), QLabel(str(values)))

        self.form.addRow(QLabel(""), self.okButton)

