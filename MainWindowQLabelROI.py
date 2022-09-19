from QlabelROI import QlabelROI
from CameraGUI import CameraGUI
from abc import ABCMeta

class QlabelExtention(QlabelROI):


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    window = MainWindowQLabelROI()

    window.show()

    app.exec_()
