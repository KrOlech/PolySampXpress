from ctypes import LittleEndianStructure, c_double, c_uint


class Calibration(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('A', c_double),
        ('MicrostepMode', c_uint)
    ]
