from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QAction


class AbstractManipulatorInterfejs(QWidget):

    @property
    def buttonsNames(self):
        return ["/\\", "<", ">", r'\/']

    def __new__(cls, *args, **kwargs):
        #cls.fun = [cls.__key_down, cls.__key_left, cls.__key_right, cls.__key_up]

    def __init__(self, master, *args, **kwargs):
        super(AbstractManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.fun = [self.__key_down, self.__key_left, self.__key_right, self.__key_up]

        self.master = master

        self.__layout = QGridLayout()

        self.__buttons = [QPushButton(name) for name in self.buttonsNames]

        [self.__layout.addWidget(value, i, j) for j, i, value in zip([2, 3, 3, 4], [3, 2, 4, 3], self.__buttons)]

        self.actions = [QAction("&dw", self), QAction("&lf", self), QAction("&ri", self), QAction("&up", self)]

        [a.triggered.connect(f) for a, f in zip(self.actions, self.fun)]

        [button.released.connect(f) for f, button in zip(self.fun, self.__buttons)]

        self.setLayout(self.__layout)

    def __key_up(self):
        self.master.manipulator.up()

    def __key_left(self):
        self.master.manipulator.left()

    def __key_right(self):
        self.master.manipulator.right()

    def __key_down(self):
        self.master.manipulator.down()

    def center(self, pos):
        self.master.manipulator.center(pos)

    def moveUp(self):
        self.master.manipulator.up()

    def moveRight(self):
        self.master.manipulator.right()

    def moveDown(self):
        self.master.manipulator.down()

    def moveLeft(self):
        self.master.manipulator.left()

    def moveXY(self):
        x, y, speed = self.__getManipulatorParamiters()
        self.master.manipulator.goToCords(x=x + speed, y=y + speed)

    def moveNegativeXY(self):
        x, y, speed = self.__getManipulatorParamiters()
        self.master.manipulator.goToCords(x=x - speed, y=y - speed)

    def __getManipulatorParamiters(self):
        return self.master.manipulator.x, self.master.manipulator.y, self.master.manipulator.speed

    def waitForTarget(self):
        self.master.manipulator.waitForTarget()
