import inspect


def abstractmetod(self):
    print(f"[{type(self).__name__}] - [{inspect.stack()[1].function}] Abstract Methode")
