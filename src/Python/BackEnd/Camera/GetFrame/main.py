from Python.BackEnd.Camera.GetFrame.GetFrameUSB import GetFrameUSB
from Python.BackEnd.Camera.GetFrame.GetFreamFromCameraProducent import GetFrameFromProducent


class GetFrame(GetFrameUSB, GetFrameFromProducent):
    device = None

    FrameFun = None

    def __init__(self):
        super().__init__()

        try:
            self.getFrameProducent()
        except Exception as e:
            self.loger(e)
            self.FrameFun = self.getFrameUSB
        else:
            self.FrameFun = self.getFrameProducent

    def getFrame(self):
        return self.FrameFun()
