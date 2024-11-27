

from Python.BaseClass.Slider.Slider import Slider


class SliderCommunicationPoint(Slider):

    def __init__(self, master, cP, *args, **kwargs):
        self.communicationPoint = cP
        super(SliderCommunicationPoint, self).__init__(master, cP.min, cP.max, cP.value, *args, **kwargs)

        self.setFixedWidth(150)

    def change(self, value) -> None:
        self.value = self.conversion(value)
        self.communicationPoint.value = self.value
        self.master.camera.setNewValueForCommunicationPoint(self.communicationPoint)



