from PyQt5.Qt import QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton

from Python.InacuracyMesurments.Main.Main import InaccuracyMeasurements
from Python.BackEnd.Calibration.LocateCrossAutomatic_2_0.Main import LocateCross
from Python.FrontEnd.MainWindow.CloseWindow.ClosseWindow import ClosseWindow
from Python.FrontEnd.MainWindow.QlabelRoi.MainWindwoQlabelROI import CameraGUIExtension
from Python.BackEnd.Manipulator.Abstract.DialogWindow.SimpleDialogWindow import GoToCordsDialog
from Python.BackEnd.Manipulator.Abstract.DialogWindow.StepSizeDialog import SetStepSizeDialog
from Python.BackEnd.Manipulator.Abstract.DialogWindow.WaitDialoge import HomeAxisDialog
from Python.Interface.ManipulatorInterfejs.Main.ManipulatorInterfejs import ManipulatorInterfere


class MainWindowManipulatorInterfejs(CameraGUIExtension):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]
    buttons = None
    testEventClose = False
    calibratePixelsMode = False

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.myStatusBar = self.__configureStatusBar()
        self.myStatusBarMouse = self.configureStatusBarMouse()

        self.manipulatorInterferes = ManipulatorInterfere(self, self.windowSize, self.myStatusBar)

        self.__manipulatorButtons()

        manipulatorMenu = self.menu.addMenu("&Manipulator")

        homeAxis = self.qActionCreate("Home All Axis", self.__homeAxis)
        goToCords = self.qActionCreate("Go To Cords", self.__goToCords)
        setStepSize = self.qActionCreate("Set Step Size", self.__setStepSize)
        setZeroPoint = self.qActionCreate("Set Zero Point", self.__setZeroPoint)
        setZeroPointManual = self.qActionCreate("Set Zero Point Manual", self.__setZeroPointManual)
        calculateInaccuracy = self.qActionCreate("Calculate Inaccuracy", self.__calculateInaccuracy)

        manipulatorMenu.addAction(homeAxis)
        manipulatorMenu.addAction(goToCords)
        manipulatorMenu.addAction(setStepSize)
        manipulatorMenu.addAction(setZeroPoint)
        manipulatorMenu.addAction(setZeroPointManual)
        manipulatorMenu.addAction(calculateInaccuracy)

    def __createAction(self, name, manipulatorSeFun):
        return self.qActionCreate(name, manipulatorSeFun, checkable=True)

    def __homeAxis(self):
        homeAxis = HomeAxisDialog(self.manipulatorInterferes)
        homeAxis.run()
        homeAxis.exec_()

    def __setZeroPoint(self):
        x, y = LocateCross(self, "00Location").locateCross()
        self.cameraView.setAbsolutZeroPositionForPixels(y, x)

    def __setZeroPointManual(self):
        self.calibratePixelsMode = True
        self.myStatusBarClick.setText("Select Zero Point")

    def __goToCords(self):
        GoToCordsDialog(self.manipulatorInterferes).exec_()

    def __setStepSize(self):
        SetStepSizeDialog(self.manipulatorInterferes).exec_()

    def __calculateInaccuracy(self):
        InaccuracyMeasurements(self).runScript()

    def __configureStatusBar(self):
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
            self.logEnd()
            return

        event.ignore()

    def closeAction(self):
        self.manipulatorInterferes.closeAction()

    def __manipulatorButtons(self):
        self.manipulatorButtons = self.manipulatorInterferes.createButtons(70)
        self.focusButtons = self.manipulatorInterferes.crateFocusButtons()
        self.focusSlider = self.manipulatorInterferes.createFocusSlider()

        positions = [self.geometry().bottomRight() - button.geometry().bottomRight() - offset for
                     button, offset in zip(self.manipulatorButtons, self.offsets)]

        [button.move(pos - QPoint(self.focusSlider.width(), 80)) for button, pos in
         zip(self.manipulatorButtons, positions)]

        self.focusSlider.move(self.geometry().bottomRight() -
                              self.focusSlider.geometry().bottomRight()
                              - QPoint(300 + self.focusSlider.width(),
                                       35))  # todo full pruth calculation ja wiem ze to jest ok ale musi byc lepiej

        self.focusButtons[0].move(self.geometry().bottomRight() -
                                  self.focusButtons[0].geometry().bottomRight()
                                  - QPoint(300 + self.focusButtons[0].width(), 55))

        self.focusButtons[1].move(self.geometry().bottomRight() -
                                  self.focusButtons[1].geometry().bottomRight()
                                  - QPoint(300 + self.focusButtons[1].width(), self.focusSlider.height()+85))

    def rightMenu(self, pos):
        self.buttons = self.manipulatorInterferes.createButtons(100)

        positions = [pos + button.geometry().bottomRight() - offset - QPoint(0, 20) for button, offset in
                     zip(self.buttons, self.offsets)]

        [button.move(ps) for button, ps in zip(self.buttons, positions)]
        [button.show() for button in self.buttons]

    def hideRightClickButtons(self):
        [button.hide() for button in self.buttons]
        self.buttons = []

    def configureStatusBarMouse(self):
        myStatusBar = QLabel(self)

        myStatusBar.setFixedWidth(self.windowSize.width() // 8)

        myStatusBar.setStyleSheet("background-color: rgba(255, 255, 255, 75);")

        font = QFont()
        font.setPointSize(13)
        myStatusBar.setFont(font)
        myStatusBar.setText("test")
        myStatusBar.move(
            QPoint((self.windowSize.width() // 8), self.windowSize.height() - 25))
        myStatusBar.show()

        return myStatusBar


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
