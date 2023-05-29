from ctypes import c_int, Structure, c_char_p, c_void_p, POINTER, c_long, c_ubyte, cast, windll, sizeof, c_uint8


class AbstractCameraFromProducent:
    tisgrabber = windll.LoadLibrary(
        r"C:\Users\Administrator\PycharmProjects\MagisterkaV2\Documentation\Camera\tisgrabber_x64.dll")

    class GrabberHandle(Structure):
        pass

    GrabberHandle._fields_ = [('unused', c_int)]

    GrabberHandlePtr = POINTER(GrabberHandle)

    create_grabber = tisgrabber.IC_CreateGrabber
    create_grabber.restype = GrabberHandlePtr
    create_grabber.argtypes = None

    open_device_by_unique_name = tisgrabber.IC_OpenDevByUniqueName
    open_device_by_unique_name.restype = c_int
    open_device_by_unique_name.argtypes = (GrabberHandlePtr,
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

    def __init__(self):
        self.tisgrabber.IC_InitLibrary(None)

        self.handle = self.create_grabber()

        self.open_device_by_unique_name(self.handle, b'DFK 37BUX178 44121122')
