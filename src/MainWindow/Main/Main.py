from src.MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from src.MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


class MainWindow(MainWindowInicialisationFlag,
                 MainWindowRoiCreationInterferes):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.createRoiModsMenu()
