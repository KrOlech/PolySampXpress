from MAP.GUI.AbstractMapWindow import AbstractMapWindow
from utilitis.Depracation.DepractionFactory import deprecated


class MapWindowOLD(AbstractMapWindow):

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def conwertManipulatotrCordsToMapOLD(self, manipulatorX, manipulatorY):
        if manipulatorY - self.fild[0]:
            y = int((manipulatorY - self.fild[0]) * self.yOffset / self.scalY)  # -50+17+10-5
            print(f"start {y}")
        else:
            y = 0
        if manipulatorX - self.fild[2]:
            x = int((manipulatorX - self.fild[2]) * self.xOffset / self.scalX)  # +70
        else:
            x = 0

        return x, y

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def addFrameOLD(self, vie, x=25, y=25):
        x, y = self.conwertManipulatotrCordsToMapOLD(x, y)
        try:
            self.map[x:x + int(self.x / self.scalX), y:y + int(self.y / self.scalY)] = self.scalleFream(vie)
            self.cpmwertMap()
        except ValueError as e:
            print(e)

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def conwertManipulatotrCordsToMap(self, manipulatorX, manipulatorY):
        if manipulatorY - self.fild[0]:
            y = int((manipulatorY - self.fild[0] - 1) * self.xOffset)
        else:
            y = 0

        if manipulatorX - self.fild[2]:
            x = int((manipulatorX - self.fild[2] - 1) * self.yOffset)
        else:
            x = 0

        return x, y

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def addFrame(self, vie, x, y):
        x, y = self.conwertManipulatotrCordsToMap(x, y)
        self.addFrameY(vie, x, y)

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def addFrameY(self, vie, x, y):
        y = int(y / self.scalX / 2)  # 53
        # y //=64
        # y *=64
        crop = self.scalleFream(vie)
        crop = crop[:, self.dim[0] - int(self.xOffset / self.scalX / 2):]
        try:
            print("x i y", x, y)
            print(f"y kon{int(self.xOffset / self.scalX / 2)}")
            self.map[x:x + self.dim[1], y + self.dim[0]:y + self.dim[0] + int(self.xOffset / self.scalX / 2)] = crop
            self.cpmwertMap()
        except ValueError as e:
            print(e)

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def addFrameX(self, vie):
        crop = self.scalleFream(vie)
        crop = crop[self.dim[1] - int(self.xOffset / self.scalX / 2):, :]
        try:
            self.map[self.dim[1]:self.dim[1] + int(self.xOffset / self.scalX / 2), :self.dim[0]] = crop
            self.cpmwertMap()
        except ValueError as e:
            print(e)

    @deprecated("Old way do not work correct old wey may be reImplemented in the future")
    def mapCreate(self):

        if self.photoCount[1] == 0 and self.photoCount[0] == 0 and self.mapDirection == "R":
            print("end right")
            self.mapEnd = True
            self.takePhotoBottomRight()
            self.photoCount[0] -= 1
            return True

        elif self.photoCount[1] == 0 and self.photoCount[0] == 0 and self.mapDirection == "L":
            print("end left")
            self.mapEnd = True
            self.takePhotoBottomLeft()
            self.photoCount[0] -= 1
            return True

        elif self.photoCount[1] == 0 and self.mapDirection == "R":
            print("hop y right")
            self.takePhotoRight()
            self.wait(1, self.mapCreate)
            self.photoCount[0] -= 1
            self.mapDirection = 'L'
            self.moveManipulatorToY()

        elif self.photoCount[1] == 0 and self.mapDirection == "L":
            print("hop y left")
            self.takePhotoLeft()
            self.wait(1, self.mapCreate)
            self.photoCount[0] -= 1
            self.mapDirection = 'R'
            self.moveManipulatorToY()

        elif self.photoCount[0] == 0 and self.photoCount[1] == self._photoCount[1] and self.mapDirection == "L":
            print("botom right")
            self.takePhotoBottomRight()
            self.wait(1, self.mapCreate)
            self.photoCount[1] += 1
            self.moveManipulatorToX()

        elif self.photoCount[0] == 0 and self.photoCount[1] == self._photoCount[1] and self.mapDirection == "R":
            print("botom left")
            self.takePhotoBottomLeft()
            self.wait(1, self.mapCreate)
            self.photoCount[1] -= 1
            self.moveManipulatorToX()

        elif self.photoCount[0] == 0:
            print("botom botom")
            self.takePhotoBottom()
            self.wait(1, self.mapCreate)
            self.photoCount[1] -= 1
            self.moveManipulatorToX()

        elif self.mapDirection == 'R':
            print("full right")
            self.takePhotoFull()
            self.wait(1, self.mapCreate)
            self.photoCount[1] -= 1
            self.moveManipulatorToX()

        elif self.mapDirection == 'L':
            print("full left")
            self.takePhotoFull()
            self.wait(1, self.mapCreate)
            self.photoCount[1] += 1
            self.moveManipulatorToX()

        else:
            print("first first")
            self.takePhotoFirst()
            self.mapDirection = "R"
            self.photoCount[1] -= 1
            self.moveManipulatorToX()
            self.wait(1, self.mapCreate)


    def moveManipulatorToX(self):
        print('x', self.photoCount)
        #self.manipulator.goToCords(x=self.fild[0] + self.cmdx * self.photoCount[1])

    def moveManipulatorToY(self):
        print('y', self.photoCount)
        #self.manipulator.goToCords(y=self.fild[2] + self.cmdy * self.photoCount[0])