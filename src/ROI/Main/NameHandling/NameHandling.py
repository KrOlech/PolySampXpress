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
    def GetTextLocationMap(self, screenWidth, screenheight, mapWidth, mapHeight, mapX0, mapY0, scale, MapLabel):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]

        x0mm = x0 / self.xOffset
        y0mm = y0 / self.yOffset

        x0mm = int(MapLabel.calculatePixels(x0mm, screenWidth, mapX0, mapX0 + mapWidth))
        y0mm = int(MapLabel.calculatePixels(y0mm, screenheight, mapY0, mapY0 + mapHeight))

        x0mm -= 15
        y0mm -= 15

        self.loger(f"TextLocation {x0mm} i {y0mm}")
        return int(x0mm), int(y0mm)

    def setName(self, name):
        self.name = name
        self.label.updateName(name)

    def rename(self):
        self.__textedit.show()
