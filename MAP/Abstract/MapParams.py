from utilitis.JsonRead.JsonRead import JsonHandling


class MapParams(JsonHandling):
    __zoom = 0

    __xOffset = 0

    __yOffset = 0

    __offsets = []

    __x = []

    __y = []

    def __new__(cls, manipulatorFullConfig, *args, **kwargs):
        if manipulatorFullConfig == -1:
            raise ValueError

        return super(MapParams, cls).__new__(cls, *args, **kwargs)

    def __init__(self, manipulatorFullConfig):

        type(self).__zoom = manipulatorFullConfig["zoom"]

        offsets = manipulatorFullConfig["offsets"]

        type(self).__xOffset = offsets["x"]

        type(self).__yOffset = offsets["y"]

        borders = manipulatorFullConfig["borders"]

        type(self).__x = [borders['x']["min"], borders['x']["max"]]

        type(self).__y = [borders['y']["min"], borders['y']["max"]]

        type(self).__offsets = [type(self).__xOffset, type(self).__yOffset]

    @property
    def xMax(self) -> int:
        return type(self).__x[1]

    @property
    def xMin(self) -> int:
        return type(self).__x[0]

    @property
    def yMax(self) -> int:
        return type(self).__y[1]

    @property
    def yMin(self) -> int:
        return type(self).__y[0]

    @property
    def xOffset(self) -> int:
        return type(self).__xOffset

    @property
    def yOffset(self) -> int:
        return type(self).__yOffset

    @property
    def zoom(self) -> int:
        return type(self).__zoom

    @property
    def offsets(self) -> list:
        return type(self).__offsets
