from PyQt5.Qt import QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel

# todo move to separate classes
from src.MainWindow.CloseWindow.ClosseWindow import ClosseWindow
from src.MainWindow.QlabelRoi.MainWindwoQlabelROI import CameraGUIExtension
from src.Manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from src.Manipulator.Abstract.DialogWindow.SimpleDialogWindow import GoToCordsDialog
from src.Manipulator.Abstract.DialogWindow.StepSizeDialog import SetStepSizeDialog
from src.Manipulator.Abstract.DialogWindow.WaitDialoge import HomeAxisDialog
from src.Manipulator.Interfejs.ManipulatorInterfejs import ManipulatorInterfere
from src.Manipulator.SCIIPPlus.Main.MainHardwer import SCIManipulatorMain
from src.Manipulator.SCIIPPlus.Main.MainSymulator import SCIManipulatorSimulator
from src.Manipulator.Standa import StandaManipulator


class MainWindowManipulatorInterfejs(CameraGUIExtension):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]
    buttons = None
    testEventClose = False

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.myStatusBar = self.configureStatusBar()
        self.myStatusBarMouse = self.configureStatusBarMouse()

        self.manipulator = AbstractManipulator(self.windowSize, self.myStatusBar)

        self.manipulatorInterferes = ManipulatorInterfere(self)

        self.__manipulatorButtons()

        manipulatorMenu = self.menu.addMenu("&Manipulator")

        homeAxis = self.qActionCreate("Home All Axis", self.homeAxis)
        goToCords = self.qActionCreate("Go To Cords", self.goToCords)
        setStepSize = self.qActionCreate("Set Step Size", self.setStepSize)

        manipulatorMenu.addAction(homeAxis)
        manipulatorMenu.addAction(goToCords)
        manipulatorMenu.addAction(setStepSize)

        manipulatorChoiceMenu = manipulatorMenu.addMenu("&Manipulator Type")

        self.abstractManipulatorAction = self.__createAction("AbstractManipulator", self.setAbstractManipulator)
        self.standManipulatorAction = self.__createAction("StandManipulator", self.setStandManipulator)
        self.sCIManipulatorSimulatorAction = self.__createAction("SCISimulator", self.setSCIManipulatorSimulator)
        self.sCIManipulatorMainAction = self.__createAction("SCIManipulatorMain", self.setSCIManipulatorMain, )

        manipulatorChoiceMenu.addAction(self.abstractManipulatorAction)
        manipulatorChoiceMenu.addAction(self.standManipulatorAction)
        manipulatorChoiceMenu.addAction(self.sCIManipulatorSimulatorAction)
        manipulatorChoiceMenu.addAction(self.sCIManipulatorMainAction)

        self.manipulatorActions = [self.abstractManipulatorAction, self.standManipulatorAction,
                                   self.sCIManipulatorSimulatorAction, self.sCIManipulatorMainAction]

        self.abstractManipulatorAction.setChecked(True)

    def __createAction(self, name, manipulatorSeFun):
        return self.qActionCreate(name, manipulatorSeFun, checkable=True)

    def setAbstractManipulator(self):
        self.__UncheckAll()
        self.manipulator.close()
        self.abstractManipulatorAction.setChecked(True)
        self.manipulator = AbstractManipulator(self.windowSize, self.myStatusBar)

    def setStandManipulator(self):
        self.__UncheckAll()
        self.manipulator.close()
        self.standManipulatorAction.setChecked(True)
        self.manipulator = StandaManipulator(self.windowSize, self.myStatusBar)

    def setSCIManipulatorSimulator(self):
        self.__UncheckAll()
        self.manipulator.close()
        self.sCIManipulatorSimulatorAction.setChecked(True)
        self.manipulator = SCIManipulatorSimulator(self.windowSize, self.myStatusBar)

    def setSCIManipulatorMain(self):
        self.__UncheckAll()
        self.manipulator.close()
        self.sCIManipulatorMainAction.setChecked(True)
        self.manipulator = SCIManipulatorMain(self.windowSize, self.myStatusBar)

    def __UncheckAll(self, State=False):
        for manipulatorAction in self.manipulatorActions:
            manipulatorAction.setChecked(State)

    def homeAxis(self):
        homeAxis = HomeAxisDialog(self.manipulator)
        homeAxis.run()
        homeAxis.exec_()

    def goToCords(self):
        GoToCordsDialog(self.manipulator).exec_()

    def setStepSize(self):
        SetStepSizeDialog(self.manipulator).exec_()

    def configureStatusBar(self):
        myStatusBar = QLabel(self)

        myStatusBar.setFixedWidth(self.windowSize.width() // 8)

        myStatusBar.setStyleSheet("background-color: rgba(255, 255, 255, 75);")
        myStatusBar.setText("master have not been connected yet")
        font = QFont()
        font.setPointSize(13)
        myStatusBar.setFont(font)
        myStatusBar.move(QPoint(0, self.windowSize.height() - 25))
        myStatusBar.show()

        return myStatusBar

    def closeEvent(self, event):

        ClosseWindow(self).exec_()

        if self.testEventClose:
            self.closeAction()
            event.accept()
            return

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

    def configureStatusBarMouse(self):
        myStatusBar = QLabel(self)

        myStatusBar.setFixedWidth(self.windowSize.width() // 16)

        myStatusBar.setStyleSheet("background-color: rgba(255, 255, 255, 75);")

        font = QFont()
        font.setPointSize(13)
        myStatusBar.setFont(font)
        myStatusBar.setText("test")
        myStatusBar.move(
            QPoint(self.windowSize.width() - (self.windowSize.width() // 16), self.windowSize.height() - 25))
        myStatusBar.show()

        return myStatusBar


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
