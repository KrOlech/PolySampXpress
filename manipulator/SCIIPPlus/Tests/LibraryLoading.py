import os
import sys
from ctypes import *
from time import sleep

from DllList import dllList
from manipulator.SCIIPPlus.DllFuntionWraper.dllFunctionWrapper import DllFunctionWrapper

print(windll.kernel32)

print(cdll.msvcrt)

# [WinDLL(dll) for dll in dllList]
dll = WinDLL(r"C:\Windows\System32\ACSCL_x64.dll")
print(dll)

parTypes = (c_void_p, c_int, c_int, c_int, c_void_p)

acsc_ClearBuffer = DllFunctionWrapper("acsc_ClearBuffer", dll, parTypes, c_int)

parTypes = (c_char_p, c_int)
acsc_OpenCommEthernetTCP = DllFunctionWrapper("acsc_OpenCommEthernetTCP", dll, parTypes, c_void_p)

acsc_OpenCommSimulatorTypes = ()
acsc_OpenCommSimulator = DllFunctionWrapper("acsc_OpenCommSimulator", dll, acsc_OpenCommSimulatorTypes, c_void_p)

print(acsc_OpenCommSimulator())

p1 = c_int(701) #nr portu
p2 = c_char_p(b"100.10.1.100") #adres IP

print(p2)
print(c_char_p(acsc_OpenCommEthernetTCP(p2, p1)))

sleep(10)

#print(acsc_ClearBuffer(byref(p1), p3, p4, p1, byref(p2)))
