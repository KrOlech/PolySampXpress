from abc import ABCMeta

from src.ROI.Creation.ClickCreate.ClickCreateAbstract import ClickCreateAbstract


class ClikcCreateScatter(ClickCreateAbstract):
    __metaclass__ = ABCMeta

    @property
    def scatter(self):
        return True

    def __savePressLocation(self, e):
        self.savePressLocation(e)

    def __seveReliseLocation(self, e):
        self.seveReliseLocation(e)

    def __saveTemporaryLocation(self, e):
        self.saveTemporaryLocation(e)
