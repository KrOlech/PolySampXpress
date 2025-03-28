from PyQt5.QtCore import Qt

from Python.BackEnd.AutoFokus_02.Main.AutoFokus_02 import AutoFokus02
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness
from Python.Interface.ManipulatorInterfejs.Abstract.AbstractManipulatroInterfejs import \
    AbstractManipulatorInterferes
from Python.Interface.ManipulatorInterfejs.Selection.Select import SelectManipulator
from Python.Utilitis.GenericProgressClass import GenericProgressClass


class ManipulatorInterfere(AbstractManipulatorInterferes, SelectManipulator):

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, windowSize, myStatusBar, *args, **kwargs)

        # keyboard = [Qt.Key_W, Qt.Key_A, Qt.Key_D, Qt.Key_S]
        keyboard2 = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        # [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]
        [a.setShortcut(k) for a, k in zip(self.actions, keyboard2)]

        [a.setShortcutContext(Qt.WindowShortcut) for a in self.actions]

        [self.master.addAction(a) for a in self.actions]

        # self.autoFokus()

    def autoFokus(self, method=image_sharpness, showResults=False):
        focus = AutoFokus02(self, self.master.camera, method)
        window = GenericProgressClass("Auto Fokus in progress", focus.run, 200, self)
        focus.window = window

        window.run()
        window.exec_()

        if showResults:
            focus.show()

    def autoFokusNotAsync(self):
        fokus = AutoFokus02(self, self.master.camera)
        fokus.run()

    def fokusGoTo(self, x):
        self._focusManipulator.x = x
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    def fokusUp(self, d=100):
        self._focusManipulator.x += d
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    def fokusDown(self, d=100):
        self._focusManipulator.x -= d
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    def fokus0(self, x=2250):
        self._focusManipulator.x = x
        self._focusManipulator.gotoNotAsync()
        self._focusManipulator.waitForTarget()

    @property
    def fokusPos(self):
        return self._focusManipulator.x
