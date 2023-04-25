from src.manipulator.DialogWindow.Abstract import AbstractDialog


class GoToCordsDialog(AbstractDialog):

    @property
    def windowName(self):
        return "Go To Cords"

    def __init__(self, manipulator, *args, **kwargs):
        super().__init__(manipulator, *args, **kwargs)

        self.valueX = self.createQSpinBox(self.manipulator.x)
        self.valueY = self.createQSpinBox(self.manipulator.y)

        self.form.addRow('X:', self.valueX)
        self.form.addRow('Y:', self.valueY)

        self.finaliseOutput()

    def okPressed(self):
        self.manipulator.goToCords(x=self.valueX.value(), y=self.valueY.value())
        super(GoToCordsDialog, self).okPressed()
