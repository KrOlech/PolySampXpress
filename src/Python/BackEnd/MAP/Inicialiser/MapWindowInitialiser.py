import threading
from abc import ABCMeta
from asyncio import sleep

import numpy as np
from numpy import ones

from src.Python.BackEnd.MAP.Abstract.AbstractMapWindow import AbstractMapWindow
from src.Python.BackEnd.MAP.Abstract.MapParams import MapParams
from src.Python.BackEnd.MAP.Label.MapLabel import MapLabel
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class MapWindowInitialise(AbstractMapWindow, JsonHandling):
    __metaclass__ = ABCMeta

    # Pointer to Master object
    master = None

    # Pointer to Manipulator Object
    manipulator = None

    # dictionary containing full Manipulator config
    manipulatorFullConfig = None

    # Pointer to Map Params object
    mapParams = None

    cameraFrameSizeX, cameraFrameSizeY = JsonHandling.loadCameraResolutionJson()  # 2560, 1440

    def __init__(self, master, windowSize, manipulatorInterferes):
        self.master = master
        self.manipulator = manipulatorInterferes
        self.windowSize = windowSize

        self.mapParams = self.__mapParams()

        self.movementMap = self.__workFilledMovementMap()

        self.photoCount, self._photoCount = self.__photoCount()

        self.scale, self.ScaledMapSizeIn_px = self.__mapScalle()

        self.__isZoomWaliable()

        self.mapNumpy = self.__mapContainer()
        self.mapNumpyBorders = self.__mapContainer()

        self.scaledCameraFrameSize = self.__calculateScaledCameraFrameSize()
        self.loger(f"scaledCameraFrameSize {self.scaledCameraFrameSize}")

        self.lock = threading.Lock()

        self.mapWidget = self.__createMapLabel()

    async def __gotoMapStart(self):
        if self.manipulator.conn:
            self.manipulator.goToCords(x=self.master.fildParams[0])
            await sleep(60)
            self.manipulator.goToCords(y=self.master.fildParams[2])
            await sleep(60)

    def __calculateScaledCameraFrameSize(self):
        return [int(size // self.scale) for size in JsonHandling.loadCameraResolutionJson()]

    def __createMapLabel(self):
        mapWidget = MapLabel(self)

        mapWidget.resize(self.ScaledMapSizeIn_px[0], self.ScaledMapSizeIn_px[1])

        mapWidget.setAspectRatio(self.ScaledMapSizeIn_px[0] / self.ScaledMapSizeIn_px[1])
        return mapWidget

    def __loadManipulatorFullMovement(self):
        rowData = self.readFile(self.MANIPULATOR_FULL_MOVEMENT_FILEPATH)

        for data in rowData.values():
            if data[self.ZOOM] == self.master.selectedManipulatorZoom:
                break
        else:
            self.logWarning("There is no selected Manipulator")
            return -1

        return data

    def __mapParams(self):
        try:
            return MapParams(self.__loadManipulatorFullMovement())
        except ValueError:
            return MapParams({'zoom': 0, 'offsets': {'x': 1, 'y': 1},
                              'borders': {'x': {'min': 0, 'max': 0}, 'y': {'min': 0, 'max': 0}}})

    def __mapScalle(self):

        sizeIn_mm = [self.master.fildParams[1] - self.master.fildParams[0],
                     self.master.fildParams[3] - self.master.fildParams[2]]

        sizeIn_px = [(wal * offset) + cam for wal, offset, cam in
                     zip(sizeIn_mm, self.mapParams.offsets, JsonHandling.loadCameraResolutionJson())]

        self.realSizeIn_mm = [(wal / offset) for wal, offset in
                              zip(sizeIn_px, self.mapParams.offsets)]

        self.loger(f"work filld size in mm {sizeIn_mm}")
        self.loger(f"real map size in mm {self.realSizeIn_mm}")
        self.loger(f"real map size in px {sizeIn_px}")

        pixelCount = sizeIn_px[0] * sizeIn_px[1]

        mapRes_x, mapRes_y, _ = self.loadResolution("1080P")

        mapPixelCount = mapRes_x * mapRes_y

        scale = pow((pixelCount / mapPixelCount), (1 / 2))

        ScaledMapSizeIn_px = [int(wal / scale) for wal in sizeIn_px]

        self.loger(f"scala: {scale}")
        self.loger(f"scaled map size in px {ScaledMapSizeIn_px}")
        return scale, ScaledMapSizeIn_px

    def __workFilledMovementMap(self):
        # xOffset, yOffset = 900-30, 485-140-25  # loadOffsetsJson()
        xOffset, yOffset = 590, 490 #toDo from file
        xMaxManipulator, yMaxanipulator = self.readManipulatorMax()
        dy = self.cameraFrameSizeX / xOffset
        dx = self.cameraFrameSizeY / yOffset
        self.loger(f"cameraX: {self.cameraFrameSizeX} offsetx: {xOffset}")
        self.loger(f"cameraY: {self.cameraFrameSizeY} offsety: {yOffset}")
        self.loger(f"krok po Y {dx} krok po X {dy}")
        self.loger(f"Fild Params {self.master.fildParams}")

        movementMap = []
        x = self.master.fildParams[0]
        while x < min(self.master.fildParams[1] + dx, xMaxManipulator):
            y = self.master.fildParams[2]
            movementMap.append([])
            while y < min(self.master.fildParams[3] + dy, yMaxanipulator):
                movementMap[-1].append((x, y))
                y += dy
            x += dx

        if movementMap is []:
            movementMap = [[]]

        self.loger("Movement Map:")
        self.loger([row for row in movementMap])
        return movementMap

    def __isZoomWaliable(self):
        x, y = JsonHandling.loadCameraResolutionJson()
        if self.scale < 1:
            self.logWarning("Zoom to low desire map resolution exits row resolution")
        elif self.scale > (x * y * 0.000005):
            self.logWarning("Zoom to high to mach pixels for desire map")

    def __photoCount(self):
        return [0, 0], (len(self.movementMap) - 1, len(self.movementMap[0]) - 1)

    def __mapContainer(self):
        return ones(shape=(*self.ScaledMapSizeIn_px, 3), dtype=np.uint8)
