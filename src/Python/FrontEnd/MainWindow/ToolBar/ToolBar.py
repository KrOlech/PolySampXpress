from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract
from PyQt5.QtCore import Qt


class MainWindowToolBar(MainWindowAbstract):

    def createToolbar(self):
        self.toolBar = self.addToolBar("File")

        self.toolBar.setFloatable(False)
        self.toolBar.setMovable(False)
        self.toolBar.setContextMenuPolicy(Qt.PreventContextMenu)

        self.addToolBar(self.toolBar)
