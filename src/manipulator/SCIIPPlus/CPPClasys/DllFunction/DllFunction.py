from ctypes import CDLL, c_double, byref, c_long, c_char_p, c_int

from src.utilitis.Logger.Logger import Loger


class DllFunctions(Loger):

    def __init__(self, *args, **kwargs):
        self.dll = CDLL(r"C:\Windows\System32\ACSCL_x64.dll")

    def __enter__(self):
        self.handle = self.dll.acsc_OpenCommEthernetTCP(c_char_p(b"10.0.0.100"), 701)
        return self

    def __exit__(self, type, value, traceback):
        self.dll.acsc_CloseSimulator()

    def getAxisCount(self):
        buffer = c_double(-1)
        self.dll.acsc_SysInfo(self.handle, 13, byref(buffer), 0)
        return int(buffer.value)

    def getMotorState(self, axis=0):
        buffer = c_long()

        self.dll.acsc_GetAxisState(self.handle, axis, byref(buffer), 0)

        return buffer.value

    def getMotorStateM(self, axis):
        state = [self.getMotorState(ax) for ax in axis]
        return any(state)

    def getPosition(self, axis=0):
        buffer = c_double(0)

        self.dll.acsc_GetFPosition(self.handle, axis, byref(buffer), 0)
        self.loger(f"Position axis {axis} is {buffer}")

        return buffer.value

    def enableAllAxis(self):
        for i in range(int(self.getAxisCount())):
            self.dll.acsc_Enable(self.handle, i, 0)
            self.dll.acsc_WaitMotorEnabled(self.handle, i, 1, 0)

    def disableAllAxis(self):
        for i in range(int(self.getAxisCount())):
            self.dll.acsc_Disable(self.handle, i, 0)

    def goToPointM(self, cellsAxisDictionary: dict):
        for axis, direction in cellsAxisDictionary.items():
            self.dll.acsc_ToPoint(self.handle, 0, axis, c_double(direction), 0)

        keys = cellsAxisDictionary.keys()

        keys = [int(key) for key in keys]

        axis = (c_int * len(keys))(*keys)

        self.dll.acsc_GoM(self.handle, axis, 0)

    def goToPoint(self, cell, axis=0):
        self.dll.acsc_ToPoint(self.handle, 0, axis, c_double(cell), 0)

        self.dll.acsc_Go(self.handle, axis, 0)
        # dll.acsc_ExtToPoint(handle,0,0,c_double(2),c_double(1),c_double(1),0) nie wymaga go

    def checkAxisStateM(self):
        return any([self.checkAxisState(axisNr) for axisNr in range(self.getAxisCount())])


    def checkAxisState(self, axisNr):

        m_MotorFault = c_int(0)

        self.dll.acsc_GetFault(self.handle, axisNr, byref(m_MotorFault), 0)

        m_MotorFault = m_MotorFault.value

        state = False

        if m_MotorFault == 1:
            self.loger(f"Right limit stop for axis {axisNr}")
            state = True

        elif m_MotorFault == 2:
            self.loger(f"Left limit stop for axis {axisNr}")
            state = True

        return state
    def checkFaultMask(self, axisNr):
        m_FaultMask = c_int(0)
        self.dll.acsc_GetFaultMask(self.handle, axisNr, byref(m_FaultMask), 0)
        self.loger(f"GetFaultMask for axis {axisNr}: {m_FaultMask.value}")

    def setPositions(self, position: dict):
        for axisNr, axisPosition in position.items():
            self.dll.acsc_SetFPosition(self.handle, axisNr, axisPosition, 0)

    def setZero(self):
        for axisNr in range(self.getAxisCount()):
            self.dll.acsc_SetFPosition(self.handle, axisNr, 0, 0)


if __name__ == "__main__":

    with DllFunctions() as handle:

        print(handle.handle)

        handle.getMotorState()

        handle.getPosition()

        handle.goToPoint(0)

        while handle.getMotorState():
            print("pozycja", handle.getPosition().value)

        handle.goToPoint(10)

        while handle.getMotorState():
            print("pozycja", handle.getPosition().value)

        handle.getMotorState()
        print("pozycja", handle.getPosition().value)
