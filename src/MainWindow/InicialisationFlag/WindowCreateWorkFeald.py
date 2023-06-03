from src.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class WindowCreateWorkFeald(AbstractDialogMaster):

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

        self.finaliseOutput()

    def okPressed(self):
        nrWorkFields = len(self.master.workFildActions)

        field = [self.x0.value(), self.x1.value(), self.y0.value(), self.y1.value(), "new"]

        name = f"X:{field[0]}_{field[1]}; Y:{field[2]}_{field[3]}"

        action = self.master.qActionCreate(name, lambda checked, nr=nrWorkFields: self.master.togle(nr), checkable=True)

        self.master.workFildMenu.addAction(action)
        self.master.workFildActions.append(action)
        self.master.readWorkFieldWindow.workFields.append(field)

        self.master.togle(nrWorkFields)

        super().okPressed()
