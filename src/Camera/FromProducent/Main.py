from ctypes import c_int, Structure, c_char_p, c_void_p, POINTER, c_long, c_ubyte, cast, windll, sizeof, c_uint8

import numpy as np

from src.Camera.FromProducent.Abstract import AbstractCameraFromProducent
from src.Camera.GetFrame.AbstractGetFream import AbstractGetFrame


class GetFrameFromProducent(AbstractGetFrame, AbstractCameraFromProducent):

    def __init__(self):
        super().__init__()

        self.StartLive(self.handle, 1)


        self.BildDaten = self.GetImageDescription()[:3]
        self.lWidth = self.BildDaten[0]
        self.lHeight = self.BildDaten[1]
        self.iBitsPerPixel = self.BildDaten[2] / 8

        self.bufferSize = int(self.lWidth * self.lHeight * self.iBitsPerPixel * sizeof(c_uint8))

    def setWhiteBalanceAuto(self):
        self.tisgrabber.IC_SetWhiteBalanceAuto(self.handle, 1)

    def GetImageDescription(self):
        lWidth = c_long()
        lHeight = c_long()
        iBitsPerPixel = c_int()
        COLORFORMAT = c_int()

        Error = self._GetImageDescription(self.handle, lWidth, lHeight, iBitsPerPixel, COLORFORMAT)

        return (lWidth.value, lHeight.value, iBitsPerPixel.value, COLORFORMAT.value)

    def getImagePointer(self):
        return self.GetImagePtr(self.handle)

    def getFrame(self):
        imagePointer = self.getImagePointer()

        Bild = cast(imagePointer, POINTER(c_ubyte * self.bufferSize))

        print(Bild.contents)

        img = np.frombuffer(buffer=Bild.contents,
                            dtype=np.uint8)

        # img = np.ndarray(buffer=Bild.contents,
        #                 dtype=np.uint8,
        #                 shape=(lHeight,
        #                        lWidth,
        #                        iBitsPerPixel))
        return img


    def StopLive(self):
        Error = self.tisgrabber.IC_StopLive(self.handle)
        return Error

if __name__ == "__main__":
    t = GetFrameFromProducent()

    for x in range(100000):
        print(x)

    t.setWhiteBalanceAuto()

    for x in range(1000000):
        print(x)

    x = t.StopLive()
