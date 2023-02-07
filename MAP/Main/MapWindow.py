from MAP.Inicialiser.MapWindowInitialiser import MapWindowInitialise


class MapWindow(MapWindowInitialise):

    def mapCreate(self):
        while not self.mapEnd:
            print(self.photoCount, self._photoCount)
            self.takePhoto()
            self.addFrame()
            self.calculateNextManipulatorPosition()
            self.moveManipulator()


    def addFrame(self, param, y, x):
        pass

    def moveManipulator(self):
        if self.manipulator.x != self.movementMap[self.photoCount[0]][self.photoCount[1]][0]:
            print(f"x: { self.movementMap[self.photoCount[0]][self.photoCount[1]][0]}")
            self.manipulator.goToCords(x=self.movementMap[self.photoCount[0]][self.photoCount[1]][0])
        elif self.manipulator.y != self.movementMap[self.photoCount[0]][self.photoCount[1]][1]:
            print(f"y: { self.movementMap[self.photoCount[0]][self.photoCount[1]][1]}")
            self.manipulator.goToCords(y=self.movementMap[self.photoCount[0]][self.photoCount[1]][1])


    def chopTop(self):
        pass

    def chopLeft(self):
        pass

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