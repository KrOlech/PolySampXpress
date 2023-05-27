from PyQt5.QtWidgets import QLabel

from src.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow
from src.Calibration.Propertis.Propertis import CalibrateProperty

from src.BaseClass.JsonRead.JsonRead import JsonHandling


class CalibrationResultsDialog(AbstractWindow, JsonHandling, CalibrateProperty):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        data = self.readFile(self.configFile)

        for index in range(2):
            legend = self.indexLegend[index]
            values = data["0"]["offsets"][legend]

            self.form.addRow(QLabel(f"{legend}: "), QLabel(str(values)))

        self.form.addRow(QLabel(""), self.okButton)

