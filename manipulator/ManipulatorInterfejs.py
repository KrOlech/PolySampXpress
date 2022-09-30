from PyQt5.QtCore import Qt
from manipulator.AbstractManipulatroInterfejs import _AbstractManipulatorInterfejs


class ManipulatorInterfere(_AbstractManipulatorInterfejs):

    def __init__(self, ManipulatorObject, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(ManipulatorObject, *args, **kwargs)

        keyboard = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]

