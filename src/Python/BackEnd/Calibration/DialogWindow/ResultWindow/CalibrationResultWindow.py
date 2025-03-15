from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow
from Python.BackEnd.Calibration.Propertis.Propertis import CalibrateProperty

from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class CalibrationResultsDialog(AbstractWindow, JsonHandling, CalibrateProperty):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master.manipulatorInterferes, *args, **kwargs)

        data = self.readFile(self.configFile)

        for index in range(2):
            legend = self.indexLegend[index]
            values = data[str(int(master.master.zoom))]["offsets"][legend]

            self.form.addRow(QLabel(f"{legend}: "), QLabel(str(abs(values))))

        self.finaliseGUISingleButton()

