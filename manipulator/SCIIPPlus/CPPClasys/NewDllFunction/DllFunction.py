from ctypes import CDLL, c_double, byref, c_long
from time import sleep


class DllFunctions:

    def __init__(self):
        self.dll = CDLL(r"C:\Windows\System32\ACSCL_x64.dll")

    def __enter__(self):
        self.handle = self.dll.acsc_OpenCommSimulator()
        return self

    def __exit__(self, type, value, traceback):
        self.dll.acsc_CloseSimulator()

    def getAxisCount(self):
        buffer = c_double(-1)
        self.dll.acsc_SysInfo(self.handle, 13, byref(buffer), 0)

        print("axis Count", buffer)

        return buffer

    def getMotorState(self):
        buffer = c_long()

        self.dll.acsc_GetAxisState(self.handle, 0, byref(buffer), 0)
        print("stan Motoru", buffer)

        return buffer.value

    def getPosition(self, axis=0):
        buffer = c_double(0)

        self.dll.acsc_GetFPosition(self.handle, axis, byref(buffer), 0)
        print("pozycja", buffer)

        return buffer

    def goToPoint(self, cell, axis=0):
        self.dll.acsc_Enable(self.handle, axis, 0)
        self.dll.acsc_WaitMotorEnabled(self.handle, axis, 1, 0)

        self.dll.acsc_ToPoint(self.handle, 0, axis, c_double(cell), 0)

        self.dll.acsc_Go(self.handle, axis, 0)
        # dll.acsc_ExtToPoint(handle,0,0,c_double(2),c_double(1),c_double(1),0) nie wymaga go


if __name__ == "__main__":

    with DllFunctions() as handle:

        handle.getMotorState()

        handle.getPosition()

        handle.goToPoint(0)

        sleep(5)

        handle.goToPoint(10)

        while handle.getMotorState():
            print("pozycja", handle.getPosition().value)

        handle.getMotorState()
        print("pozycja", handle.getPosition().value)
