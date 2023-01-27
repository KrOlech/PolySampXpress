import sys

from PyQt5.QtWidgets import QApplication

from MainWindow.InicialisationFlag.MainWindowIniciialisationFlag import MainWindowInicialisationFlag
from WorkFeald.Main.main import ReadPoleRobocze

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindowInicialisationFlag(app.desktop().availableGeometry().size())

    window = ReadPoleRobocze(mainWindow,app.desktop().availableGeometry().size())

    mainWindow.show()

    window.show()

    app.exec_()
