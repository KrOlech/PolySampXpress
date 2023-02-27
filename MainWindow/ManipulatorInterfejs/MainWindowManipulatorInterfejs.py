from PyQt5.Qt import QPoint
from PyQt5.QtWidgets import QMessageBox, QPushButton

from MainWindow.QlabelRoi.MainWindwoQlabelROI import CameraGUIExtension
from manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from manipulator.Interfejs.ManipulatorInterfejs import ManipulatorInterfere
from manipulator.Standa.StandaManipulator import StandaManipulator
from manipulator.TCIP.TCIPManipulator import TCIPManipulator


class MainWindowManipulatorInterfejs(CameraGUIExtension):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]
    buttons = None

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.manipulator = TCIPManipulator(self.windowSize)  # AbstractManipulator() TCIPManipulator, StandaManipulator

        self.manipulatorInterferes = ManipulatorInterfere(self.manipulator)

        self.__manipulatorButtons()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "mesage",
                                     "Czy napewno chcesz zamknac program?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.closeAction()
            event.accept()
        else:
            event.ignore()

    def closeAction(self):
        if self.manipulator:
            self.manipulator.close()

    def __createManipulatorButtons(self):
        buttons = [QPushButton(name, self.widget) for name in self.manipulatorInterferes.buttonsNames]
        [button.released.connect(f) for f, button in zip(self.manipulatorInterferes.fun, buttons)]
        [button.setStyleSheet("background-color: rgba(255, 255, 255, 10);") for button in buttons]
        return buttons

    def __manipulatorButtons(self):
        self.manipulatorButtons = self.__createManipulatorButtons()

        self.positions = [self.geometry().bottomRight() - button.geometry().bottomRight() - offset for button, offset in
                          zip(self.manipulatorButtons, self.offsets)]

        [button.move(pos) for button, pos in zip(self.manipulatorButtons, self.positions)]

    def rightMenu(self, pos):
        self.buttons = self.__createManipulatorButtons()

        [button.setStyleSheet("background-color: rgba(255, 255, 255,100);") for button in self.buttons]

        positions = [pos + button.geometry().bottomRight() - offset - QPoint(0, 20) for button, offset in
                     zip(self.buttons, self.offsets)]

        [button.move(ps) for button, ps in zip(self.buttons, positions)]
        [button.show() for button in self.buttons]

    def hideRightClickButtons(self):
        [button.hide() for button in self.buttons]
        self.buttons = []


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
