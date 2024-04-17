from ctypes import c_int, Structure, c_char_p, c_void_p, POINTER, c_long, windll

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
import ctypes

import tisgrabber as tis

ic = ctypes.cdll.LoadLibrary("./tisgrabber_x64.dll") #toDo move to class corectli no as global and corect file location

tis.declareFunctions(ic)


class AbstractCameraFromProducent:
    def __init__(self, *args, **kwargs):
        self.ic = ic

        self.ic.IC_InitLibrary(0)

    # tisgrabber = windll.LoadLibrary(JsonHandling.getFileLocation(r"CameraDLL\tisgrabber_x64.dll"))

    class GrabberHandle(Structure):
        pass

    GrabberHandle._fields_ = [('unused', c_int)]

    GrabberHandlePtr = POINTER(GrabberHandle)

    '''
    create_grabber = tisgrabber.IC_CreateGrabber
    create_grabber.restype = GrabberHandlePtr
    create_grabber.argtypes = None

    open_device_by_unique_name = tisgrabber.IC_OpenDevByUniqueName
    open_device_by_unique_name.restype = c_int
    open_device_by_unique_name.argtypes = (GrabberHandlePtr,
                                           c_char_p)

    _OpenVideoCaptureDevice = tisgrabber.IC_OpenVideoCaptureDevice
    _OpenVideoCaptureDevice.restype = c_int
    _OpenVideoCaptureDevice.argtypes = (GrabberHandlePtr,
                                           c_char_p)

    GetImagePtr = tisgrabber.IC_GetImagePtr
    GetImagePtr.restype = c_void_p
    GetImagePtr.argtypes = (GrabberHandlePtr,)

    StartLive = tisgrabber.IC_StartLive
    StartLive.restype = c_int
    StartLive.argtypes = (GrabberHandlePtr,
                          c_int,)

    _GetImageDescription = tisgrabber.IC_GetImageDescription
    _GetImageDescription.restype = c_int
    _GetImageDescription.argtypes = (GrabberHandlePtr,
                                     POINTER(c_long),
                                     POINTER(c_long),
                                     POINTER(c_int),
                                     POINTER(c_int),)

    _SetVideoFormat = tisgrabber.IC_SetVideoFormat
    _SetVideoFormat.restype = c_int
    _SetVideoFormat.argtypes = (GrabberHandlePtr,
                                     c_char_p)

    _IsDevValid = tisgrabber.IC_IsDevValid
    _IsDevValid.restype = c_int
    _IsDevValid.argtypes = (GrabberHandlePtr,)
    '''

    __isConnectionEstablished = None

    def establishConnection(self):
        self.ic.IC_InitLibrary(None)

        self.handle = self.ic.IC_ShowDeviceSelectionDialog(None)

        # self.__isConnectionEstablished = self.open_device_by_unique_name(self.handle, b'DFK 37BUX178 44121122')
        #self.__isConnectionEstablished = self.ic.IC_OpenVideoCaptureDevice(self.handle, b"DFK 37BUX178")
        self.__isConnectionEstablished = self.ic.IC_IsDevValid(self.handle)
        return self.ic.IC_IsDevValid(self.handle)

    @property
    def isConnectionEstablished(self):
        return self.__isConnectionEstablished
