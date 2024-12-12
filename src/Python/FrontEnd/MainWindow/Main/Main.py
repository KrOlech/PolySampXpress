from Python.FrontEnd.MainWindow.MapMenuList.MainWindowMapMenuList import MainWindowMapMenuList
from Python.FrontEnd.MainWindow.MapMenus.MainWindowMapMenu import MainWindowMapMenu
from Python.FrontEnd.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes
from Python.FrontEnd.MainWindow.RoiList.MainWindowROIList import MainWindowROIList
from Python.FrontEnd.MainWindow.StepSize.StepSize import MainWindowStepSize
from Python.FrontEnd.MainWindow.ToolBar.ToolBar import MainWindowToolBar
from Python.FrontEnd.MainWindow.WorkFieldMenu.MainWindowWorkFieldMenu import MainWindowWorkFieldMenu
from Python.FrontEnd.MainWindow.Zoom.MainWindowZoom import MainWindowZoom


class MainWindow(MainWindowROIList,
                 MainWindowRoiCreationInterferes,
                 MainWindowToolBar,
                 MainWindowZoom,
                 MainWindowStepSize,
                 MainWindowWorkFieldMenu,
                 MainWindowMapMenu,
                 MainWindowMapMenuList):

    def __init__(self, *args, **kwargs):
        self.logStart()
        super().__init__(*args, **kwargs)

        self.createRoiModsMenu()

        self.createToolbar()

        self.createZoom()

        self.createStepSize()

        self.createMapMenu()

        self.createMapMenuList()

        self.createWorkFieldMenu()

    def TestClose(self):
        self.testEventClose = True
        self.close()

    def closeAction(self):
        super(MainWindow, self).closeAction()
        self.closeActionMapMenus()
