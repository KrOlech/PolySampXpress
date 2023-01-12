import sys

from PyQt5.QtWidgets import QApplication

from MainWindow.MapConection.MapInterfejs import MainWindowMapInterfejs
from WorkFeald.Main.main import ReadPoleRobocze

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindowMapInterfejs(app.desktop().availableGeometry().size())

    window = ReadPoleRobocze(mainWindow,app.desktop().availableGeometry().size())

    mainWindow.show()

    window.show()

    app.exec_()
