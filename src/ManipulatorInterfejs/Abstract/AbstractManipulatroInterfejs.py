from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QAction
from PyQt5.QtCore import Qt

from src.BaseClass.Logger.Logger import Loger
from src.ManipulatorInterfejs.ManipulatorSlider.ManipulatorSlider import ManipulatorSlider


class AbstractManipulatorInterferes(QWidget, Loger):
    _focusManipulator = None
    _manipulator = None

    @property
    def buttonsNames(self):
        return ["/\\", "<", ">", r'\/']

    @property
    def x(self):
        return self._manipulator.x

    @property
    def y(self):
        return self._manipulator.y

    @property
    def x0(self):  # toDO powino to byc zawsze 0 obecnie z uwagi na blad z kalibracja
        return self._manipulator.x0

    @property
    def y0(self):  # toDO powino to byc zawsze 0 obecnie z uwagi na blad z kalibracja
        return self._manipulator.y0

    def conn(self):  # toDO old implementation need redo propably not useed
        return self._manipulator.conn

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(AbstractManipulatorInterferes, self).__init__(*args, **kwargs)

        self.fun = [self.__key_down, self.__key_left, self.__key_right, self.__key_up]

        self.windowSize = windowSize

        self.master = master

        self.myStatusBar = myStatusBar

        self.resolveManipulator()

        self.__layout = QGridLayout()

        self.__buttons = [QPushButton(name) for name in self.buttonsNames]

        [self.__layout.addWidget(value, i, j) for j, i, value in zip([2, 3, 3, 4], [3, 2, 4, 3], self.__buttons)]

        self.actions = [QAction("&dw", self), QAction("&lf", self), QAction("&ri", self), QAction("&up", self)]

        [a.triggered.connect(f) for a, f in zip(self.actions, self.fun)]

        [button.released.connect(f) for f, button in zip(self.fun, self.__buttons)]

        self.setLayout(self.__layout)

    def __key_up(self):
        self._manipulator.up()

    def __key_left(self):
        self._manipulator.left()

    def __key_right(self):
        self._manipulator.right()

    def __key_down(self):
        self._manipulator.down()

    def __stop(self):
        self._manipulator.stop()

    def center(self, pos):
        self._manipulator.center(pos)

    def moveUp(self):
        self._manipulator.up()

    def moveRight(self):
        self._manipulator.right()

    def moveDown(self):
        self._manipulator.down()

    def moveLeft(self):
        self._manipulator.left()

    def moveXY(self):
        x, y, speed = self.__getManipulatorParamiters()
        self._manipulator.goToCords(x=x + speed, y=y + speed)

    def moveNegativeXY(self):
        x, y, speed = self.__getManipulatorParamiters()
        self._manipulator.goToCords(x=x - speed, y=y - speed)

    def __getManipulatorParamiters(self):
        return self._manipulator.x, self._manipulator.y, self._manipulator.speed

    def waitForTarget(self):
        self._manipulator.waitForTarget()

    def createButtons(self, transparency=10):
        buttons = [QPushButton(name, self.master.widget) for name in self.buttonsNames]
        [button.released.connect(f) for f, button in zip(self.fun, buttons)]
        [button.setStyleSheet(f"background-color: rgba(255, 255, 255, {transparency});") for button in buttons]
        return buttons

    def createFocusSlider(self, transparency=10):
        slider = ManipulatorSlider(self._focusManipulator, -10000, 10000,
                                   value=self._focusManipulator.x,
                                   orientation=Qt.Vertical, widget=self.master)

        slider.setFixedWidth(20)
        slider.setFixedHeight(200)
        return slider

    def stop(self):
        self._manipulator.stop()

    def homeAxis(self):
        self._manipulator.homeAxis()

    def goToCords(self, x, y):
        self._manipulator.goToCords(x=x, y=y)

    @property
    def inMotion(self):
        return self._manipulator.inMotion

    def center(self, x, y):
        self._manipulator.center(x, y)
