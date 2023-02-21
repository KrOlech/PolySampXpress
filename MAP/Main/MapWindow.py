import inspect
from asyncio import sleep

from MAP.Inicialiser.MapWindowInitialiser import MapWindowInitialise


class MapWindow(MapWindowInitialise):

    async def mapCreate(self):
        while not self.mapEnd:
            self.loger(f"{self.photoCount}, {self._photoCount}")
            self.addFrame(self.takePhoto())
            self.calculateNextManipulatorPosition()
            self.moveManipulator()
            await sleep(30)



    def addFrame(self, frame):

        n = self.photoCount[0] * self.scaledCameraFrameSize[1]
        m = self.photoCount[1] * self.scaledCameraFrameSize[0]

        photoShape = frame.shape
        self.loger(f"map Fragment shape {self.mapNumpy[n: n + photoShape[0], m:m + photoShape[1]].shape}")
        self.loger(f"photo shape {photoShape}")

        try:
            self.mapNumpy[n: n + photoShape[0], m:m + photoShape[1]] = frame

        except Exception as e:
            eStr = str(e)
            if eStr.find("could not broadcast input array from shape") == 0:
                self.loger("Frame need chopping")
                x, y, z = self.decodeEroreMesage(eStr)
                self.loger(f"{x}, {y}, {z}")
                self.addFrame(frame[:x, :y])
            else:
                self.loger(e)

        self.convertMap()

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
        if self.manipulator.x != self.movementMap[self.photoCount[0]][self.photoCount[1]][1]:
            self.loger(f"x: {self.movementMap[self.photoCount[0]][self.photoCount[1]][1]}")
            self.manipulator.goToCords(x=self.movementMap[self.photoCount[0]][self.photoCount[1]][1])
        elif self.manipulator.y != self.movementMap[self.photoCount[0]][self.photoCount[1]][0]:
            self.loger(f"y: {self.movementMap[self.photoCount[0]][self.photoCount[1]][0]}")
            self.manipulator.goToCords(y=self.movementMap[self.photoCount[0]][self.photoCount[1]][0])

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