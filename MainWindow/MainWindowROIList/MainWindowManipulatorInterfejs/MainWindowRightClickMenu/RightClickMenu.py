from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt
from abc import abstractmethod
from abc import ABCMeta

from PyQt5 import QtGui

from utilitis.Abstract import abstractmetod
from PyQt5.QtWidgets import QLabel


class RightMenu(QMenu):

    def __init__(self, mainWindow, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.center = self.addAction("Center Hear")
        self.center.triggered.connect(self.mainWindow.center)

    def addRoiMenus(self, rois, editTrybe):
        menus = []
        if editTrybe:
            self.center = self.addAction("end edit")
            self.center.triggered.connect(self.mainWindow.endEdit)

        for roi in rois:
            menu = self.addMenu(str(roi.name))
            menus.append(menu)
            edit = menu.addAction("Edit ROI")
            rename = menu.addAction("Rename")
            delete = menu.addAction("delete ROI")
            edit.triggered.connect(roi.edit)
            delete.triggered.connect(roi.delete)
            rename.triggered.connect(roi.rename)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.mainWindow.hideRightClickButtons()
        super(RightMenu, self).closeEvent(a0)


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
