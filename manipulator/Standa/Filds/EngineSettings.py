from _ctypes import Structure
from ctypes import c_uint, c_int


class EngineSettings(Structure):
    _fields_ = [
        ("NomVoltage", c_uint),
        ("NomCurrent", c_uint),
        ("NomSpeed", c_uint),
        ("uNomSpeed", c_uint),
        ("EngineFlags", c_uint),
        ("Antiplay", c_int),
        ("MicrostepMode", c_uint),
        ("StepsPerRev", c_uint),
    ]
