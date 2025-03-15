from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QAction

from Python.BaseClass.Logger.Logger import Loger
from Python.Interface.ManipulatorInterfejs.ManipulatorSlider.ManipulatorSlider import ManipulatorSlider


class AbstractManipulatorInterferes(QWidget, Loger):
    _focusManipulator = None
    _zoomManipulator = None
    _manipulator = None

    AXIS_HOMED = False

    @property
    def buttonsNames(self):
        return ["/\\", "<", ">", r'\/']

    @property
    def focusPosition(self):
        return self._focusManipulator.x

    @property
    def x(self):
        return self._manipulator.x

    @property
    def y(self):
        return self._manipulator.y

    @property
    def x0(self):
        return self._manipulator.x0

    @property
    def y0(self):
        return self._manipulator.y0

    @property
    def speed(self):
        return self._manipulator.speed

    @property
    def sampleAccessPosition(self) -> (int, int):
        return 90, 0

    @property
    def centerPosition(self) -> (int, int):
        return 100, 100

    @property
    def inMotion(self):
        return self._manipulator.inMotion

    def conn(self):
        return self._manipulator.conn

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(AbstractManipulatorInterferes, self).__init__(*args, **kwargs)

        self.fun = [self.__key_down, self.__key_left, self.__key_right, self.__key_up]

        self.focusFun = [self.__focus_key_down, self.__fockus_key_up]

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
        if not self._manipulator.inMotion:
            self._manipulator.up()

    def __key_left(self):
        if not self._manipulator.inMotion:
            self._manipulator.left()

    def __key_right(self):
        if not self._manipulator.inMotion:
            self._manipulator.right()

    def __key_down(self):
        if not self._manipulator.inMotion:
            self._manipulator.down()

    def __fockus_key_up(self):
        self._focusManipulator.left()

    def __focus_key_down(self):
        self._focusManipulator.right()

    def __stop(self):
        self._manipulator.stop()

    def moveUp(self):
        self._manipulator.up()

    def moveRight(self, step: int = 1):
        self._manipulator.right(step)

    def moveDown(self):
        self._manipulator.down()

    def moveLeft(self, step: int = 1):
        self._manipulator.left(step)

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
        self._focusManipulator.waitForTarget()
        self._zoomManipulator.waitForTarget()

    def createButtons(self, transparency=10):
        buttons = [QPushButton(name, self.master.widget) for name in self.buttonsNames]
        [button.released.connect(f) for f, button in zip(self.fun, buttons)]
        [button.setStyleSheet(f"background-color: rgba(255, 255, 255, {transparency});") for button in buttons]
        return buttons

    def crateFocusButtons(self, transparency=10):
        buttons = [QPushButton(r'\/', self.master.widget), QPushButton("/\\", self.master.widget)]
        [button.setStyleSheet(f"background-color: rgba(255, 255, 255, {transparency});") for button in buttons]
        [button.released.connect(f) for f, button in zip(self.focusFun, buttons)]
        [button.setFixedSize(20, 20) for button in buttons]
        return buttons

    def createFocusSlider(self):
        slider = ManipulatorSlider(self._focusManipulator,
                                   value=self._focusManipulator.x,
                                   widget=self.master)

        return slider

    def stop(self):
        self._manipulator.stop()

    def homeAxis(self):
        self._manipulator.homeAxis()
        self.AXIS_HOMED = True

    def goToCenter(self):
        self.goToCords(*self.centerPosition)

    def goToCords(self, x, y):
        self._manipulator.goToCords(x=x, y=y)

    def removeSample(self):
        self._manipulator.goToCords(*self.sampleAccessPosition)

    async def goToCordsAsync(self, x, y):
        self._manipulator.goToCords(x=x, y=y)
        self._manipulator.waitForTarget()

    def center(self, x, y, zoom):
        self._manipulator.center(x, y, zoom)

    async def zoomManipulatorChange(self, cords):
        self._zoomManipulator.x = 0
        self._zoomManipulator.gotoNotAsync()
        self._zoomManipulator.waitForTarget()
        self._zoomManipulator.x = self._zoomManipulator.ZoomStepsMap[cords]
        self._zoomManipulator.gotoNotAsync()
        self._zoomManipulator.waitForTarget()

    def syncZoomManipulatorChange(self, cords):
        self._zoomManipulator.x = 0
        self._zoomManipulator.gotoNotAsync()
        self._zoomManipulator.waitForTarget()
        self._zoomManipulator.x = self._zoomManipulator.ZoomStepsMap[cords]
        self._zoomManipulator.gotoNotAsync()
        self._zoomManipulator.waitForTarget()

    def fokusManipulatorChange(self):
        self._focusManipulator.gotoNotAsync()

    def setSpeed(self, newSpeed):
        self._manipulator.speed = newSpeed
