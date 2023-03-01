import sys

from PyQt5.QtWidgets import QApplication
from MainWindow.Main.Main import MainWindow
from WorkFeald.Main.main import ReadPoleRobocze


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    window = ReadPoleRobocze(mainWindow, app.desktop().availableGeometry().size())

    mainWindow.show()

    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
    # cProfile.run("main()", filename='my_profile.prof')
