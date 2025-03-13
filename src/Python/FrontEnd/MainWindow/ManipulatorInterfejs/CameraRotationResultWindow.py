from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class CameraRotationResultWindow(AbstractDialogMaster):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.form.addRow(QLabel("Difference in x: "), QLabel(f"{self.master.dXmm:.4f} mm"))
        self.form.addRow(QLabel("Difference in y: "), QLabel(f"{self.master.dYmm:.4f} mm"))

        self.finaliseGUISingleButton()
