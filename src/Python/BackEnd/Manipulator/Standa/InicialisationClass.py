import os
import platform
import sys
from ctypes import create_string_buffer, byref, string_at, c_uint, CDLL, cast, POINTER, c_int

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BackEnd.Manipulator.Standa.Filds.DeviceInformation import DeviceInformation
from Python.BackEnd.Manipulator.Standa.Filds.Status import StatusFild
from Python.BackEnd.Manipulator.Standa.Abstract.AbstractStandaManipulator import AbstractStandaManipulator
from Python.BackEnd.Manipulator.Standa.Filds.Calibration import Calibration

from Python.BackEnd.Manipulator.Standa.Filds.EngineSettings import EngineSettings


class StandaManipulatorInitialisation(AbstractStandaManipulator):
    manipulatorConnected = False

    @property
    def ZoomStepsMap(self):
        return {0.85: 0, 1: -35, 2: -190, 3: -280, 4: -335, 5: -355, 6: -425, 7: -455, 8: -485, 9: -505, 10: -525}

    @property
    def StepZoomsMap(self):
        return {0: 0.85, -35: 1, -190: 2, -280: 3, -335: 4, -355: 5, -425: 6, -455: 7, -485: 8, -505: 9, -525: 10}

    def __init__(self, device_id_Address, screenSize, *args, **kwargs):
        super().__init__(screenSize, *args, **kwargs)
        self.__checkSystem()

        self.eng = EngineSettings()

        user_unit = Calibration()
        user_unit.A = 1
        user_unit.MicrostepMode = self.eng.MicrostepMode

        self.lib = self.__readSharedLib()

        self.device_id = self.enter(device_id_Address)

    def getLibVer(self):
        sbuf = create_string_buffer(64)
        self.lib.ximc_version(sbuf)
        self.loger("library version: " + sbuf.raw.decode().rstrip("\0"))
        return sbuf.raw.decode().rstrip("\0")

    def enter(self, encodedComPort):
        try:
            device_id = self.lib.open_device(encodedComPort)
            self.loger(f"Device ID {device_id}")
            self.__testInfo(device_id)
            self.__testSerial(device_id)
            return device_id
        except Exception as e:
            self.loger(e)
            self.loger(f"error Trying opening device: {encodedComPort.decode()}")

    def close(self):
        self.saveFile(f"StandaPosition_{self.device_id}.json", {"x": self.x, "y": self.y, "z": self.z})
        self.closeDevice(self.device_id)
        self.loger("Done Closing Standa")

    def closeDevice(self, device_id):
        if device_id:
            self.lib.close_device(byref(cast(device_id, POINTER(c_int))))
            self.manipulatorConnected = False
        else:
            self.logError("Erore Closing Standa")

    def __checkSystem(self):
        if platform.system() == "Windows":
            libDir = JsonHandling.getFileLocation("win64-Standa")
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
            from ctypes import WinDLL
            if sys.version_info[0] == 3 and sys.version_info[0] >= 8:
                return WinDLL("libximc.dll", winmode=os.RTLD_GLOBAL)
            else:
                return WinDLL("libximc.dll")
        else:
            return None

    # todo better name
    def __testInfo(self, device_id):
        x_device_information = DeviceInformation()
        result = self.lib.get_device_information(device_id, byref(x_device_information))
        self.loger("Result: " + repr(result))
        if result == self.ok:
            self.loger("Device information:")
            self.loger(" Manufacturer: " + repr(string_at(x_device_information.Manufacturer).decode()))
            self.loger(" Hardware version: " + repr(x_device_information.Major) + "." + repr(
                x_device_information.Minor) + "." + repr(x_device_information.Release))
            self.manipulatorConnected = True

    def __testStatus(self, device_id):

        """
        A function of reading status information from the device

        You can use this function to get basic information about the device status.

        :param self.lib: structure for accessing the functionality of the self.libximc self.library.
        :param device_id:  device id.
        """

        self.loger("Get status")
        x_status = StatusFild()
        result = self.lib.get_status(device_id, byref(x_status))
        self.loger("Result: " + repr(result))
        if result == self.ok:
            self.loger("Status.Ipwr: " + repr(x_status.Ipwr))
            self.loger("Status.Upwr: " + repr(x_status.Upwr))
            self.loger("Status.Iusb: " + repr(x_status.Iusb))
            self.loger("Status.Flags: " + repr(hex(x_status.Flags)))

    def __testSerial(self, device_id):
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
