from PyQt5.QtCore import Qt

from src.manipulator.Abstract.Interfejs.AbstractManipulatroInterfejs import AbstractManipulatorInterfejs


class ManipulatorInterfere(AbstractManipulatorInterfejs):

    def __init__(self, master, *args, **kwargs):
        super(ManipulatorInterfere, self).__init__(master, *args, **kwargs)

        keyboard = [Qt.Key_Up, Qt.Key_Left, Qt.Key_Right, Qt.Key_Down] #todo inwestigate why not working corectli newer inicialise?

        [a.setShortcut(k) for a, k in zip(self.actions, keyboard)]

