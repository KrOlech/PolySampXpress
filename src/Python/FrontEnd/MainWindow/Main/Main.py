from src.Python.FrontEnd.MainWindow.Zoom.MainWindowZoom import MainWindowZoom
from src.Python.FrontEnd.MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from src.Python.FrontEnd.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


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
