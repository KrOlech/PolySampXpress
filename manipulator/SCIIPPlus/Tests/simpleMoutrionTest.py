from ctypes import c_int, c_double, byref, c_char_p
from time import sleep

from manipulator.SCIIPPlus.DllFuntionWraper.DllFunctions import DllFunction

wrapper = DllFunction()

handle = wrapper.OpenCommSimulator()
# handle = wrapper.OpenCommEthernetUDP(c_char_p("10.0.0.100".encode()),c_int(701))

print(wrapper.startSpiiPlusSC())

print(wrapper.enable(handle, c_int(0), byref(c_int(0))))

print(wrapper.waitMotorEnable(handle,c_int(0), c_int(1), c_int(3000)))

print(wrapper.getFPosition(handle, c_int(0), byref(c_int(0))))

print(wrapper.sysInfo(handle, 10, byref(c_int(0))))

#buffer = c_double(0)

#print(wrapper.readReal(handle, c_int(0), b"FPOS", c_int(0), c_int(0), c_int(-1),c_int(-1), byref(buffer), byref(c_int(0))))
#print(buffer.value)

print(wrapper.ToPoint(handle, c_int(0), c_int(0), c_double(-10.0), byref(c_int(0))))

print(wrapper.Go(handle, c_int(0), byref(c_int(0))))

print(wrapper.getFPosition(handle, c_int(0), byref(c_int(0))))


print(wrapper.disable(handle, c_int(0), byref(c_int(0))))

# print(wrapper.getAxesCount(handle, byref(c_int(0))))

print(wrapper.stopSpiiPlusSC())

print(wrapper.closeSimulator())
