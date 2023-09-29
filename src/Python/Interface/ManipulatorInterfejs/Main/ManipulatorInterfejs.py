import cv2
from PyQt5.QtCore import Qt

from src.Python.Interface.ManipulatorInterfejs.Abstract.AbstractManipulatroInterfejs import AbstractManipulatorInterferes
from src.Python.Interface.ManipulatorInterfejs.Selection.Select import SelectManipulator


class ManipulatorInterfere(AbstractManipulatorInterferes, SelectManipulator):

    def __init__(self, master, windowSize, myStatusBar, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, windowSize, myStatusBar, *args, **kwargs)

        # toDo no simple two shortcut for single action
        # keyboard = [Qt.Key_W, Qt.Key_A, Qt.Key_D, Qt.Key_S]
        keyboard2 = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        # [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]
        [a.setShortcut(k) for a, k in zip(self.actions, keyboard2)]

        [a.setShortcutContext(Qt.WindowShortcut) for a in self.actions]

        [self.master.addAction(a) for a in self.actions]

        #self.autoFokus()

    def __calcucateFokus(self):
        image = self.master.camera.getFrame()
        return cv2.Laplacian(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()

    def autoFokus(self):

        treshold = self.__calcucateFokus()
        self._focusManipulator.x -= 1
        self._focusManipulator.gotoNotAsync()

        while True:
            focusMetric = self.__calcucateFokus()

            if focusMetric < treshold:
                self._focusManipulator.x -= 1
            if focusMetric > treshold:
                self._focusManipulator.x += 1
            self._focusManipulator.gotoNotAsync()

            newTreshold = self.__calcucateFokus()

            self.loger(treshold, newTreshold)

            if round(newTreshold - treshold, 2) == 0:
                break
            else:
                treshold = newTreshold