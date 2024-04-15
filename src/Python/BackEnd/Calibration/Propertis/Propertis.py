from Python.BackEnd.Calibration.Propertis.PatternDialog import PatternDialog


class CalibrateProperty:
    __dataColected = False
    __x = 0
    __y = 0
    __s = 0

    @property
    def indexLegend(self):
        return {0: "x", 1: "y"}

    @property
    def configFile(self):
        return "ManipulatorFullConfig.json"

    @property
    def templateLocationX(self):
        if not self.__dataColected:
            self.resolvetemplate()
        while not self.__dataColected:
            ...
        return self.__x

    @property
    def templateLocationY(self):
        if not self.__dataColected:
            self.resolvetemplate()
        while not self.__dataColected:
            ...
        return self.__y

    @property
    def templateSize(self):
        if not self.__dataColected:
            self.resolvetemplate()
        while not self.__dataColected:
            ...
        return self.__s

    def resolvetemplate(self):
        PatternDialog(self).exec_()

    def dataPrivaided(self, x, x1, y, y1):
        self._s = max(x - x1, y - y1)
        self.__x = min(x, x1)
        self.__y = min(y, y1)
