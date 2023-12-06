from Python.FrontEnd.MainWindow.Zoom.MainWindowZoom import MainWindowZoom
from Python.FrontEnd.MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from Python.FrontEnd.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


class MainWindow(MainWindowInicialisationFlag,
                 MainWindowRoiCreationInterferes,
                 MainWindowZoom):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.createRoiModsMenu()

        self.createZoomSlider()

    def TestClose(self):
        self.testEventClose = True
        self.close()
