from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class WorkFaldLabel(QWidget):
    scalaX, scalaY = JsonHandling.readRoiLabelScalles()  # todo check if from correct value tipe it is read

    def __init__(self, workFildParams, gui, screenSize, *args, **kwargs):
        super(WorkFaldLabel, self).__init__(*args, **kwargs)

        self.x = screenSize.width() // self.scalaX
        self.y = screenSize.height() // self.scalaY

        self.workFildParams = workFildParams
        self.gui = gui

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton(self)
        self.button.setMaximumSize(self.x, self.y)
        self.button.setMinimumSize(self.x, self.y)
        self.button.released.connect(self.trigger)
        self.layout.addWidget(self.button)

        self.nameLabel = QLabel(workFildParams[-1], self)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.move(self.x // 2 - self.nameLabel.size().width() // 2, self.y // 2 - 40)

        self.xLabel = QLabel(f"X:{workFildParams[0]}mm->{workFildParams[1]}mm", self)
        self.xLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xLabel.move(self.x // 2 - self.xLabel.size().width() // 2, self.y // 2 - 20)

        self.yLabel = QLabel(f"Y:{workFildParams[2]}mm->{workFildParams[3]}mm   ", self)
        self.yLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yLabel.move(self.x // 2 - self.yLabel.size().width() // 2, self.y // 2)

        self.setLayout(self.layout)

        self.setMaximumSize(self.x, self.y)
        self.setMinimumSize(self.x, self.y)

    def trigger(self):
        self.gui.setFildParams(self.workFildParams)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = WorkFaldLabel([25.0, 30.0, 25.0, 14.0, 'pole 2'], app)

    window.show()

    app.exec_()
