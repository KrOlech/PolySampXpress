import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Python.FrontEnd.MainWindow.Main.Main import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationDisplayName("PolySampXpress beta-0.7")

    icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))

    app.setWindowIcon(icon)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())
    mainWindow.setWindowIcon(icon)

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    app.exec_()


if __name__ == '__main__':
    main()
    # cProfile.run("main()", filename='my_profile.prof')
