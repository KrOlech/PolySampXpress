from Python.FrontEnd.MainWindow.StepSize.StepSize import MainWindowStepSize
from Python.FrontEnd.MainWindow.ToolBar.ToolBar import MainWindowToolBar
from Python.FrontEnd.MainWindow.Zoom.MainWindowZoom import MainWindowZoom
from Python.FrontEnd.MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from Python.FrontEnd.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


class MainWindow(MainWindowInicialisationFlag,
                 MainWindowRoiCreationInterferes,
                 MainWindowToolBar,
                 MainWindowZoom,
                 MainWindowStepSize):

    def __init__(self, *args, **kwargs):
        self.logStart()
        super().__init__(*args, **kwargs)

        self.createRoiModsMenu()

        self.createToolbar()

        self.createZoom()

        self.createStepSize()

    def TestClose(self):
        self.testEventClose = True
        self.close()
