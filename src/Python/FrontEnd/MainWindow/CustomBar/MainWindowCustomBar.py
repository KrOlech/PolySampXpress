from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication

from PyQt6.QtCore import Qt, QEvent

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
#rom Python.FrontEnd.MainWindow.Utilitis.WindowBar import MyBar


class MainWindowCustomBar(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindowCustomBar, self).__init__(*args, **kwargs)

        icon = QIcon(JsonHandling.getFileLocation("smallLogo.png"))
        self.setWindowIcon(icon)

        self.center_window()

    def center_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:

            if self.windowState() & Qt.WindowState.WindowMaximized:
                self.showFullScreen()

            elif not self.isFullScreen():
                self.showNormal()

        super().changeEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape and self.isFullScreen():
            self.showNormal()


    def mouseDoubleClickEvent(self, event):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mw = MainWindowCustomBar()

    mw.show()

    sys.exit(app.exec())
