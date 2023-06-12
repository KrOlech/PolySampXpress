from src.BaseClass.Slider.Slider import Slider


class ManipulatorSlider(Slider):

    def change(self, value):
        self.value = self.conversion(value)
        self.master.x = self.value
        self.master.gotoNotAsync()
