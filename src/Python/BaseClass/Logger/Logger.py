from inspect import stack
import sys
from datetime import datetime


class Loger:

    def logStart(self):
        self._logImportant(" Program Starting ", (41, 42))

    def logEnd(self):
        self._logImportant(" Program Stoping ", (41, 42))

    def _logImportant(self, mesage, offset=(42, 42)):
        self.loger("#" * 100)
        self.loger("#" * offset[0] + mesage + "#" * offset[1])
        self.loger("#" * 100)

    def loger(self, *message):
        self.__log(*message, state="log")

    def logError(self, *message):
        self.__log(*message, state="ERROR")
        msg = []
        for fun in stack():
            msg.append(fun.function)
        self.__log(msg, state="ERROR")

    def logWarning(self, *message):
        self.__log(*message, state="Warning")

    def abstractmetod(self, name=None):
        if name:
            self.__log(f"Abstract Methode {name}", state="Warning")
        else:
            self.__log("Abstract Methode", state="Warning")

    def __log(self, *message, state="log"):
        info = f"[{datetime.now()}] - [{type(self).__name__}] - [{self.__resolveFunctionCall()}] [{state}] [{[mes for mes in message]}]"

        print(info)

        with open(f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log", "a") as file:
            file.write(info + "\n")

    @staticmethod
    def __resolveFunctionCall():
        try:
            return stack()[2].function
        except IndexError as e:
            return stack()[0].function

    @staticmethod
    def log(message, type, state="log"):
        info = f"[{datetime.now()}] - [{type}] - [{stack()[2].function}] [{state}] [{message}]"

        print(info)

        with open(f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log", "a") as file:
            file.write(info + "\n")

    @staticmethod
    def isDebuggerActive() -> bool:
        return hasattr(sys, 'gettrace') and sys.gettrace() is not None
