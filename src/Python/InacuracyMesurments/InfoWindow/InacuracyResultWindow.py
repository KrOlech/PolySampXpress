from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Calibration.DialogWindow.AbstractWindow.AbstractWindow import AbstractWindow


class InacuracyResultWindow(AbstractWindow):

    def __init__(self, master, dataMaster, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel(f"Old Cross Location: "), QLabel(str(dataMaster.oldCrossLocation)))

        self.form.addRow(QLabel(f"New Cross Location "), QLabel(str(dataMaster.newCrossLocation)))

        self.form.addRow(QLabel(f"Cross Location Delta"), QLabel(dataMaster.delta))

        self.form.addRow(QLabel(""), self.okButton)
