from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogManipulator


class SetStepSizeDialog(AbstractDialogManipulator):

    @property
    def windowName(self):
        return "Set Step Size"

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.manipulator.speed)

        self.form.addRow('Enter Step Size:', self.valueX)

        self.finaliseOutput()

    def okPressed(self):
        self.manipulator.setSpeed(self.valueX.value())
        super(SetStepSizeDialog, self).okPressed()
