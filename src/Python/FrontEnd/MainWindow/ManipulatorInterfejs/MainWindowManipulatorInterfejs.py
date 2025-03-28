from PyQt5.Qt import QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMenu

from Python.BackEnd.Manipulator.Abstract.DialogWindow.MoveByValue import MoveByValue
from Python.BackEnd.Manipulator.Abstract.DialogWindow.RemoveSampleDialog import RemoveSampleDialog
from Python.BackEnd.SzarpnesCalculation.Main import SzarpnesCalculation
from Python.BackEnd.XeroStartup.Main import XeroStartup
from Python.BackEnd.XeroStartup.XeroConfirmationWindow import XeroConfirmationWindow
from Python.BackEnd.XeroStartup.XeroProgresWindow import XeroProgresWindow
from Python.BackEnd.XeroStartup.XeroTreySelection import XeroTreySelection
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.CameraRotationProgressClass import CameraRotationProgressClass
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.CameraRotationResultWindow import CameraRotationResultWindow
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.SharpnessCalculationConfig import SharpnessCalculationConfig
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.SampleAccessProgressWindow import SampleAccessProgressWindow
from Python.InacuracyMesurments.Main.Main import InaccuracyMeasurements
from Python.BackEnd.Calibration.LocateCrossAutomatic_3_0.main import LocateCross
from Python.FrontEnd.MainWindow.CloseWindow.ClosseWindow import ClosseWindow
from Python.FrontEnd.MainWindow.QlabelRoi.MainWindwoQlabelROI import CameraGUIExtension
from Python.BackEnd.Manipulator.Abstract.DialogWindow.SimpleDialogWindow import GoToCordsDialog
from Python.BackEnd.Manipulator.Abstract.DialogWindow.StepSizeDialog import SetStepSizeDialog
from Python.BackEnd.Manipulator.Abstract.DialogWindow.WaitDialoge import HomeAxisDialog
from Python.Interface.ManipulatorInterfejs.Main.ManipulatorInterfejs import ManipulatorInterfere
from Python.Utilitis.GenericProgressClass import GenericProgressClass
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness, image_sharpness2, sobel, \
    fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness


