from src.MainWindow.InicialisationFlag.AbstractCreateWorkFild import AbstractCreateWorkFild
from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class WindowCreateWorkFeald(AbstractDialogMaster, AbstractCreateWorkFild):

    @property
    def okName(self):
        return "Save and select"

    @property
    def CancelName(self):
        return "Cancel"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.x0 = self.createQSpinBox(0)
        self.x1 = self.createQSpinBox(0)
        self.y0 = self.createQSpinBox(0)
        self.y1 = self.createQSpinBox(0)

        self.form.addRow("x0:", self.x0)
        self.form.addRow("x1:", self.x1)
        self.form.addRow("y0:", self.y0)
        self.form.addRow("y1:", self.y1)

        self.finaliseGUI()

    def okPressed(self):
        field = [self.x0.value(), self.x1.value(), self.y0.value(), self.y1.value(), "new"]

        self.createWorkFild(field)

        super().okPressed()
