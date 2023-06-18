from src.MainWindow.Zoom.MainWindowZoom import MainWindowZoom
from src.MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from src.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


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
