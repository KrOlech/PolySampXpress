from MainWindow.MainWindowROIList import MainWindowROIList


class MainWindow(MainWindowROIList):
    pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = MainWindow(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
