from PyQt5.QtWidgets import QLabel

from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class InacuracyResultWindow(AbstractWindow):

    def __init__(self, master, dataMaster, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        xOffset, yOffset = JsonHandling.loadOffsetsJson()  # {self.x / xOffset} mm, {self.y / yOffset} mm, prawie ok brakuje wspułrzednych pkt 00

        self.form.addRow(QLabel(f"Old Cross Location: "), QLabel(str(dataMaster.oldCrossLocation)))

        self.form.addRow(QLabel(f"New Cross Location "), QLabel(str(dataMaster.newCrossLocation)))

        self.form.addRow(QLabel(f"Cross Location Delta"), QLabel(dataMaster.delta))

        x = str(int(dataMaster.delta[0]) / xOffset)
        y = str(int(dataMaster.delta[1]) / yOffset)

        self.form.addRow(QLabel(f"Cross Location Delta mm"), QLabel(x + ' ' + y))

        self.form.addRow(QLabel(""), self.okButton)
