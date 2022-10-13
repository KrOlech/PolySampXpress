from MainWindowRightClickMenu.MainWindwoQlabelROI import CameraGUIextention
from manipulator.ManipulatorInterfejs import ManipulatorInterfere
from manipulator.AbstractManipulator import AbstractManipulator
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.Qt import QPoint


class MainWindowManipulatorInterfejs(CameraGUIextention):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]

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

    def _createManipulatorButtons(self):
        buttons = [QPushButton(name, self.widget) for name in self.manipulatorInterferes.buttonsNames]
        [button.released.connect(f) for f, button in zip(self.manipulatorInterferes.fun, buttons)]
        [button.setStyleSheet("background-color: rgba(255, 255, 255, 10);") for button in buttons]
        return buttons

    def _manipulatorButtons(self):

        self.manipulatorButtons = self._createManipulatorButtons()

        self.positions = [self.geometry().bottomRight() - button.geometry().bottomRight() - offset for button, offset in
                          zip(self.manipulatorButtons, self.offsets)]

        [button.move(pos) for button, pos in zip(self.manipulatorButtons, self.positions)]

    def right_menu(self, pos):

        Buttons = self._createManipulatorButtons()

        [button.setStyleSheet("background-color: rgba(255, 255, 255,100);") for button in self.manipulatorButtons]

        positions = [pos + button.geometry().bottomRight() - offset - QPoint(0, 20) for button, offset in
                     zip(Buttons, self.offsets)]

        [button.move(ps) for button, ps in zip(self.manipulatorButtons, positions)]

    def hideRightClickButtons(self):
        [button.setStyleSheet("background-color: rgba(255, 255, 255, 10);") for button in self.manipulatorButtons]
        [button.move(pos) for button, pos in zip(self.manipulatorButtons, self.positions)]


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
