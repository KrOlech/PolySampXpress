from abc import ABCMeta

from ROI.Main.Abstract.AbstractROI import AbstractROI
from ROI.RenameWindow.RenameWidnow import ReNameWindow


class NameHandling:
    __metaclass__ = ABCMeta
    name = ""

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.__textedit = ReNameWindow(self, text=str(self.name))

    def GetTextLocation(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        return self.x0 - 15 - dx, self.y0 - 15 - dy

    def setName(self, name):
        self.name = name

    def rename(self):
        self.__textedit.show()
