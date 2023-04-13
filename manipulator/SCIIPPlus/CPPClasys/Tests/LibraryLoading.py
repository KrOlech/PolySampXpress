from ctypes import *
from time import sleep

from manipulator.SCIIPPlus.DllFuntionWraper.dllFunctionWrapper import DllFunctionWrapper

print(windll.kernel32)

print(cdll.msvcrt)

# [WinDLL(dll) for dll in dllList]
dll = WinDLL(r"C:\Windows\System32\ACSCL_x64.dll")
print(dll)

parTypes = (c_void_p, c_int, c_int, c_int, c_void_p)

acsc_ClearBuffer = DllFunctionWrapper("acsc_ClearBuffer", dll, parTypes, c_int)

parTypes = (c_char_p, c_int)
acsc_OpenCommEthernetTCP = DllFunctionWrapper("acsc_OpenCommEthernetTCP", dll, parTypes, c_int)

acsc_OpenCommEthernetUDP = DllFunctionWrapper("acsc_OpenCommEthernetUDP", dll, parTypes, c_int)

acsc_OpenCommSimulatorTypes = ()
acsc_OpenCommSimulator = DllFunctionWrapper("acsc_OpenCommSimulator", dll, acsc_OpenCommSimulatorTypes, c_int)

acsc_CloseSimulator = DllFunctionWrapper("acsc_CloseSimulator", dll, acsc_OpenCommSimulatorTypes, c_int)


print("symulator", acsc_OpenCommSimulator())
sleep(10)
print("symulator close", acsc_CloseSimulator())

p1 = c_int(701)  # nr portu
p2 = c_char_p()  # adres IP

print("ethernet", acsc_OpenCommEthernetTCP(p2, p1))

print("UDP", acsc_OpenCommEthernetUDP(p2, p1))

# sleep(10)

# print(acsc_ClearBuffer(byref(p1), p3, p4, p1, byref(p2)))
