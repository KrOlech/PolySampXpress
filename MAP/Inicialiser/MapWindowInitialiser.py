import threading
from abc import ABCMeta
from itertools import chain

import numpy as np

from MAP.Abstract.AbstractMapWindow import AbstractMapWindow
from MAP.Abstract.MapParams import MapParams
from MAP.Label.MapLabel import MapLabel

from utilitis.JsonRead.JsonRead import JsonHandling, loadCameraResolutionJson, loadResolution

from numpy import arange, ones


class MapWindowInitialise(AbstractMapWindow, JsonHandling):
    __metaclass__ = ABCMeta

    # Pointer to Master object
    master = None

    # Pointer to manipulator Object
    manipulator = None

    # dictionary containing full manipulator config
    manipulatorFullConfig = None

    # Pointer to Map Params object
    mapParams = None

    cameraFrameSizeX, cameraFrameSizeY = loadCameraResolutionJson()  # 2560, 1440

    def __init__(self, master, windowSize, manipulator):
        self.master = master
        self.manipulator = manipulator

        self.mapWidget = self.__createMapLabel(windowSize)

        self.mapParams = self.__mapParams()

        self.movementMap = self.__workFilledMovementMap()

        self.photoCount, self._photoCount = self.__photoCount()

        self.scale, self.ScaledMapSizeIn_px = self.__mapScalle()

        self.__isZoomWaliable()

        self.mapNumpy = self.__mapContainer()

        self.scaledCameraFrameSize = self.__calculateScaledCameraFrameSize()
        print(f"scaledCameraFrameSize {self.scaledCameraFrameSize}")

        self.lock = threading.Lock()

    def __calculateScaledCameraFrameSize(self):
        return [int(size // self.scale) for size in loadCameraResolutionJson()[::-1]]

    def __createMapLabel(self, windowSize):
        mapWidget = MapLabel(self)
        mapWidget.setMinimumSize(1284, 857)
        mapWidget.setMaximumSize(windowSize)
        # mapWidget.setFixedSize(windowSize)
        return mapWidget

    def __loadManipulatorFullMovement(self):
        rowData = self.readFile(self.MANIPULATOR_FULL_MOVEMENT_FILEPATH)

        for data in rowData.values():
            if data[self.ZOOM] == self.master.selectedManipulatorZoom:
                break
        else:
            print("[Warning] - There is no selected manipulator")
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
                     zip(sizeIn_mm, self.mapParams.offsets, loadCameraResolutionJson())]

        realSizeIn_mm = [(wal / offset) for wal, offset in
                         zip(sizeIn_px, self.mapParams.offsets)]

        self.loger(f"work filld size in mm {sizeIn_mm}")
        self.loger(f"real map size in mm {realSizeIn_mm}")
        self.loger(f"real map size in px {sizeIn_px}")

        pixelCount = sizeIn_px[0] * sizeIn_px[1]

        mapRes_x, mapRes_y, _ = loadResolution("1440P")

        mapPixelCount = mapRes_x * mapRes_y

        scale = pixelCount / mapPixelCount

        ScaledMapSizeIn_px = [int(wal / scale) for wal in sizeIn_px]

        self.loger(f"scala: {scale}")
        self.loger(f"scaled map size in px {ScaledMapSizeIn_px}")
        return scale, ScaledMapSizeIn_px

    def __workFilledMovementMap(self):
        dx = self.cameraFrameSizeX / self.mapParams.xOffset
        dy = self.cameraFrameSizeY / self.mapParams.yOffset
        self.loger(f"krok po X {dx} krok po y {dy}")

        movmentMap = []
        x = self.master.fildParams[0]
        while x < self.master.fildParams[1]+dx:
            y = self.master.fildParams[2]
            movmentMap.append([])
            while y < self.master.fildParams[3]+dy:
                movmentMap[-1].append((x, y))
                y += dy
            x += dx

        [print(row) for row in movmentMap]

        return movmentMap

    def __isZoomWaliable(self):
        x, y = loadCameraResolutionJson()
        if self.scale < 1:
            print("[Warning] Zoom to low desire map resolution exits row resolution")
        elif self.scale > (x * y * 0.000005):
            print("[Warning] Zoom to high to mach pixels for desire map")

    def __photoCount(self):
        return [0, 0], (len(self.movementMap) - 1, len(self.movementMap[0]) - 1)

    def __mapContainer(self):
        return ones(shape=(*self.ScaledMapSizeIn_px, 3), dtype=np.uint8)
