from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import Qt

from src.MainWindow.Utilitis.WindowBar import MyBar


class MainWindowCustomBar(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindowCustomBar, self).__init__(*args, **kwargs)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mw = MainWindowCustomBar()

    mw.show()

    sys.exit(app.exec_())
