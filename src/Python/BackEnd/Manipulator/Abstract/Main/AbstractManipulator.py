import asyncio
from abc import ABCMeta
from abc import abstractmethod

from Python.ErrorHandling.CustomExceptions.Exceptions import InvalidSpeed
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class AbstractManipulator(JsonHandling):
    __metaclass__ = ABCMeta

    speed = 0
    x, y, z = 0, 0, 0

    x0, y0, z0 = 0, 0, 0

    xOffset = 1
    yOffset = 1

    inMotion = False

    def __init__(self, screenSize, label, *args, **kwargs):
        self.label = label
        self.screenSize = screenSize
        self.x, self.y, self.z = self.getCurrentPosition()

    @property
    @abstractmethod
    def ZoomStepsMap(self):
        return {0: 0.85, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    @abstractmethod
    def getCurrentPosition(self):
        self.abstractmetod()
        return 0, 0, 0

    @abstractmethod
    def validateSpeed(self, speed):
        self.abstractmetod()
        return True

    @abstractmethod
    async def goto(self):
        self.upadteLable()

    @abstractmethod
    def gotoNotAsync(self):
        self.upadteLable()

    @abstractmethod
    def close(self):
        self.abstractmetod()

    @abstractmethod
    def waitForTarget(self):
        self.abstractmetod()

    @abstractmethod
    def homeAxis(self):
        self.abstractmetod()

    @abstractmethod
    def stop(self):
        self.abstractmetod()

    def upadteLable(self):
        self.label.setText(f"Manipulator X:{self.y:.2f} Y:{self.x:.2f}")

    def up(self):
        self.y += self.speed
        self.gotoNotAsync()

    def down(self):
        self.y -= self.speed
        self.gotoNotAsync()

    def left(self):
        self.x -= self.speed
        self.gotoNotAsync()

    def right(self):
        self.x += self.speed
        self.gotoNotAsync()

    def forward(self):
        self.z -= self.speed
        self.gotoNotAsync()

    def backwards(self):
        self.z += self.speed
        self.gotoNotAsync()

    def goToCords(self, x=None, y=None, z=None):
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y
        self.z = z if z is not None else self.z

        self.gotoNotAsync()

    def goToCordsAsync(self, x=None, y=None, z=None):
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y
        self.z = z if z is not None else self.z

        asyncio.run(self.goto())

    def center(self, x, y, zoom):
        self.xOffset, self.yOffset = self.loadOffsetsJson(zoom)

        self.x += (x - 1536 // 2) / self.xOffset #toDo get From Camera not hend put
        self.y += (y - 1000 // 2) / self.yOffset

        self.gotoNotAsync()

    def setSpeed(self, speed):
        if self.validateSpeed(speed):
            self.speed = speed
        else:
            try:
                raise InvalidSpeed()
            except InvalidSpeed:
                self.logWarning(f"{speed} is invalid")
