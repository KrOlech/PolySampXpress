from ctypes import c_int, POINTER, c_long, c_ubyte, cast, sizeof, c_uint8

from pygetwindow import getWindowsWithTitle
from numpy import ndarray, uint8

from src.Python.BackEnd.Camera.FromProducent.Abstract import AbstractCameraFromProducent
from src.Python.BackEnd.Camera.GetFrame.AbstractGetFream import AbstractGetFrame


class GetFrameFromProducent(AbstractGetFrame, AbstractCameraFromProducent):

    def __init__(self):
        if not self.isConnectionEstablished:
            self.establishConnection()

        self.StartLive()

        self.lWidth, self.lHeight, self.iBitsPerPixel, _ = self.GetImageDescription()

        self.bufferSize = self.lWidth * self.lHeight * self.iBitsPerPixel * sizeof(c_uint8)

        self.shape = (self.lHeight, self.lWidth, self.iBitsPerPixel)

    def setWhiteBalanceAuto(self):
        self.tisgrabber.IC_SetWhiteBalanceAuto(self.handle, 1)

    def GetImageDescription(self):
        lWidth = c_long()
        lHeight = c_long()
        iBitsPerPixel = c_int()
        COLORFORMAT = c_int()

        Error = self._GetImageDescription(self.handle, lWidth, lHeight, iBitsPerPixel, COLORFORMAT)

        return (lWidth.value, lHeight.value, iBitsPerPixel.value // 8, COLORFORMAT.value)

    def getImagePointer(self):
        return self.GetImagePtr(self.handle)

    def getFrameProducent(self):
        self.SnapImage()
        imagePointer = self.getImagePointer()

        Bild = cast(imagePointer, POINTER(c_ubyte * self.bufferSize))

        img = ndarray(buffer=Bild.contents,
                      dtype=uint8,
                      shape=self.shape)
        return img

    def getFrame(self) -> ndarray:
        return self.getFrameProducent()

    def StopLive(self):
        Error = self.tisgrabber.IC_StopLive(self.handle)
        return Error

    def PrepareLive(self):
        self.tisgrabber.IC_PrepareLive(self.handle)

    def SuspendLive(self):
        self.tisgrabber.IC_SuspendLive(self.handle)

    def GetPropertyMapString(self):
        self.tisgrabber.IC_GetPropertyMapString(self.handle)

    def StartLive(self):
        Error = self.tisgrabber.IC_StartLive(self.handle, 1)
        win = getWindowsWithTitle('ActiveMovie Window')[0]
        win.close()

        return Error

    def SnapImage(self):
        self.tisgrabber.IC_SnapImage(self.handle, 2000)


if __name__ == "__main__":
    t = GetFrameFromProducent()

    # t.PrepareLive()

    # t.StartLive()

    for x in range(100000):
        print(t.getFrame())

    # for x in range(100):
    #    t.getFrame()

    print(t.getFrame())

    t.StopLive()
