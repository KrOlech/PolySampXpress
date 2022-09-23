from MainWindowRightClickMenu.QlabelROI import CameraGUIextention
from manipulator.ManipulatorInterfejs import ManipulatorInterfere
from manipulator.AbstractManipulator import AbstractManipulator
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.Qt import QPoint


class MainWindowManipulatorInterfejs(CameraGUIextention):

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.manipulatorInterferes = ManipulatorInterfere(AbstractManipulator())

        self._manipulatorButtons()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, "mesage",
                                     "Czy napewno chcesz zamknac program?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:

            self.closeActtion()
            event.accept()

        else:
            event.ignore()

    def closeActtion(self):
        pass

    def _manipulatorButtons(self):

        self.manipulatorButtons = [QPushButton(name, self.widget) for name in self.manipulatorInterferes.buttonsNames]
        [button.released.connect(f) for f, button in zip(self.manipulatorInterferes.fun, self.manipulatorButtons)]

        self.offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]
        self.positions = [self.geometry().bottomRight() - button.geometry().bottomRight() - offset for button, offset in
                          zip(self.manipulatorButtons, self.offsets)]
        [button.move(pos) for button, pos in zip(self.manipulatorButtons, self.positions)]


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
