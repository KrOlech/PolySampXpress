from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt
from abc import abstractmethod
from abc import ABCMeta
from MainWindowMenuBar import MainWindowMenuBar
from Abstract import abstractmetod

class RightMenu(QMenu):

    def __init__(self, mainWindow, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        new = self.addAction("New ROI")
        edit = self.addAction("Edit ROI")
        center = self.addAction("Center Hear")

        new.triggered.connect(self.mainWindow.newROI)
        edit.triggered.connect(self.mainWindow.editROI)
        center.triggered.connect(self.mainWindow.center)

    def removeRoi(self):
        remove = self.addAction("delete ROI")
        remove.triggered.connect(self.mainWindow.deleteROI)


class MainWindow(MainWindowMenuBar):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

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


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication


    class TestWindow(MainWindow):

        def __init__(self):
            super(TestWindow, self).__init__()
            self.delite = False

            testmenu = self.menu.addMenu("&test")
            testmenu.addAction(self.qActionCreate("&togle", self.toglecreate))

        def toglecreate(self):
            self.delite = not self.delite

        def right_menu(self, pos):
            menu = RightMenu(self)
            if self.delite:
                menu.removeRoi()
            menu.exec_(self.mapToGlobal(pos))


    app = QApplication(sys.argv)

    window = TestWindow()

    window.show()

    app.exec_()
