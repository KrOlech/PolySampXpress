from MainWindow.MainWindowROIList import MainWindowROIList
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':


    app = QApplication(sys.argv)

    window = MainWindowROIList(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
