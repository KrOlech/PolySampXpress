import sys

from PyQt5.QtWidgets import QApplication

from MAP.PolaRobocze import ReadPoleRobocze
from MainWindow.MainWindowIniciialisationFlag import MainWindowInicialisationFlag

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindowInicialisationFlag(app.desktop().availableGeometry().size())

    window = ReadPoleRobocze(mainWindow)

    mainWindow.show()

    window.show()

    app.exec_()
