from ctypes import WinDLL, c_char_p, c_int, c_void_p, c_double

from manipulator.SCIIPPlus.DllFuntionWraper.DllFunctionNames import DllFunctionNames
from manipulator.SCIIPPlus.DllFuntionWraper.dllFunctionWrapper import DllFunctionWrapper


class DllFunction(DllFunctionNames):

    def __init__(self):
        self.dll = WinDLL(r"C:\Windows\System32\ACSCL_x64.dll")

        self.__createOpenCommEthernetTCP()

        self.__createOpenCommEthernetUDP()

        self.__createOpenCommSimulator()
        self.__createCloseSimulator()

    def __createClearBuffer(self):
        self.__OpenCommEthernetTCP = DllFunctionWrapper(self.clearBufferName, self.dll,
                                                        (c_void_p, c_int, c_int, c_int, c_void_p), c_int)

    def clearBuffer(self, Handle, Buffer, FromLine, ToLine, Wait):
        # HANDLE Handle, int Buffer, int FromLine, int ToLine, ACSC_WAITBLOCK* Wait
        # HANDLE - c_void_p - c_int
        # ACSC_WAITBLOCK - struct:
        # HANDLE Event;				//signal event
        # int Ret;					//code of return

        return self.__OpenCommEthernetTCP(Handle, Buffer, FromLine, ToLine, Wait)  # TODo Validator if needed

    def __createOpenCommEthernetTCP(self):
        self.__OpenCommEthernetTCP = DllFunctionWrapper(self.openCommEthernetTCPName, self.dll, (c_char_p, c_int),
                                                        c_void_p)

    def OpenCommEthernetTCP(self, IP, port):
        return self.__OpenCommEthernetTCP(*self.__validateIPAndPort(IP, port))

    def __createOpenCommEthernetUDP(self):
        self.__OpenCommEthernetUDP = DllFunctionWrapper(self.openCommEthernetUDPName, self.dll, (c_char_p, c_int),
                                                        c_void_p)

    def OpenCommEthernetUDP(self, IP, port):
        return self.__OpenCommEthernetUDP(*self.__validateIPAndPort(IP, port))

    def __createOpenCommSimulator(self):
        self.__OpenCommSimulator = DllFunctionWrapper(self.openCommSimulatorName, self.dll, (), c_void_p)

    def OpenCommSimulator(self):
        return self.__OpenCommSimulator()

    def __createCloseSimulator(self):
        self.__CloseSimulator = DllFunctionWrapper(self.closeSimulatorName, self.dll, (), c_int)

    def closeSimulator(self):
        return self.__CloseSimulator()

    def __createInstallCallback(self):
        self.__InstallCallback = DllFunctionWrapper(self.closeSimulatorName, self.dll, (c_void_p, int, c_int,), c_int)

    def installCallback(self, hCom, calbacFun, preciseTimer, acscIntr):
        return self.__InstallCallback(hCom, calbacFun, preciseTimer, acscIntr)

    def  __creatAcscToPoint(self):

        self.__CloseSimulator = DllFunctionWrapper(self.ToPointName, self.dll, (c_void_p, c_int, c_int, c_double, c_void_p), c_int)



    @staticmethod
    def __validateIPAndPort(IP, port):
        if not isinstance(IP, c_char_p):
            IP = c_char_p(IP)

        if not isinstance(port, c_int):
            port = c_int(port)

        return IP, port
