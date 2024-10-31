from Python.BackEnd.ROI.Main.NameHandling.NameHandling import NameHandling


class LineNameHandling(NameHandling):

    def GetTextLocation(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        x, y = self.foundCenter()
        return x - 15 - dx, y - 15 - dy

    def setNameFromLen(self):
        self.name = str(self.lineLenMM())
        self.label.updateName(self.name)