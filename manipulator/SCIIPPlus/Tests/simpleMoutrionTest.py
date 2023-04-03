from ctypes import c_int, c_double, byref, c_char_p
from time import sleep

from manipulator.SCIIPPlus.DllFuntionWraper.DllFunctions import DllFunction

wrapper = DllFunction()

handle = wrapper.OpenCommSimulator()
#handle = wrapper.OpenCommEthernetUDP(c_char_p("10.0.0.100".encode()),c_int(701))

print(wrapper.startSpiiPlusSC())

print(wrapper.enable(handle, c_int(0), byref(c_int(0))))

print(wrapper.getFPosition(handle, c_int(0), byref(c_int(0))))

print(wrapper.ToPoint(handle, c_int(0), c_int(0), c_double(10.0), byref(c_int(0))))

print(wrapper.getFPosition(handle, c_int(0), byref(c_int(0))))

print(wrapper.disable(handle, c_int(0), byref(c_int(0))))

#print(wrapper.getAxesCount(handle, byref(c_int(0))))

print(wrapper.stopSpiiPlusSC())

print(wrapper.closeSimulator())
