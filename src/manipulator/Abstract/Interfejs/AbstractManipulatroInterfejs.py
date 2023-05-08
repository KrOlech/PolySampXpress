from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QAction


class AbstractManipulatorInterfejs(QWidget):

    def __init__(self, master, *args, **kwargs):
        super(AbstractManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.master = master

        self._layout = QGridLayout()

        self.buttonsNames = ["/\\", "<", ">", r'\/']

        self.buttons = [QPushButton(name) for name in self.buttonsNames]

        [self._layout.addWidget(value, i, j) for j, i, value in zip([2, 3, 3, 4], [3, 2, 4, 3], self.buttons)]

        self.actions = [QAction("&dw", self), QAction("&lf", self), QAction("&ri", self), QAction("&up", self)]

        self.fun = [self._key_down, self._key_left, self._key_right, self._key_up]

        [a.triggered.connect(f) for a, f in zip(self.actions, self.fun)]

        [button.released.connect(f) for f, button in zip(self.fun, self.buttons)]

        self.setLayout(self._layout)

    def _key_up(self):
        self.master.manipulator.up()

    def _key_left(self):
        self.master.manipulator.left()

    def _key_right(self):
        self.master.manipulator.right()

    def _key_down(self):
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
