from PyQt5.QtWidgets import QLabel, QComboBox

from Python.FrontEnd.MainWindow.Abstract.MainWindowAbstract import MainWindowAbstract


class MainWindowStepSize(MainWindowAbstract):
    stepsDictionary = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0.5, 6: 0.5, 7: 0.1, 8: 0.1, 9: 0.1,
                       10: 0.1}  # toDo set empiricly

    def createStepSize(self):
        self.toolBar.addSeparator()
        self.toolBar.addWidget(QLabel(" Step Size: "))

        self.valueX = QComboBox()
        self.valueX.activated.connect(self.newStepSize)

        self.valueX.addItems([str(i) for i in [0.1, 0.25, 0.4, 0.5, 0.75, 1, 2, 2.5, 4, 5, 7.5, 10]])

        self.toolBar.addWidget(self.valueX)

        self.valueX.setCurrentText("1")

    def newStepSize(self, i):
        self.step = self.manipulatorInterferes.setSpeed(float(self.valueX.itemText(i)))

    def setStepSize(self, i):
        self.valueX.setCurrentText(str(self.stepsDictionary[i]))
        self.loger(self.valueX.itemText(i))
        self.manipulatorInterferes.setSpeed(float(self.stepsDictionary[i]))
