import inspect


class Loger:

    def loger(self, *message):
        print(f"[{type(self).__name__}] - [{inspect.stack()[1].function}] {[mes for mes in message] }")

    def logError(self, message):
        print(f"[{type(self).__name__}] - [{inspect.stack()[1].function}] [ERROR] {message}")

    def logWarning(self, message):
        print(f"[{type(self).__name__}] - [{inspect.stack()[1].function}] [Warning] {message}")
