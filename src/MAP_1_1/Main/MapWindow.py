import threading

from tests import MapWindowInitialise
from tests import TCIPManipulator  # depraceted support Drop


class MapWindow(MapWindowInitialise):
    firstPhotoNotTaken = True  # ToDO move to Abstract
    hopY = False

    def __init__(self, master, windowSize, manipulator: TCIPManipulator, *args, **kwargs):
        super(MapWindow, self).__init__(master, windowSize, manipulator, *args, **kwargs)
        self.lock = threading.Lock()

    def takPhoto(self):
        crop = self.scalleFream(self.master.camera.getFrame())
        self.map[:self.scaledCameraFrameSize[1], self.scaledCameraFrameSize[0]:] = crop[:, :self.map.shape[1] -
                                                                                            self.scaledCameraFrameSize[
                                                                                                0]]
        self.convertMap()

    def moveManipulator(self):
        if self.manipulator.x != self.movementMap[self.photoCount[0]][self.photoCount[1]][0]:
            self.manipulator.__goToCords()
        elif self.manipulator.y != self.movementMap[self.photoCount[0]][self.photoCount[1]][1]:
            self.manipulator.__goToCords()

    def mapCreate(self):
        # print(self.photoCount, self._photoCount, self.mapDirection, self.mapEnd)

        if self.mapEnd:
            return True

        if self.firstPhotoNotTaken:
            self.firstPhotoNotTaken = False
            self.firstPhoto()
        else:
            self.__calculateNextPhotoTypeAndMakePhoto()

        self.calculateNextManipulatorPosition()

        self.moveManipulator()
        self.wait(fun=self.mapCreate)

    def firstPhoto(self):
        self._addFrameZero(self.scalleFream(self.master.camera.getFrame()))

    def __calculateNextPhotoTypeAndMakePhoto(self):
        __funTab = self.__isBottom()

        if self.photoCount[1] == self._photoCount[1]:
            __funTab[0]()
        elif self.photoCount[1] == 0:
            __funTab[2]()
        else:
            __funTab[1]()

    def __isBottom(self):
        if self.photoCount[0] == self._photoCount[0]:  # bottom
            return self.rightBottom, self.bottom, self.leftBottom
        else:  # top
            return self.right, self.takePhotoFull, self.left

    def rightBottom(self):
        crop = self.__takPhoto()

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][2]:
            crop = self.chopLeft(crop)

        crop = self.chopRight(crop)

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][3]:
            crop = self.chopTop(crop)

        crop = self.chopBottom(crop)

        self.insertPhotoIntoMap(crop)

    def bottom(self):
        crop = self.__takPhoto()

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][3]:
            crop = self.chopTop(crop)

        crop = self.chopBottom(crop)

        self.insertPhotoIntoMap(crop)

    def leftBottom(self):
        crop = self.__takPhoto()

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][2]:
            crop = self.chopRight(crop)

        crop = self.chopLeft(crop)

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][3]:
            crop = self.chopTop(crop)

        crop = self.chopBottom(crop)

        self.insertPhotoIntoMap(crop)

    def right(self):
        crop = self.__takPhoto()

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][2]:
            crop = self.chopLeft(crop)

        crop = self.chopRight(crop)

        self.insertPhotoIntoMap(crop)

    def takePhotoFull(self):  # toDo oczyscic wklejanie bo jest bardzo nie czytelne
        # print(f"full {self.photoCount}")
        crop = self.__takPhoto()
        try:
            self.map[int(self.scaledCameraFrameSize[1] * self.photoCount[0]):int(
                self.scaledCameraFrameSize[1] * (self.photoCount[0] + 1)),
            int(self.scaledCameraFrameSize[0] * self.photoCount[1]):int(
                self.scaledCameraFrameSize[0] * (self.photoCount[1] + 1))] = crop
            self.convertMap()
        except ValueError as e:
            print(e)

    def left(self):
        crop = self.__takPhoto()

        if not self.movementMap[self.photoCount[0]][self.photoCount[1]][2]:
            crop = self.chopRight(crop)

        crop = self.chopLeft(crop)

        self.insertPhotoIntoMap(crop)

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

    def __takPhoto(self):
        return self.scalleFream(self.master.camera.getFrame())

    def chopTop(self, photo):
        y = self.movementMap[self.photoCount[0]][self.photoCount[1]][1]
        yr = self.movementMap[self.photoCount[0]][self.photoCount[1]][5]
        n = int((yr - y) * self.yOffset)

        print(f"top:, y: {y}, yr: {yr},  n: {n}")
        return photo[n:, :]

    def chopBottom(self, photo):
        m = int((self._photoCount[0] * self.scaledCameraFrameSize[1]) - self.scaledMapSizeXInPx)

        print(f"bottom m: {m}")
        return photo[: m, :]

    def chopRight(self, photo):
        m = int((self.photoCount[1] * self.scaledCameraFrameSize[0]) - self.scaledMapSizeYInPx)
        x = self.movementMap[self.photoCount[0]][self.photoCount[1]][0]
        xr = self.movementMap[self.photoCount[0]][self.photoCount[1]][4]
        n = int((xr - x) * self.xOffset)

        print(f"right:, x: {x}, xr: {xr}, m: {m}, n: {n} v: {m - n}")
        return photo[:, :-(m - n)]

    def chopLeft(self, photo):
        # m = int((self.photoCount[1] * self.scaledCameraFrameSize[0]) - self.maxX)
        x = self.movementMap[self.photoCount[0]][self.photoCount[1]][0]
        xr = self.movementMap[self.photoCount[0]][self.photoCount[1]][4]
        n = int((xr - x) * self.xOffset)

        m = int((self.photoCount[1] * self.scaledCameraFrameSize[0]) - self.scaledMapSizeYInPx)

        print(f"left x: {x}, xr: {xr}, m: {m}, n: {n} v: {n}")
        return photo[:, n:]

    def insertPhotoIntoMap(self, photo):
        try:
            n = self.photoCount[0] * self.scaledCameraFrameSize[1]
            m = self.photoCount[1] * self.scaledCameraFrameSize[0]
            photoShape = photo.shape
            print(f"map Fragmetn shape {self.map[n: n + photoShape[0], m:m + photoShape[1]].shape}")
            print(f"photo shape {photo.shape}")
            self.map[n: n + photoShape[0], m:m + photoShape[1]] = photo
            self.convertMap()
        except Exception as e:
            print(e)
