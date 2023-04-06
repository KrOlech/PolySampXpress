from ctypes import WinDLL, c_char_p, c_int, c_void_p, c_double, c_int, byref

from manipulator.SCIIPPlus.DllFuntionWraper.DllFunctionNames import DllFunctionNames
from manipulator.SCIIPPlus.DllFuntionWraper.dllFunctionWrapper import DllFunctionWrapper


class DllFunction(DllFunctionNames):

    def __init__(self):
        self.dll = WinDLL(r"C:\Windows\System32\ACSCL_x64.dll")

        self.__createOpenCommEthernetTCP()

        self.__createOpenCommEthernetUDP()

        self.__createOpenCommSimulator()
        self.__createCloseSimulator()

        # self.__createInstallCallback()

        self.__createToPoint()
        self.__createToPointM()

        self.__createBreak()
        self.__createBreakM()

        self.__createExtToPoint()
        self.__createExtToPointM()

        self.__createGetAxesCount()

        self.__createStartSpiiPlusSC()
        self.__createStopSpiiPlusSC()

        self.__createGetFPosition()

        self.__createEnable()
        self.__createDisable()

        self.__createEnableM()
        self.__createDisableM()

        self.__createGo()
        self.__createGoM()

        self.__createReadReal()

        self.__createSysInfo()

        self.__createWaitMotorEnable()

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

    def __createToPoint(self):
        # HANDLE Handle, int Flags, int Axis, double Point, ACSC_WAITBLOCK* Wait
        self.__ToPoint = DllFunctionWrapper(self.toPointName, self.dll,
                                            (c_void_p, c_int, c_int, c_double, c_void_p), c_int)

    def ToPoint(self, Handle, Flags, Axis, Point, Wait):
        return self.__ToPoint(Handle, Flags, Axis, Point, Wait)

    def __createToPointM(self):
        # HANDLE Handle, int Flags, int* Axes, double* Point, ACSC_WAITBLOCK* Wait
        self.__ToPointM = DllFunctionWrapper(self.toPointMName, self.dll,
                                             (c_void_p, c_int, c_void_p, c_void_p, c_void_p), c_int)

    def ToPointM(self, Handle, Flags, Axis, Point, Wait):
        axisTab = c_int * len(Axis)
        filledAxisTab = axisTab(*Axis)

        pointTab = c_double * len(Point)
        filledPointTab = pointTab(*Point)

        return self.__ToPointM(Handle, Flags, byref(filledAxisTab), byref(filledPointTab), Wait)

    def __createBreak(self):
        # HANDLE Handle, int Axis, ACSC_WAITBLOCK* Wait
        self.__break = DllFunctionWrapper(self.breakName, self.dll,
                                          (c_void_p, c_int, c_void_p), c_int)

    def breakF(self, Handle, Axis, Wait):
        return self.__break(Handle, Axis, Wait)

    def __createBreakM(self):
        # HANDLE Handle, int* Axes, ACSC_WAITBLOCK* Wait
        self.__breakM = DllFunctionWrapper(self.breakMName, self.dll,
                                           (c_void_p, c_void_p, c_void_p), c_int)

    def breakMF(self, Handle, Axis, Wait):
        axisTab = c_int * len(Axis)
        axisTab = axisTab(*Axis)
        return self.__breakM(Handle, byref(axisTab), Wait)

    def __createExtToPoint(self):
        # HANDLE Handle, int Flags, int Axis, double Point, double Velocity, double EndVelocity, ACSC_WAITBLOCK* Wait
        self.__ExtToPoint = DllFunctionWrapper(self.extToPointName, self.dll,
                                               (c_void_p, c_int, c_int, c_double, c_double, c_double, c_void_p), c_int)

    def ExtToPoint(self, Handle, Flags, Axis, Point, Velocity, EndVelocity, Wait):
        return self.__ExtToPoint(Handle, Flags, Axis, Point, Velocity, EndVelocity, Wait)

    def __createExtToPointM(self):
        # HANDLE Handle, int Flags, int* Axes, double* Point, double Velocity, double EndVelocity, ACSC_WAITBLOCK* Wait
        self.__ExtToPointM = DllFunctionWrapper(self.extToPointMName, self.dll,
                                                (c_void_p, c_int, c_void_p, c_void_p, c_double, c_double, c_void_p),
                                                c_int)

    def ExtToPointM(self, Handle, Flags, Axis, Point, Velocity, EndVelocity, Wait):
        axisTab = c_int * len(Axis)
        filledAxisTab = axisTab(*Axis)

        pointTab = c_double * len(Point)
        filledPointTab = pointTab(*Point)

        return self.__ExtToPointM(Handle, Flags, byref(filledAxisTab), byref(filledPointTab), Velocity, EndVelocity,
                                  Wait)

    def __createGetAxesCount(self):
        # HANDLE Handle, int Flags, int* Axes, double* Point, double Velocity, double EndVelocity, ACSC_WAITBLOCK* Wait
        self.__getAxesCount = DllFunctionWrapper(self.getAxesCountName, self.dll,
                                                 (c_void_p, c_void_p, c_void_p),
                                                 c_int)

    def getAxesCount(self, Handle, Wait):
        buffer = c_void_p()

        print(self.__getAxesCount(Handle, byref(buffer), Wait))
        return buffer

    def __createStartSpiiPlusSC(self):
        self.__StartSpiiPlus = DllFunctionWrapper(self.StartSPiiPlusSCName, self.dll, (), c_int)

    def startSpiiPlusSC(self):
        return self.__StartSpiiPlus()

    def __createStopSpiiPlusSC(self):
        self.__StopSpiiPlus = DllFunctionWrapper(self.StopSPiiPlusSCName, self.dll, (), c_int)

    def stopSpiiPlusSC(self):
        return self.__StopSpiiPlus()

    def __createGetFPosition(self):
        # HANDLE Handle, int Axis, double* FPosition, ACSC_WAITBLOCK* Wait
        self.__getFPosition = DllFunctionWrapper(self.getFPositionName, self.dll, (c_void_p, c_int, c_void_p, c_void_p),
                                                 c_int)

    def getFPosition(self, Handle, Axis, Wait):
        buffer = c_void_p()

        print(self.__getFPosition(Handle, Axis, byref(buffer), Wait))
        return buffer

    def __createEnable(self):
        # HANDLE Handle, int Axis, ACSC_WAITBLOCK* Wait
        self.__enable = DllFunctionWrapper(self.enableName, self.dll, (c_void_p, c_int, c_void_p), c_int)

    def enable(self, Handle, Axis, Wait):
        return self.__enable(Handle, Axis, Wait)

    def __createEnableM(self):
        # HANDLE Handle, int* Axes, ACSC_WAITBLOCK* Wait
        self.__enableM = DllFunctionWrapper(self.enableMName, self.dll, (c_void_p, c_void_p, c_void_p), c_int)

    def enableM(self, Handle, Axis, Wait):
        axisTab = c_double * len(Axis)
        filledAxisTab = axisTab(*Axis)

        return self.__enableM(Handle, byref(filledAxisTab), Wait)

    def __createDisable(self):
        # HANDLE Handle, int Axis, ACSC_WAITBLOCK* Wait
        self.__disable = DllFunctionWrapper(self.disableName, self.dll, (c_void_p, c_int, c_void_p), c_int)

    def disable(self, Handle, Axis, Wait):
        return self.__disable(Handle, Axis, Wait)

    def __createDisableM(self):
        # HANDLE Handle, int* Axes, ACSC_WAITBLOCK* Wait
        self.__disableM = DllFunctionWrapper(self.disableMName, self.dll, (c_void_p, c_void_p, c_void_p), c_int)

    def disableM(self, Handle, Axis, Wait):
        axisTab = c_double * len(Axis)
        filledAxisTab = axisTab(*Axis)

        return self.__disableM(Handle, byref(filledAxisTab), Wait)

    def __createGo(self):
        self.__go = DllFunctionWrapper(self.goName, self.dll, (c_void_p, c_int, c_void_p), c_int)

    def Go(self, Handle, Axis, Wait):
        return self.__go(Handle, Axis, Wait)

    def __createGoM(self):
        self.__goM = DllFunctionWrapper(self.goMName, self.dll, (c_void_p, c_void_p, c_void_p), c_int)

    def GoM(self, Handle, Axis, Wait):
        axisTab = c_double * len(Axis)
        filledAxisTab = axisTab(*Axis)

        return self.__goM(Handle, byref(filledAxisTab), Wait)

    def __createReadReal(self):
        # HANDLE Handle, int NBuf, char* Var, int From1, int To1, int From2, int To2, double* Values, ACSC_WAITBLOCK* Wait
        self.__ReadReal = DllFunctionWrapper(self.goMName, self.dll,
                                             (
                                                 c_void_p, c_int, c_char_p, c_int, c_int, c_int, c_int, c_void_p,
                                                 c_void_p),
                                             c_int)

    def readReal(self, Handle, NBuf, Var, From1, To1, From2, To2, Values, Wait):
        return self.__ReadReal(Handle, NBuf, Var, From1, To1, From2, To2, Values, Wait)

    def __createSysInfo(self):
        # HANDLE Handle, int Key, double* Value, ACSC_WAITBLOCK* Wait
        self.__sysInfo = DllFunctionWrapper(self.sysInfoName, self.dll, (c_void_p, c_int, c_void_p, c_void_p), c_int)

    def sysInfo(self, Handle, Key, Wait):
        # print(wrapper.sysInfo(handle, 13, byref(c_int(0))))
        buffer = c_void_p()
        #print(buffer.value)
        print(self.__sysInfo(Handle, Key, byref(buffer), Wait))
        return buffer.value

    def __createWaitMotorEnable(self):
        # HANDLE Handle, int Axis, int State, int Timeout
        self.__waitMotorEnable = DllFunctionWrapper(self.waitMotorEnabledName, self.dll, (c_void_p, c_int, c_int, c_int), c_int)

    def waitMotorEnable(self, Handle, Axis, State, Timeout):
        return self.__waitMotorEnable(Handle, Axis, State, Timeout)

    @staticmethod
    def __validateIPAndPort(IP, port):
        if not isinstance(IP, c_char_p):
            IP = c_char_p(IP)

        if not isinstance(port, c_int):
            port = c_int(port)

        return IP, port
