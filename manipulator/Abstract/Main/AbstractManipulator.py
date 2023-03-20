import asyncio
from abc import ABCMeta
from abc import abstractmethod

from utilitis.Abstract import abstractmetod
from utilitis.CustomExceptions.Exceptions import InvalidSpeed
from utilitis.Logger.Logger import Loger


class AbstractManipulator(Loger):
    __metaclass__ = ABCMeta

    speed = 0
    x, y, z = 0, 0, 0

    xOffset = 1
    yOffset = 1

    inMotion = False

    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.x, self.y, self.z = self.getCurrentPosition()

    @abstractmethod
    def getCurrentPosition(self):
        abstractmetod(self)
        return 0, 0, 0

    @abstractmethod
    def validateSpeed(self, speed):
        abstractmetod(self)
        return True

    @abstractmethod
    async def goto(self):
        abstractmetod(self)

    @abstractmethod
    def gotoNotAsync(self):
        abstractmetod(self)

    @abstractmethod
    def close(self):
        abstractmetod(self)

    @abstractmethod
    def waitForTarget(self):
        abstractmetod(self)

    def up(self):
        self.y += self.speed
        asyncio.run(self.goto())

    def down(self):
        self.y -= self.speed
        asyncio.run(self.goto())

    def left(self):
        self.x -= self.speed
        asyncio.run(self.goto())

    def right(self):
        self.x += self.speed
        asyncio.run(self.goto())

    def forward(self):
        self.z -= self.speed
        asyncio.run(self.goto())

    def backwards(self):
        self.z += self.speed
        asyncio.run(self.goto())

    def goToCords(self, x=None, y=None, z=None):
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y
        self.z = z if z is not None else self.z

        self.gotoNotAsync()

    def center(self, x, y):

        self.x += (x - self.screenSize.width() // 2) / self.xOffset
        self.y += (y - self.screenSize.height() // 2) / self.yOffset
        asyncio.run(self.goto())

    def setSpeed(self, speed):
        if self.validateSpeed(speed):
            self.speed = speed
        else:
            try:
                raise InvalidSpeed()
            except InvalidSpeed:
                self.logWarning(f"{speed} is invalid")
