from abc import ABCMeta
from functools import cache

from src.ROI.RenameWindow.RenameWidnow import ReNameWindow
from src.utilitis.Logger.Logger import Loger


class NameHandling(Loger):
    __metaclass__ = ABCMeta
    name = ""

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.__textedit = ReNameWindow(self, text=str(self.name))

    @cache
    def GetTextLocation(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        self.loger(f"TextLocation {self.x0 - 15 - dx} i {self.y0 - 15 - dy}")
        return self.x0 - 15 - dx, self.y0 - 15 - dy

    def setName(self, name):
        self.name = name
        self.label.updateName(name)

    def rename(self):
        self.__textedit.show()
