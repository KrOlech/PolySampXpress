from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDialog
from MAP.GUI.PoleLabel import PoleLabel



class PoleRoboczeGui(QDialog):
    walueSet = False
    fildParamiters = None

    def __init__(self,workFields,*args, **kwargs):
        super(PoleRoboczeGui, self).__init__(*args, **kwargs)

        self.fildLabels = [PoleLabel(workField,self) for workField in workFields]

        self.layout = QHBoxLayout(self)

        [self.layout.addWidget(label) for label in self.fildLabels]


    def setFildParams(self,fildParams):
        self.hide()
        self.walueSet = True
        self.fildParamiters = fildParams

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from utilitis.JsonRead.JsonRead import loadPolaRoboczeJson

    app = QApplication(sys.argv)

    window = PoleRoboczeGui(loadPolaRoboczeJson())

    window.show()

    app.exec_()