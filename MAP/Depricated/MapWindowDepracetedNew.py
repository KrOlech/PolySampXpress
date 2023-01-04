import threading
from time import sleep

from MAP.Inicialiser.MapWindowInitialiser import MapWindowInitialise
from manipulator.TCIP.TCIPManipulator import TCIPManipulator
from utilitis.Depracation.DepractionFactory import deprecated


@deprecated("OLD Implementation")
class __MapWindow(MapWindowInitialise):

    def __init__(self, master, windowSize, manipulator: TCIPManipulator, *args, **kwargs):
        super(MapWindowInitialise, self).__init__(master, windowSize, manipulator, *args, **kwargs)
        self.lock = threading.Lock()
        self._addFrameZero(self.scalleFream(master.camera.getFrame()))

    def createMap(self):
        self.manipulator.goToCords(x=25 + (self.cameraFrameSizeX / self.xOffset))
        sleep(0.01)
        self.wait(30)

    def takPhoto(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        self.map[:self.scaledCameraFrameSize[1], self.scaledCameraFrameSize[0]:] = crop[:, :self.map.shape[1] - self.scaledCameraFrameSize[0]]
        self.cpmwertMap()

    def takePhotoFull(self):
        # print(f"full {self.photoCount}")
        crop = self.scalleFream(self.master.camera.getFrame())
        try:
            self.map[int(self.scaledCameraFrameSize[1] * self.photoCount[0]):int(self.scaledCameraFrameSize[1] * (self.photoCount[0] + 1)),
            int(self.scaledCameraFrameSize[0] * self.photoCount[1]):int(self.scaledCameraFrameSize[0] * (self.photoCount[1] + 1))] = crop
            self.cpmwertMap()
        except ValueError as e:
            print(e)

    def takePhotoRight(self):
        # print(f"right {self.photoCount}")
        mapShape = self.map[:, int(self.scaledCameraFrameSize[0] * self.photoCount[1]):].shape
        crop = self.scalleFream(self.master.camera.getFrame())
        try:
            self.map[int(self.scaledCameraFrameSize[1] * self.photoCount[0]):int(self.scaledCameraFrameSize[1] * (self.photoCount[0] + 1)),
            int(self.scaledCameraFrameSize[0] * self.photoCount[1]):] = crop[:, :mapShape[1]]
            self.cpmwertMap()
        except ValueError as e:
            print(e)

    def takePhotoLeft(self):

        crop = self.scalleFream(self.master.camera.getFrame())
        try:
            self.map[int(self.scaledCameraFrameSize[1] * self.photoCount[0]):int(self.scaledCameraFrameSize[1] * (self.photoCount[0] + 1)),
            :int(self.scaledCameraFrameSize[0])] = crop
            self.cpmwertMap()
        except ValueError as e:
            print(e)

        print(
            f"map shape: {self.map[int(self.scaledCameraFrameSize[1] * self.photoCount[0]):int(self.scaledCameraFrameSize[1] * (self.photoCount[0] + 1)), :int(self.scaledCameraFrameSize[0] * self.photoCount[1])].shape}")
        print(f'crop shape: {crop.shape}')
        print(f"left {self.photoCount}")

    def takePhotoBottom(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("bottom")

    def takePhotoBottomRight(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("botomRight")

    def takePhotoBottomLeft(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("botomLeft")

    def moveManipulator(self):
        print(self.manipulator.x, self.manipulator.y)
        print(self.movementMap[self.photoCount[0]][self.photoCount[1]])
        if self.movementMap[self.photoCount[0]][self.photoCount[1]][0] != self.manipulator.x:
            print(f"x = {self.movementMap[self.photoCount[0]][self.photoCount[1]][0]}")
            self.manipulator.x = self.movementMap[self.photoCount[0]][self.photoCount[1]][0]
        elif self.movementMap[self.photoCount[0]][self.photoCount[1]][1] != self.manipulator.y:
            print(f"y = {self.movementMap[self.photoCount[0]][self.photoCount[1]][1]}")
            self.manipulator.y = self.movementMap[self.photoCount[0]][self.photoCount[1]][1]

        # self.manipulator.goToCords(cameraFreamSizeX=self.fild[0] + self.scaledCameraFrameSizeX * self.photoCount[1])

    def mapCreate(self):
        print(self.photoCount, self.mapDirection, self.mapEnd)

        if self.mapEnd:
            return True
        elif self.mapDirection == "R":
            self.rightMovement()
        elif self.mapDirection == "L":
            self.leftMovement()
        else:
            self.firstPhoto()

        self.moveManipulator()
        self.wait(fun=self.mapCreate)

    def calculateNextPhotoTypeAndMakePhoto(self):
        __funTab = self.__isBottom()

        if self.photoCount[1] == self._photoCount[1]:
            __funTab[0]()
        elif self.photoCount[1] == 0:
            __funTab[2]()
        else:
            __funTab[1]()

    def rightMovement(self):
        print(self.photoCount, self._photoCount)
        if self.photoCount == list(self._photoCount):
            return self.rightEnd()

        if self.photoCount[1] == 0 and self.photoCount[0] == self._photoCount[0]:
            self.leftBottom()
        elif self.photoCount[1] == self._photoCount[1]:
            self.rightHopY()
        elif self.photoCount[1] == 0:
            self.leftEdge()
        elif self.photoCount[0] == self._photoCount[0]:
            self.rightBottom()
        else:
            self.rightFull()

    def leftMovement(self):
        print(self.photoCount, self._photoCount)
        if self.photoCount[1] == 0 and self.photoCount[0] == self._photoCount[0]:
            return self.leftEnd()

        if self.photoCount[1] == self._photoCount[1] and self.photoCount[0] == self._photoCount[0]:
            self.rightBottom()
        elif self.photoCount[1] == 0:
            self.leftHopY()
        elif self.photoCount[1] == self._photoCount[1]:
            self.rightEdge()
        elif self.photoCount[0] == self._photoCount[0]:
            self.leftBottom()
        else:
            self.leftFull()

    def rightHopY(self):
        self.takePhotoRight()
        self.photoCount[0] += 1
        self.mapDirection = 'L'

    def leftHopY(self):
        self.takePhotoLeft()
        self.photoCount[0] += 1
        self.mapDirection = 'R'

    def leftBottom(self):
        self.takePhotoBottomLeft()
        self.photoCount[1] += 1

    def rightBottom(self):
        self.takePhotoBottomRight()
        self.photoCount[1] += 1

    def leftEdge(self):
        self.takePhotoLeft()
        self.photoCount[1] += 1

    def rightEdge(self):
        self.takePhotoRight()
        self.photoCount[1] -= 1

    def rightFull(self):
        self.takePhotoFull()
        self.photoCount[1] += 1

    def leftFull(self):
        self.takePhotoFull()
        self.photoCount[1] -= 1

    def rightEnd(self):
        self.mapEnd = True
        self.takePhotoBottomRight()

    def leftEnd(self):
        self.mapEnd = True
        self.takePhotoBottomLeft()

    def firstPhoto(self):
        self.mapDirection = "R"
