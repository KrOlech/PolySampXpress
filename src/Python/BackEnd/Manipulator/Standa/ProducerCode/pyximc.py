from ctypes import *
import platform
import sys
from src.Python.BackEnd.Manipulator.Standa.ProducerCode.FildsClass import device_enumeration_t


def ximc_shared_lib():
    if platform.system() == "Linux":
        return CDLL("libximc.so")
    elif platform.system() == "FreeBSD":
        return CDLL("libximc.so")
    elif platform.system() == "Darwin":
        return CDLL("libximc.framework/libximc")
    elif platform.system() == "Windows":
        if sys.version_info[0] == 3 and sys.version_info[0] >= 8:
            return WinDLL("libximc.dll", winmode=RTLD_GLOBAL)
        else:
            return WinDLL("libximc.dll")
    else:
        return None


if __name__ == "__main__":
    lib = ximc_shared_lib()

    lib.enumerate_devices.restype = POINTER(device_enumeration_t)
    lib.get_device_name.restype = c_char_p

