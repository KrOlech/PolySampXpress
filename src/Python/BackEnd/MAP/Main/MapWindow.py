import numpy as np

from Python.ErrorHandling.CustomExceptions.Exceptions import NoPlaceToAddFreame
from Python.BackEnd.MAP.Inicialiser.MapWindowInitialiser import MapWindowInitialise
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv

from Python.Utilitis.timer import timeit


class MapWindow(MapWindowInitialise):

    async def mapCreate(self):
        self.missedFrames = 0

        self.moveManipulator()
        self.waitForManipulator()

        i = 0

        maxFrameCount = self._photoCount[0] * self._photoCount[0]

        while not self.mapEnd:
            self.loger(f"{self.photoCount}, {self._photoCount}")
            self.addFrame(self.takePhoto())
            self.calculateNextManipulatorPosition()
            self.moveManipulator()
            self.waitForManipulator()

            i += 1
            self.master.dialogWindowMap.pbar.setValue(int(i / maxFrameCount * 100))

        self.loger(f"During Camera Creating {self.missedFrames} was missed")

        self.master.isMapReadi = True
        self.master.creatingMap = False
        self.isMapReadi = True

    @timeit
    def addFrame(self, frame):

        n = self.photoCount[0] * self.scaledCameraFrameSize[1]
        m = self.photoCount[1] * self.scaledCameraFrameSize[0]

        photoShape = frame.shape
        mozaikPieceShape = self.mapNumpy[n: n + photoShape[0], m:m + photoShape[1]].shape
        self.loger(f"Mozaik Fragment shape {mozaikPieceShape}")
        self.loger(f"photo shape {photoShape}")

        try:
            if all([a == b for a, b in zip(mozaikPieceShape, photoShape)]):
                self.mapNumpy[n: n + photoShape[0], m:m + photoShape[1]] = frame
                #self.mapNumpyBorders[n: n + photoShape[0], m:m + photoShape[1]] = frame

            elif not all(mozaikPieceShape):
                raise NoPlaceToAddFreame()
            else:
                self.addFrame(frame[:mozaikPieceShape[0], :mozaikPieceShape[1]])

            #self.drewLines(n, m, photoShape)

        except NoPlaceToAddFreame as e:
            self.loger(e)
            self.missedFrames += 1

        except ValueError as e:
            self.__errorHandling(e, frame)

    @timeit
    def __errorHandling(self, e, frame):
        eStr = str(e)
        if eStr.find("could not broadcast input array from shape") == 0:
            self.loger("Frame need chopping")
            x, y, z = self.decodeEroreMesage(eStr)
            self.loger(f"Decoded frame size {x}, {y}, {z}")
            self.addFrame(frame[:x, :y])
        else:
            self.loger(e)

    #def drewLines(self, n, m, photoShape): #TODO reimplement if needed
    #    self.mapNumpyBorders[n: n + photoShape[0], m - 1:m, :] = np.ones((photoShape[0], 1, 3), dtype=np.uint8) * 255
    #    self.mapNumpyBorders[n: n + photoShape[0], m + photoShape[1] - 1:m + photoShape[1], :] = np.ones(
    #        (photoShape[0], 1, 3),
    #        dtype=np.uint8) * 255
    #    self.mapNumpyBorders[n - 1:n, m:m + photoShape[1], :] = np.ones((1, photoShape[1], 3), dtype=np.uint8) * 255
    #    self.mapNumpyBorders[n + photoShape[0] - 1:n + photoShape[0], m:m + photoShape[1], :] = np.ones(
    #        (1, photoShape[1], 3),
    #        dtype=np.uint8) * 255

    def decodeEroreMesage(self, mesage):
        cropMesage = mesage[mesage.find("into shape"):]
        cropMesage = cropMesage[cropMesage.find("(") + 1:cropMesage.find(")")]
        x = int(cropMesage[:cropMesage.find(",")])
        cropMesage = cropMesage[cropMesage.find(",") + 1:]
        y = int(cropMesage[:cropMesage.find(",")])
        cropMesage = cropMesage[cropMesage.find(",") + 1:]
        z = int(cropMesage)
        return x, y, z

    def moveManipulator(self):

        self.loger(f"x: {self.movementMap[self.photoCount[0]][self.photoCount[1]][1]}")
        self.loger(f"y: {self.movementMap[self.photoCount[0]][self.photoCount[1]][0]}")
        self.manipulator.goToCords(x=self.movementMap[self.photoCount[0]][self.photoCount[1]][1],
                                   y=self.movementMap[self.photoCount[0]][self.photoCount[1]][0])

    def calculateNextManipulatorPosition(self):
        if self.photoCount[1] == 0 and self.mapDirection == "L":
            if self.photoCount[0] == self._photoCount[0]:
                self.mapEnd = True
            else:
                self.mapDirection = "R"
                self.photoCount[0] += 1
        elif self.photoCount[1] == self._photoCount[1] and self.mapDirection == "R":
            if self.photoCount[0] == self._photoCount[0]:
                self.mapEnd = True
            else:
                self.mapDirection = "L"
                self.photoCount[0] += 1
        elif self.mapDirection == "R":
            self.photoCount[1] += 1
        elif self.mapDirection == "L":
            self.photoCount[1] -= 1

    def waitForManipulator(self):
        self.manipulator.waitForTarget()
