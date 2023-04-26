import sys

from PyQt5.QtWidgets import QApplication

from src.MainWindow.Main.Main import MainWindow


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow(app.desktop().availableGeometry().size())

    mainWindow.show()

    mainWindow.readWorkFieldWindow.show()

    app.exec_()


if __name__ == '__main__':
    main()
    # cProfile.run("main()", filename='my_profile.prof')
