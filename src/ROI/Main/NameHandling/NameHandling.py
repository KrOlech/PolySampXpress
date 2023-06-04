from abc import ABCMeta
from functools import cache

from src.ROI.RenameWindow.RenameWidnow import ReNameWindow
from src.BaseClass.Logger.Logger import Loger


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

    @cache
    def GetTextLocationMap(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]

        x0mm = x0 / self.xOffset
        y0mm = y0 / self.yOffset

        x0mm -= mapX0
        y0mm -= mapY0

        x0mm /= mapWidth
        y0mm /= mapHeight

        x0mm *= screenheight
        y0mm *= screenWidth

        x0mm /= scale
        y0mm /= scale

        x0mm = int(x0mm)
        y0mm = int(y0mm)

        x0mm -= 15
        y0mm -= 15

        self.loger(f"TextLocation {x0mm} i {y0mm}")
        return int(x0mm), int(y0mm)

    def setName(self, name):
        self.name = name
        self.label.updateName(name)

    def rename(self):
        self.__textedit.show()
