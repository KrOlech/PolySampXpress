import ctypes
from ctypes import c_int, POINTER, c_long, c_ubyte, cast, sizeof, c_uint8

import cv2
from pygetwindow import getWindowsWithTitle
from numpy import ndarray, uint8

from Python.BackEnd.Camera.FromProducent.Abstract import AbstractCameraFromProducent
from Python.BackEnd.Camera.GetFrame.AbstractGetFream import AbstractGetFrame
import tisgrabber as tis


class GetFrameFromProducent(AbstractGetFrame, AbstractCameraFromProducent):

    def __init__(self):
        super().__init__(self)

        if not self.isConnectionEstablished:
            self.loger(f"Conection to Camera from Producent {self.establishConnection()}:")

        self.setVideoFormat()

        self.StartLive()

        self.lWidth, self.lHeight, self.iBitsPerPixel, _ = self.GetImageDescription()

        self.bufferSize = self.lWidth * self.lHeight * self.iBitsPerPixel * sizeof(c_uint8)

        self.shape = (self.lHeight, self.lWidth, self.iBitsPerPixel)
        self.loger(self.shape)

    def setWhiteBalanceAuto(self):
        self.ic.IC_SetWhiteBalanceAuto(self.handle, 1)

    def GetImageDescription(self):
        lWidth = c_long()
        lHeight = c_long()
        iBitsPerPixel = c_int()
        COLORFORMAT = c_int()

        Error = self.ic.IC_GetImageDescription(self.handle, lWidth, lHeight, iBitsPerPixel, COLORFORMAT)

        return (lWidth.value, lHeight.value, iBitsPerPixel.value // 8, COLORFORMAT.value)

    def setVideoFormat(self):
        Error = None
        if (self.ic.IC_IsDevValid(self.handle)):
            Error = self.ic.IC_SetVideoFormat(self.handle, tis.T("RGB64 (1536x1016) [Binning 2x]"))

        self.loger(f"ustawienie formatu Wideo res: {Error}")

    def getImagePointer(self):
        return self.ic.IC_GetImagePtr(self.handle)

    def getFrameProducent(self):
        self.SnapImage()
        imagePointer = self.getImagePointer()

        Bild = cast(imagePointer, POINTER(c_ubyte * self.bufferSize))

        img = ndarray(buffer=Bild.contents,
                      dtype=uint8,
                      shape=self.shape)

        # return cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
        return img

    def getFrame(self) -> ndarray:
        return self.getFrameProducent()

    def StopLive(self):
        Error = self.ic.IC_StopLive(self.handle)
        return Error

    def PrepareLive(self):
        self.ic.IC_PrepareLive(self.handle)

    def SuspendLive(self):
        self.ic.IC_SuspendLive(self.handle)

    def GetPropertyMapString(self):
        self.ic.IC_GetPropertyMapString(self.handle)

    def StartLive(self):
        try:
            Error = self.ic.IC_StartLive(self.handle, 1)
            win = getWindowsWithTitle('ActiveMovie Window')[0]
            win.close()
        except IndexError as e:
            self.logError(e)
            self.loger("no window to close?")

        return Error

    def SnapImage(self):
        self.ic.IC_SnapImage(self.handle, 2000)


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
