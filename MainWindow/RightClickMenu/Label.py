from abc import ABCMeta, abstractmethod

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel

from MainWindow.RightClickMenu.RightClickMenu import RightMenu
from utilitis.Abstract import abstractmetod


class RightClickLabel(QLabel):
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
        abstractmetod()

    @abstractmethod
    def editROI(self):
        abstractmetod()

    @abstractmethod
    def center(self):
        abstractmetod()

    @abstractmethod
    def deleteROI(self):
        abstractmetod()
