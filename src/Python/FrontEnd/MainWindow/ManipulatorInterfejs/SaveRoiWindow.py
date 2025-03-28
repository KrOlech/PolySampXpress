from Python.Utilitis.GenericProgressClass import GenericProgressClass


class SaveRoiWindow(GenericProgressClass):

    def end(self):
        self.accept()
        self.master.clearRoiList()
