import tisgrabber as tis
import platform
from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class AbstractCameraFromProducent:
    __isConnectionEstablished = None
    linux = False

    def __init__(self, *args, **kwargs):
        if platform.system() == "Windows":
            from ctypes import windll

            self.ic = windll.LoadLibrary(JsonHandling.getFileLocation(r"CameraDLL\tisgrabber_x64.dll"))

            tis.declareFunctions(self.ic)

            self.ic.IC_InitLibrary(0)
        else:
            self.linux = True
            self.__isConnectionEstablished = False

    def establishConnection(self):
        self.ic.IC_InitLibrary(0)

        self.handle = self.ic.IC_CreateGrabber()

        self.ic.IC_OpenVideoCaptureDevice(self.handle, tis.T("DFK 37BUX178"))

        self.__isConnectionEstablished = self.ic.IC_IsDevValid(self.handle)

        return self.__isConnectionEstablished

    @property
    def isConnectionEstablished(self):
        return self.__isConnectionEstablished
