from src.Python.BackEnd.ROI.Creation.ClickCreate.ClickCreateAbstract import ClickCreateAbstract


class ClikcCreateRoi(ClickCreateAbstract):

    @property
    def scatter(self):
        return False

    def __savePressLocation(self, e):
        self.savePressLocation(e)

    def __seveReliseLocation(self, e):
        self.seveReliseLocation(e)

    def __saveTemporaryLocation(self, e):
        self.saveTemporaryLocation(e)
