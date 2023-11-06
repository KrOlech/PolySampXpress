from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from src.Python.BaseClass.Logger.Logger import Loger
from src.Python.FrontEnd.MainWindow.RightClickMenu.RightClickMenu import RightMenu


class RightClickLabel(QLabel, Loger):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        super(RightClickLabel, self).__init__(*args, **kwargs)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menu)

    @abstractmethod
    def right_menu(self, pos):
        menu = RightMenu(self)

        menu.exec_(self.mapToGlobal(pos))

    @abstractmethod
    def newROI(self):
        self.abstractmetod()

    @abstractmethod
    def editROI(self):
        self.abstractmetod()

    @abstractmethod
    def center(self):
        self.abstractmetod()

    @abstractmethod
    def deleteROI(self):
        self.abstractmetod()
