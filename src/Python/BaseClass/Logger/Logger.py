from inspect import stack
import sys
from datetime import datetime


class Loger:

    def loger(self, *message):
        self.__log(*message, state="log")

    def logError(self, message):
        self.__log(*message, state="ERROR")
        self.__log(stack(), state="ERROR")

    def logWarning(self, message):
        self.__log(*message, state="Warning")

    def abstractmetod(self):
        self.__log("Abstract Methode", state="Warning")

    def __log(self, *message, state="log"):
        info = f"[{datetime.now()}] - [{type(self).__name__}] - [{stack()[2].function}] [{state}] [{[mes for mes in message]}]"

        print(info)

        with open(f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log","a") as file:
            file.write(info+"\n")

    @staticmethod
    def isDebuggerActive() -> bool:
        return hasattr(sys, 'gettrace') and sys.gettrace() is not None
