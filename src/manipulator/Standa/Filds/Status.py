from ctypes import Structure, c_uint, c_int, c_longlong


class StatusFild(Structure):
    _fields_ = [
        ("MoveSts", c_uint),
        ("MvCmdSts", c_uint),
        ("PWRSts", c_uint),
        ("EncSts", c_uint),
        ("WindSts", c_uint),
        ("CurPosition", c_int),
        ("uCurPosition", c_int),
        ("EncPosition", c_longlong),
        ("CurSpeed", c_int),
        ("uCurSpeed", c_int),
        ("Ipwr", c_int),
        ("Upwr", c_int),
        ("Iusb", c_int),
        ("Uusb", c_int),
        ("CurT", c_int),
        ("Flags", c_uint),
        ("GPIOFlags", c_uint),
        ("CmdBufFreeSpace", c_uint),
    ]
