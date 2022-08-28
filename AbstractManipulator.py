from abc import ABCMeta
from abc import abstractmethod
from Exceptions import InvalidSpeed


class AbstractManipulator:
    __metaclass__ = ABCMeta

    speed = 0
    x, y, z = 0, 0, 0

    def __init__(self):
        self.setSpeed(10)
        self.x, self.y, self.z = self.getCurentPosytion()

    @abstractmethod
    def getCurentPosytion(self):
        print("Abstract Methode")

    @abstractmethod
    def center(self, pozycja):
        print("Abstract Methode")

    @abstractmethod
    def validateSpeed(self, speed):
        print("Abstract Methode")

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
        print("Abstract Methode")

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
