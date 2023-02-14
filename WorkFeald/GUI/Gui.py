from PySide2.QtWidgets import QHBoxLayout, QDialog
from WorkFeald.Label.Label import WorkFaldLabel


class WorkFilledGui(QDialog):  # toDo Common taskbar
    valueSet = False
    fildParameters = None

    def __init__(self, workFields, windowSize, *args, **kwargs):
        super(WorkFilledGui, self).__init__(*args, **kwargs)

        self.fildLabels = [WorkFaldLabel(workField, self, windowSize) for workField in workFields]

        self.layout = QHBoxLayout(self)

        [self.layout.addWidget(label) for label in self.fildLabels]

    def setFildParams(self, fildParams):
        self.hide()
        self.valueSet = True
        self.fildParameters = fildParams


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    from utilitis.JsonRead.JsonRead import loadPolaRoboczeJson

    app = QApplication(sys.argv)

    window = WorkFilledGui(loadPolaRoboczeJson())

    window.show()

    app.exec_()
