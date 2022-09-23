from abc import ABCMeta
from abc import abstractmethod
from utilitis.Exceptions import InvalidSpeed
from utilitis.Abstract import abstractmetod


class AbstractManipulator:
    __metaclass__ = ABCMeta

    speed = 0
    x, y, z = 0, 0, 0

    def __init__(self):
        self.setSpeed(10)
        self.x, self.y, self.z = self.getCurentPosytion()

    @abstractmethod
    def getCurentPosytion(self):
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
    def goto(self, x, y, z):
        abstractmetod()

    def up(self):
        self.z += self.speed
        self.goto(self.x, self.y, self.z)

    def down(self):
        self.z -= self.speed
        self.goto(self.x, self.y, self.z)

    def left(self):
        self.y -= self.speed
        self.goto(self.x, self.y, self.z)

    def right(self):
        self.y -= self.speed
        self.goto(self.x, self.y, self.z)

    def forward(self):
        self.x -= self.speed
        self.goto(self.x, self.y, self.z)

    def backwards(self):
        self.x -= self.speed
        self.goto(self.x, self.y, self.z)
