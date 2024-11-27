from Python.Utilitis.GenericProgressClass import GenericProgressClass


class XeroProgresWindow(GenericProgressClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.addRow(self.cancelButton)


    def cancelPressed(self):
        self.loger("Mozaik Creation Stopped")
        self.master.manipulatorInterferes.stop()
        self.master.zta.stopXeroOut()
