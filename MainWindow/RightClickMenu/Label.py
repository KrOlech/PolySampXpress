from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

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
        abstractmetod(self)

    @abstractmethod
    def editROI(self):
        abstractmetod(self)

    @abstractmethod
    def center(self):
        abstractmetod(self)

    @abstractmethod
    def deleteROI(self):
        abstractmetod(self)