class MainWindowManipulatorInterfejs(CameraGUIExtension):
    offsets = [QPoint(100, 120), QPoint(150, 85), QPoint(50, 85), QPoint(100, 50)]
    buttons = None
    testEventClose = False
    calibratePixelsMode = False

    map00PointsVariable = None

    sampleTreyName = None

    dXmm: float = 0.0
    dYmm: float = 0.0

    StopTheRotationCalculation: bool = False

    def __init__(self, *args, **kwargs):
        super(MainWindowManipulatorInterfejs, self).__init__(*args, **kwargs)

        self.myStatusBar = self.__configureStatusBar()
        self.myStatusBarMouse = self.configureStatusBarMouse()

        self.manipulatorInterferes = ManipulatorInterfere(self, self.windowSize, self.myStatusBar)

        self.__manipulatorButtons()

        manipulatorMenu = self.menu.addMenu("&Manipulator")

        menuSetup = [("Home All Axis", self.__homeAxis),
                     ("Go To Cords", self.__goToCords),
                     ("Go To Center", self.__goToCenter),
                     ("Move By Value", self.__moveByValue),
                     ("Set Step Size", self.__setStepSize),
                     ("Calculate Inaccuracy", self.__calculateInaccuracy),
                     ("Go to Sample access position", self.removeSampleAsync),
                     ("Calculate Zero points", self._00Points)]

        self.refPoints = {}

        self.__addActionsToMenu(menuSetup, manipulatorMenu)

        self.SzarpnesCalculator = SzarpnesCalculation(self.manipulatorInterferes, self.camera, self)

        cameraMenuSetup = [("Auto Focus", lambda _: self.manipulatorInterferes.autoFokus(method=image_sharpness)),
                           ("Camera Rotation Calculation", self.__cameraRotationCalculationAsync)]

        self.__addActionsToMenu(cameraMenuSetup, self.cameraMenu)

        self.focusMenu = QMenu("Auto Focus alternative Methods", self)
        self.cameraMenu.addMenu(self.focusMenu)

        focusMenuSetup = [("Focus methods Scann", self.__sharpnessCalculatorRunAlgo),
                          ("Focus for current frame", self.SzarpnesCalculator.fokusForCurrentFrame)]

        self.__addActionsToMenu(focusMenuSetup, self.focusMenu)
        self.__addActionsToMenu(self.__focusMetods(), self.focusMenu)

    def __sharpnessCalculatorRunAlgo(self):
        window = SharpnessCalculationConfig("Szarpnes Calculation", self.SzarpnesCalculator.runAlgo, 250, self)
        window.exec_()

    def __focusMetods(self):
        funs: list = [image_sharpness, image_sharpness2, sobel, fft_based_sharpness, scharr_variance,
                      edge_based_sharpness, lpc_based_sharpness]
        focusMetods: list = []

        for fun in funs:
            focusMetods.append((fun.__name__, lambda _: self.manipulatorInterferes.autoFokus(method=fun)))

        return focusMetods

    def __addActionsToMenu(self, acctions, menu):
        for name, fun in acctions:
            self.__saveAndCreateAction(name, fun, menu)

    def _00Points(self):

        self.loger("do you wont to mark 00 Points?")
        XeroConfirmationWindow(self).exec_()

        if not self.createMapVariable:
            self.loger("no I don't wont to mark 00 Points")
            return

        if not self.manipulatorInterferes.AXIS_HOMED:
            self.__homeAxis()

        XeroTreySelection(self).exec_()

        self.zta = XeroStartup(self)

        window = XeroProgresWindow("Calculate Zero points", self.zeroOut, 200, self)
        window.run()
        window.exec_()

    def zeroOut(self):
        self.zta.xeroOut()

    def zeroOutMultiZoom(self):
        self.autoZoomMode = True
        for zoom in [0.85, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.zooms.setCurrentText(str(zoom))
            self.zta.xeroOut()
        self.autoZoomMode = False

    def homeAllAxis(self):
        window = GenericProgressClass("Start Up in progress", self.manipulatorInterferes.homeAxis, 200, self)
        window.run()
        window.exec_()

    def __createAction(self, name, manipulatorSeFun, checkable=True):
        return self.qActionCreate(name, manipulatorSeFun, checkable=checkable)

    def __saveAndCreateAction(self, name, manipulatorSeFun, menu, checkable=False):
        menu.addAction(self.__createAction(name, manipulatorSeFun, checkable))

    def __homeAxis(self):
        homeAxis = HomeAxisDialog(self.manipulatorInterferes)
        homeAxis.run()
        homeAxis.exec_()

    def __goToCenter(self):
        window = GenericProgressClass("Going to center in progress", self.manipulatorInterferes.goToCenter, 200, self)
        window.run()
        window.exec_()

    def __setZeroPoint(self):
        x, y = LocateCross(self, "00Location").locateCross()
        self.cameraView.setAbsolutZeroPositionForPixels(y, x)

    def __setZeroPointManual(self):
        self.calibratePixelsMode = True
        self.myStatusBarClick.setText("Select Zero Point")

    def __goToCords(self):
        GoToCordsDialog(self.manipulatorInterferes).exec_()

    def __moveByValue(self):
        MoveByValue(self.manipulatorInterferes).exec_()

    def __setStepSize(self):
        SetStepSizeDialog(self.manipulatorInterferes).exec_()

    def __calculateInaccuracy(self):
        InaccuracyMeasurements(self).runScript()

    def removeSampleAsync(self):

        if len(self.cameraView.ROIList):
            RemoveSampleDialog(self).exec_()

        if not self.manipulatorInterferes.AXIS_HOMED:
            self.__homeAxis()

        window = SampleAccessProgressWindow("Going to Sample access position in progress",
                                            self.manipulatorInterferes.removeSample, 200, self)
        window.run()
        window.exec_()

    def __configureStatusBar(self):
        myStatusBar = QLabel(self)

        myStatusBar.setFixedWidth(self.windowSize.width() // 8)

        myStatusBar.setStyleSheet("background-color: rgba(255, 255, 255, 75);")
        myStatusBar.setText("master have not been connected yet")
        font = QFont()
        font.setPointSize(13)
        myStatusBar.setFont(font)
        myStatusBar.move(QPoint(0, self.windowSize.height() - 25 - myStatusBar.height()))
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
        self.manipulatorInterferes.closeAction()

    def __manipulatorButtons(self):
        self.manipulatorButtons = self.manipulatorInterferes.createButtons(70)
        self.focusButtons = self.manipulatorInterferes.crateFocusButtons(70)
        self.focusSlider = self.manipulatorInterferes.focusSlider

        positions = [self.geometry().bottomRight() - button.geometry().bottomRight() - offset
                     for button, offset in zip(self.manipulatorButtons, self.offsets)]

        [button.move(pos - QPoint(self.focusSlider.width(), 80))
         for button, pos in zip(self.manipulatorButtons, positions)]

        self.focusSlider.move(QPoint(self.geometry().right() - 40,
                                     self.geometry().center().y() - self.focusSlider.height() // 2 + 20))

        self.focusButtons[1].move(QPoint(self.geometry().right() - 40,
                                         self.geometry().center().y() - self.focusSlider.height() // 2 - 120))

        self.focusButtons[0].move(QPoint(self.geometry().right() - 40,
                                         self.geometry().center().y() + self.focusSlider.height() // 2))

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
            QPoint((self.windowSize.width() // 8), self.windowSize.height() - 25 - myStatusBar.height()))
        myStatusBar.show()

        return myStatusBar

    def __cameraRotationCalculationAsync(self):
        self.StopTheRotationCalculation = True
        cameraRotationCalculationWindow = CameraRotationProgressClass("Camera Rotation Calculation in progress",
                                                                      self.__cameraRotationCalculation, 250,
                                                                      self)
        cameraRotationCalculationWindow.run()
        cameraRotationCalculationWindow.exec_()

    def showResultsRotationCalculation(self):
        CameraRotationResultWindow(self).exec_()

    def __cameraRotationCalculation(self):

        ITERATION_COUNT: int = 10

        ox, oy = JsonHandling.loadOffsetsJson(self.zoom)

        dx: int = 0
        dy: int = 0

        self.dXmm: float = 0.0
        self.dYmm: float = 0.0

        for _ in range(ITERATION_COUNT):
            x0, y0 = LocateCross(self, "Camera Rotation start point").locateCross(area=False)

            self.manipulatorInterferes.moveLeft(4)
            self.manipulatorInterferes.waitForTarget()
            x1, y1 = LocateCross(self, "Camera Rotation end point").locateCross(area=False)

            self.manipulatorInterferes.moveRight(4)
            self.manipulatorInterferes.waitForTarget()

            dx += x0 - x1
            dy += y0 - y1

            self.dXmm += dx / ox / ITERATION_COUNT
            self.dYmm += dy / oy / ITERATION_COUNT

            if self.StopTheRotationCalculation:
                return

        self.loger(f"dif in x:{dx} px dif in y:{dy} px ")
        self.loger(f"dif in x:{self.dXmm} mm dif in y:{self.dYmm} mm ")


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindowManipulatorInterfejs(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
