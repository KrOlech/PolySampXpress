from src.Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class SetStepSizeDialog(AbstractDialogMaster):

    @property
    def windowName(self):
        return "Set Step Size"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.master.speed)

        self.form.addRow('Enter Step Size:', self.valueX)

        self.finaliseGUI()

    def okPressed(self):
        self.master.setSpeed(self.valueX.value())
        super(SetStepSizeDialog, self).okPressed()
