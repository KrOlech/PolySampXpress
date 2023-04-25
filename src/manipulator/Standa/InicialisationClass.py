import os
import platform
import sys
from ctypes import create_string_buffer, byref, string_at, c_uint, CDLL, WinDLL, cast, POINTER, c_int

from src.manipulator.Standa.Filds.Calibration import Calibration
from src.manipulator.Standa.Filds.DeviceInformation import DeviceInformation
from src.manipulator.Standa.Filds.EngineSettings import EngineSettings
from src.manipulator.Standa.Filds.Status import StatusFild
from src.utilitis.Logger.Logger import Loger


class StandaManipulatorInicialisation(Loger):
    # Specifies the current directory.
    cur_dir = os.path.abspath(os.path.dirname(__file__))

    # Formation of the directory name with all dependencies.
    ximc_dir = os.path.join(cur_dir, "..", "..", "..", "ximc")

    # Formation of the directory name with python dependencies.
    ximc_package_dir = os.path.join(ximc_dir, "crossplatform", "wrappers", "python")

    # add pyximc.py wrapper to python path
    sys.path.append(ximc_package_dir)

    user_name = "root"
    key_esc = "esc"

    @property
    def ok(self):
        return 0

    @property
    def error(self):
        return -1

    @property
    def not_implemented(self):
        return -2

    @property
    def value_error(self):
        return -3

    @property
    def no_device(self):
        return -4

    def __init__(self):
        self.__checkSystem()

        self.eng = EngineSettings()

        user_unit = Calibration()
        user_unit.A = 1
        user_unit.MicrostepMode = self.eng.MicrostepMode

        self.lib = self.__readSharedLib()

        self.enter()

    def getLibVer(self):
        sbuf = create_string_buffer(64)
        self.lib.ximc_version(sbuf)
        self.loger("library version: " + sbuf.raw.decode().rstrip("\0"))
        return sbuf.raw.decode().rstrip("\0")

    def enter(self):
        try:
            self.device_id = self.lib.open_device("xi-com:\\\.\COM3".encode())
        except Exception as e:
            self.loger(e)
            self.loger("error Trying opening new Manipulator")
            return None
        else:
            self.__test_info()
            self.__test_serial(self.device_id)

            return self

    def close(self):
        if self.device_id:
            self.lib.close_device(byref(cast(self.device_id, POINTER(c_int))))
            self.loger("Done")
        else:
            self.logError("Erore alredi Closed")

    def __checkSystem(self):
        if platform.system() == "Windows":
            libDir = r"C:\Users\user\KrzysztofOlech\Magisterkav2\Standa_Motor_Driver_Documentation\examples\test_Python\extendtest\..\..\..\ximc\win64"
            if sys.version_info >= (3, 8):
                os.add_dll_directory(libDir)
            else:
                os.environ["Path"] = libDir + ";" + os.environ["Path"]
        else:
            raise SystemError

    @staticmethod
    def resolvWindowsArchitecture():
        return "win64" if "64" in platform.architecture()[0] else "win32"

    @staticmethod
    def __readSharedLib():
        if platform.system() == "Linux":
            return CDLL("libximc.so")
        elif platform.system() == "FreeBSD":
            return CDLL("libximc.so")
        elif platform.system() == "Darwin":
            return CDLL("libximc.framework/self.libximc")
        elif platform.system() == "Windows":
            if sys.version_info[0] == 3 and sys.version_info[0] >= 8:
                return WinDLL("libximc.dll", winmode=os.RTLD_GLOBAL)
            else:
                return WinDLL("libximc.dll")
        else:
            return None

    def __test_info(self):
        self.loger("\nGet device info")
        x_device_information = DeviceInformation()

        result = self.lib.get_device_information(self.device_id, byref(x_device_information))
        self.loger("Result: " + repr(result))
        if result == self.ok:
            self.loger("Device information:")
            self.loger(" Manufacturer: " + repr(string_at(x_device_information.Manufacturer).decode()))
            self.loger(" Hardware version: " + repr(x_device_information.Major) + "." + repr(
                x_device_information.Minor) + "." + repr(x_device_information.Release))

    def __test_status(self, device_id):

        """
        A function of reading status information from the device

        You can use this function to get basic information about the device status.

        :param self.lib: structure for accessing the functionality of the self.libximc self.library.
        :param device_id:  device id.
        """

        self.loger("\nGet status")
        x_status = StatusFild()
        result = self.lib.get_status(device_id, byref(x_status))
        self.loger("Result: " + repr(result))
        if result == self.ok:
            self.loger("Status.Ipwr: " + repr(x_status.Ipwr))
            self.loger("Status.Upwr: " + repr(x_status.Upwr))
            self.loger("Status.Iusb: " + repr(x_status.Iusb))
            self.loger("Status.Flags: " + repr(hex(x_status.Flags)))

    def __test_serial(self, device_id):
        """
        Reading the device's serial number.

        :param self.lib: structure for accessing the functionality of the self.libximc self.library.
        :param device_id: device id.
        """

        # self.loger("\nReading serial")
        x_serial = c_uint()
        result = self.lib.get_serial_number(device_id, byref(x_serial))
        if result == self.ok:
            self.loger(" Serial: " + repr(x_serial.value))
