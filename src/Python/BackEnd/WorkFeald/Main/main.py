from PyQt5.QtCore import Qt

from Python.BackEnd.WorkFeald.GUI.Gui import WorkFilledGui
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker import workFunWorker


class ReadPoleRobocze:

    def __init__(self, mainWindow, windowSize):

        self.mainWindow = mainWindow

        self.workFields = JsonHandling.loadPolaRoboczeJson()

        self.GUI = WorkFilledGui(self.workFields, windowSize)
        self.GUI.setWindowFlag(Qt.Popup)

        workFunWorker(self, self.__threadWaitForInicialisation)

    def __threadWaitForInicialisation(self):
        while True:
            if self.GUI.valueSet:
                self.showMain()
                break

    def show(self):
        self.GUI.show()

    def showMain(self):
        self.mainWindow.setPoleRobocze(self.GUI.fildParameters)
        self.mainWindow.cameraView.afterInitialisation = True
