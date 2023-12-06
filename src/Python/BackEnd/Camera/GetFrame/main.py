from Python.BackEnd.Camera.GetFrame.GetFrameUSB import GetFrameUSB
from Python.BackEnd.Camera.GetFrame.GetFreamFromCameraProducent import GetFrameFromProducent


class GetFrame(GetFrameFromProducent, GetFrameUSB):
    device = None

    def __init__(self):
        self.establishConnection()

        if self.isConnectionEstablished:
            GetFrameFromProducent.__init__(self)
        else:
            GetFrameUSB.__init__(self)

    def getFrame(self):
        if self.isConnectionEstablished:
            return self.getFrameProducent()
        else:
            return self.getFrameUSB()
