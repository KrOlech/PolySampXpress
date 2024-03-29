from PyQt5.QtWidgets import QLabel

from Python.BackEnd.Manipulator.Abstract.DialogWindow.Abstract import AbstractDialog
from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowStepSize(MainWindowAbstract):
    def createStepSize(self):
        self.toolBar.addSeparator()
        self.toolBar.addWidget(QLabel(" Step Size: "))

        self.valueX = AbstractDialog.createQSpinBox(self.manipulatorInterferes.speed)
        self.valueX.valueChanged.connect(self.newStepSize)
        
        self.toolBar.addWidget(self.valueX)

    def newStepSize(self):
        self.manipulatorInterferes.setSpeed(self.valueX.value())
