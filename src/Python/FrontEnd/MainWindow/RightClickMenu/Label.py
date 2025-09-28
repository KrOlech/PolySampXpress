from abc import ABCMeta, abstractmethod

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from Python.BaseClass.Logger.Logger import Loger
from Python.FrontEnd.MainWindow.RightClickMenu.RightClickMenu import RightMenu


class RightClickLabel(QLabel, Loger):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        super(RightClickLabel, self).__init__(*args, **kwargs)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menu)

    @abstractmethod
    def right_menu(self, pos):
        menu = RightMenu(self)

        menu.exec(self.mapToGlobal(pos))

    @abstractmethod
    def center(self):
        self.abstractmetod()
