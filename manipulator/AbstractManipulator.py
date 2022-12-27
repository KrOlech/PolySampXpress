from abc import ABCMeta
from abc import abstractmethod
from utilitis.Exceptions import InvalidSpeed
from utilitis.Abstract import abstractmetod
from utilitis.JsonRead.JsonRead import loadOffsetsJson


class AbstractManipulator:
    __metaclass__ = ABCMeta

    speed = 0
    x, y, z = 25.0, 25.0, 25.0

    xOffset = 1
    yOffset = 1

    inMotion = False

    def __init__(self):

        self.xOffset, self.yOffset = loadOffsetsJson()
        self.setSpeed(1)
        self.x, self.y, self.z = self.getCurrentPosition()

    @abstractmethod
    def getCurrentPosition(self):
        abstractmetod()
        return 0, 0, 0

    @abstractmethod
    def center(self, pozycja):
        abstractmetod()

    @abstractmethod
    def validateSpeed(self, speed):
        abstractmetod()
        return True

    def setSpeed(self, speed):
        if self.validateSpeed(speed):
            self.speed = speed
        else:
            try:
                raise InvalidSpeed()
            except InvalidSpeed as e:
                print(f"{e}")
                print(f"{speed} is invalid")

    @abstractmethod
    def goto(self):
        abstractmetod()

    def up(self):
        self.y += self.speed
        self.goto()

    def down(self):
        self.y -= self.speed
        self.goto()

    def left(self):
        self.x -= self.speed
        self.goto()

    def right(self):
        self.x += self.speed
        self.goto()

    def forward(self):
        self.z -= self.speed
        self.goto()

    def backwards(self):
        self.z += self.speed
        self.goto()

    def goToCords(self, x=None, y=None, z=None):

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

        self.goto()

    def center(self, x, y):

        x1 = x - 1280
        y1 = y - 720

        x = x1 / self.xOffset
        y = y1 / self.yOffset

        self.x += x
        self.y += y
        self.goto()

    @abstractmethod
    def close(self):
        abstractmetod()
