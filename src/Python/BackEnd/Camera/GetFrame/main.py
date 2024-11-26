from Python.BackEnd.Camera.GetFrame.GetFrameUSB import GetFrameUSB
from Python.BackEnd.Camera.GetFrame.GetFreamFromCameraProducent import GetFrameFromProducent


class GetFrame(GetFrameFromProducent):
    device = None

    def __init__(self):
        super().__init__()

    #def getFrame(self):
    #    return self.getFrameUSB()
