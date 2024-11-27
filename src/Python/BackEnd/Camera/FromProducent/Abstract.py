from ctypes import c_int, Structure, c_char_p, c_void_p, POINTER, c_long, windll

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
import ctypes

import tisgrabber as tis


class AbstractCameraFromProducent:
    __isConnectionEstablished = None

    def __init__(self, *args, **kwargs):
        self.ic = windll.LoadLibrary(JsonHandling.getFileLocation(r"CameraDLL\tisgrabber_x64.dll"))

        tis.declareFunctions(self.ic)

        self.ic.IC_InitLibrary(0)

    def establishConnection(self):
        self.ic.IC_InitLibrary(0)

        self.handle = self.ic.IC_CreateGrabber()

        self.ic.IC_OpenVideoCaptureDevice(self.handle, tis.T("DFK 37BUX178"))

        self.__isConnectionEstablished = self.ic.IC_IsDevValid(self.handle)

        return self.__isConnectionEstablished

    @property
    def isConnectionEstablished(self):
        return self.__isConnectionEstablished
