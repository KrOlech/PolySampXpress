from time import sleep

from MAP.GUI.MapWindowInitialiser import MapWindowInitialise
from manipulator.TCIPManipulator import TCIPManipulator


class MapWindow(MapWindowInitialise):

    def __init__(self, master, windowSize, manipulator: TCIPManipulator, *args, **kwargs):
        super(MapWindow, self).__init__(master, windowSize, manipulator, *args, **kwargs)
        self._addFrameZero(self.scalleFream(master.camera.getFrame()))

    def createMap(self):
        self.manipulator.goToCords(x=25 + (self.x / self.xOffset))
        sleep(0.01)
        self.wait(30)

    def takphoto(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        self.map[:self.dim[1], self.dim[0]:] = crop[:, :self.map.shape[1] - self.dim[0]]
        self.cpmwertMap()

    def takePhotoFirst(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("first")

    def takePhotoFull(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("Full")

    def takePhotoRight(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("right")

    def takePhotoLeft(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        # print("left")

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
        #print(self.photoCount)
        pass
        # self.manipulator.goToCords(x=self.fild[0] + self.cmdx * self.photoCount[1])

    def mapCreate(self):
        print(self.photoCount, self.mapDirection)
        if self.mapDirection == "R":
            self.rightMovement()
        elif self.mapDirection == "L":
            self.leftMovement()
        elif self.mapEnd:
            return True
        else:
            self.firstPhoto()

        self.moveManipulator()
        self.wait(1, self.mapCreate)

    def rightMovement(self):
        if self.photoCount == self._photoCount:
            return self.rightEnd()

        if self.photoCount[1] == 0 and self.photoCount[0] == self._photoCount[0]:
            self.leftBottom()
        elif self.photoCount[1] == self._photoCount[1]:
            self.rightHopY()
        elif self.photoCount[1] == 0:
            self.leftEdge()
        else:
            self.rightFull()

    def leftMovement(self):
        if self.photoCount[1] == 0 and self.photoCount[0] == self._photoCount[0]:
            return self.leftEnd()

        if self.photoCount[1] == self._photoCount[1] and self.photoCount[0] == self._photoCount[0]:
            self.rightBottom()
        elif self.photoCount[1] == 0:
            self.leftHopY()
        elif self.photoCount[1] == self._photoCount[1]:
            self.rightEdge()
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
        self.photoCount[1] -= 1

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
        self.takePhotoFirst()
        self.mapDirection = "R"
        self.photoCount[1] += 1
