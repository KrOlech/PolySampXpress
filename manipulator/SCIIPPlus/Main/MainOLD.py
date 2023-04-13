from abc import ABCMeta

from manipulator.Abstract.Main.AbstractManipulator import AbstractManipulator
from utilitis.Depracation.DepractionFactory import deprecated
from manipulator.SCIIPPlus.CPPClasys.DllFuntionWraper.DllFunctions import DllFunction


@deprecated("OLD Implementation")
class SCIManipulatorOld(AbstractManipulator, DllFunction):
    __metaclass__ = ABCMeta

    d_buffer_contents = "!axisdef X=0,Y=1,Z=2,T=3,A=4,B=5,C=6,D=7\r\n						\
    !axisdef x=0,y=1,z=2,t=3,a=4,b=5,c=6,d=7\r\n													\
    global int I(100),I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,I90,I91,I92,I93,I94,I95,I96,I97,I98,I99\r\n		\
    global real V(100),V0,V1,V2,V3,V4,V5,V6,V7,V8,V9,V90,V91,V92,V93,V94,V95,V96,V97,V98,V99\r\n	\
    global real shm MULTIDIM_LONG_ARRAY(10)(200)\r\n												\
    global real shm LONG_ARRAY(200)\r\n																\
    global real shm HELLO_VAR(2)(2)\r\n																\
    global int shm SEMAPHORE\r\n"

    d_buffer_index_query = "?sysinfo(11)\r"
    stop_and_reset_all_buffers = "##SR\r"
    received = 0
    BufferIndex = 0
    DBufferIndex = 0

    def __init__(self, screenSize):
        super().__init__(screenSize)

    def getCurrentPosition(self):
        pass

    def validateSpeed(self, speed):
        pass

    async def goto(self):
        pass

    def gotoNotAsync(self):
        pass

    def waitForTarget(self):
        pass
