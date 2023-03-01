from MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from MainWindow.RoiCreation.RoiCreation import MainWindowRoiCreationInterferes


class MainWindow(MainWindowInicialisationFlag,
                 MainWindowRoiCreationInterferes):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.createRoiModsMenu()
