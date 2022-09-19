from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt
from abc import abstractmethod
from abc import ABCMeta
from MainWindowMenuBar import MainWindowMenuBar
from Abstract import abstractmetod
from PyQt5.QtWidgets import QLabel


class RightMenu(QMenu):

    def __init__(self, mainWindow, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.center = self.addAction("Center Hear")
        self.center.triggered.connect(self.mainWindow.center)
        self.edit = self.addAction("Edit ROI")
        self.edit.triggered.connect(self.mainWindow.editROI)
        self.remove = self.addAction("delete ROI")
        self.remove.triggered.connect(self.mainWindow.deleteROI)
        self.disableOptions()

    def enableOptions(self):
        self._changeOptions(True)

    def disableOptions(self):
        self._changeOptions(False)

    def _changeOptions(self, change):
        self.edit.setEnabled(change)
        self.remove.setEnabled(change)


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
            menu = _RightMenu(self)
            if self.delite:
                menu.removeRoi()
            menu.exec_(self.mapToGlobal(pos))


    app = QApplication(sys.argv)

    window = TestWindow()

    window.show()

    app.exec_()
