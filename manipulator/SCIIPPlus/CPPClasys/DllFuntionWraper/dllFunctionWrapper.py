from ctypes import WINFUNCTYPE


class DllFunctionWrapper:

    def __init__(self, functionName, dllPointer, parameterTypes, returnType=None):
        self.functionName = functionName
        self.dllPointer = dllPointer
        self.parameterTypes = parameterTypes
        self.returnType = returnType

        self.__winFunType = WINFUNCTYPE(returnType, *parameterTypes)

        self.__bufferParams = tuple([(1, f"p{i}, 0") for i, _ in enumerate(parameterTypes)])

        self.__fun = self.__winFunType((functionName, dllPointer), self.__bufferParams)

    def __call__(self, *args, **kwargs):
        return getattr(self.dllPointer, self.functionName)(*args)
        # return self.__fun(*args)
