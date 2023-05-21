from PyQt5.QtCore import Qt

from src.Manipulator.Interfejs.AbstractManipulatroInterfejs import AbstractManipulatorInterfejs


class ManipulatorInterfere(AbstractManipulatorInterfejs):

    def __init__(self, master, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, *args, **kwargs)

        # toDo no simple two shortcut for single action
        # keyboard = [Qt.Key_W, Qt.Key_A, Qt.Key_D, Qt.Key_S]
        keyboard2 = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down]

        # [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]
        [a.setShortcut(k) for a, k in zip(self.actions, keyboard2)]

        [a.setShortcutContext(Qt.WindowShortcut) for a in self.actions]

        [self.master.addAction(a) for a in self.actions]
