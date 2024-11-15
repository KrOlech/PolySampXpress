from Python.BackEnd.MAP.Abstract.MapParams import MapParams
from Python.BackEnd.MAP.Inicialiser.MapWindowInitialiser import MapWindowInitialise
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class MapFromFile(MapWindowInitialise):
    mapEnd = True

    def __init__(self, master, windowSize, mapId):
        self.master = master
        self.manipulator = master.manipulatorInterferes
        self.windowSize = windowSize
        self.mapId = mapId

    def loadMap(self):
        data, qImg = self.loadMapFile()

        self.mapNumpy = qImg
        self.mapNumpyBorders = qImg
        name = list(data.keys())[0]
        values = data[name]
        self.mapParams = MapParams(values["MapParams"])
        self.name = str(values["MapName"])
        self.fildParams = values["fildParams"]

        self.scale, self.ScaledMapSizeIn_px = self.__mapScalle()

        self.mapWidget = self.createMapLabel()

    def __mapScalle(self):
        sizeIn_mm = [self.fildParams[1] - self.fildParams[0],
                     self.fildParams[3] - self.fildParams[2]]

        sizeIn_px = [(wal * abs(offset)) + cam for wal, offset, cam in
                     zip(sizeIn_mm, self.mapParams.offsets, JsonHandling.loadCameraResolutionJson())]

        self.realSizeIn_mm = [(wal / abs(offset)) for wal, offset in
                              zip(sizeIn_px, self.mapParams.offsets)]

        self.loger(f"work filld size in mm {sizeIn_mm}")
        self.loger(f"real map size in mm {self.realSizeIn_mm}")
        self.loger(f"real map size in px {sizeIn_px}")

        pixelCount = sizeIn_px[0] * sizeIn_px[1]

        mapRes_x, mapRes_y, _ = self.loadResolution("1536P")

        mapPixelCount = mapRes_x * mapRes_y

        scale = pow((pixelCount / mapPixelCount), (1 / 2))

        ScaledMapSizeIn_px = [int(wal / scale) for wal in sizeIn_px]

        self.loger(f"scala: {scale}")
        self.loger(f"scaled map size in px {ScaledMapSizeIn_px}")
        return scale, ScaledMapSizeIn_px
