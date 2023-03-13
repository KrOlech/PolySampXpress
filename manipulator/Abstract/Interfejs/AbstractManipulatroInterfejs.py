from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QAction


class AbstractManipulatorInterfejs(QWidget):

    def __init__(self, ManipulatorObject, *args, **kwargs):
        super(AbstractManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.Manipulator = ManipulatorObject

        self._layout = QGridLayout()

        self.buttonsNames = ['/\\', "<", ">", '\/']

        self.buttons = [QPushButton(name) for name in self.buttonsNames]

        [self._layout.addWidget(value, i, j) for j, i, value in zip([2, 3, 3, 4], [3, 2, 4, 3], self.buttons)]

        self.actions = [QAction("&dw", self), QAction("&lf", self), QAction("&ri", self), QAction("&up", self)]

        self.fun = [self._key_down, self._key_left, self._key_right, self._key_up]

        [a.triggered.connect(f) for a, f in zip(self.actions, self.fun)]

        [button.released.connect(f) for f, button in zip(self.fun, self.buttons)]

        self.setLayout(self._layout)

    def _key_up(self):
        self.Manipulator.up()

    def _key_left(self):
        self.Manipulator.left()

    def _key_right(self):
        self.Manipulator.right()

    def _key_down(self):
        self.Manipulator.down()

    def center(self, pos):
        self.Manipulator.center(pos)

    def moveUp(self):
        self.Manipulator.up()

    def moveLeft(self):
        self.Manipulator.left()

    def waitForTarget(self):
        self.Manipulator.waitForTarget()