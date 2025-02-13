from Python.Utilitis.GenericProgressClass import GenericProgressClass
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import image_sharpness, image_sharpness2, sobel, \
    fft_based_sharpness, scharr_variance, edge_based_sharpness, lpc_based_sharpness

class SharpnessCalculationConfig(GenericProgressClass):

    funTab = [image_sharpness, image_sharpness2, sobel, fft_based_sharpness, scharr_variance, edge_based_sharpness,
            lpc_based_sharpness]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.steps = self.createQSpinBoxInt(100)
        self.focusStep = self.createQSpinBoxInt(1, 1, 100)
        self.focusCenter = self.createQSpinBoxInt(2035, -8000, 8000)

        self.form.addRow("Steps", self.steps)
        self.form.addRow("Step Size", self.focusStep)
        self.form.addRow("Focus Around", self.focusCenter)

        self.checkBoxTab = []

        for fun in self.funTab:
            self.checkBoxTab.append(self.createCheckBox())
            self.form.addRow(fun.__name__, self.checkBoxTab[-1])

        self.finaliseGUI()

    def end(self):
        self.accept()

    def okPressed(self):
        self.steps.setDisabled(True)
        self.focusStep.setDisabled(True)
        self.focusCenter.setDisabled(True)

        self.master.SzarpnesCalculator.factors = []

        for chBox, fun in zip(self.checkBoxTab, self.funTab):
            chBox.setDisabled(True)
            if chBox.isChecked():
                self.master.SzarpnesCalculator.addFactor(fun)



        self.master.SzarpnesCalculator.setParamiters(self.steps.value(),
                                                     self.focusStep.value(),
                                                     self.focusCenter.value())
        self.run()
