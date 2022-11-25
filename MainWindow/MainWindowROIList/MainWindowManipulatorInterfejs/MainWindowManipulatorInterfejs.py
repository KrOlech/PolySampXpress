from PyQt5.Qt import QPoint
from PyQt5.QtWidgets import QMessageBox, QPushButton

from MainWindow.MainWindowROIList.MainWindowManipulatorInterfejs.MainWindowRightClickMenu.MainWindwoQlabelROI import CameraGUIextention
from manipulator.AbstractManipulator import AbstractManipulator
from manipulator.ManipulatorInterfejs import ManipulatorInterfere
from manipulator.TCIPManipulator import TCIPManipulator


class MainWindowManipulatorInterfejs(CameraGUIextention):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.manipulator = TCIPManipulator() #AbstractManipulator()

        self.manipulatorInterferes = ManipulatorInterfere(self.manipulator)

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
        if self.manipulator:
            self.manipulator.close()

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

        self.Buttons = self._createManipulatorButtons()

        [button.setStyleSheet("background-color: rgba(255, 255, 255,100);") for button in self.Buttons]

        positions = [pos + button.geometry().bottomRight() - offset - QPoint(0, 20) for button, offset in
                     zip(self.Buttons, self.offsets)]

        [button.move(ps) for button, ps in zip(self.Buttons, positions)]
        [button.show() for button in self.Buttons]

    def hideRightClickButtons(self):
        [button.hide() for button in self.Buttons]
        self.Buttons = []


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
