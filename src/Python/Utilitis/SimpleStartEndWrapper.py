from Python.BaseClass.Logger.Logger import Loger


def simpleStartEndWrapper(text):
    def inner(func):
        # code functionality here

        def wrapper(*args, **kwargs):
            Loger.log(f'{text} started', type(func).__name__)
            func(*args, **kwargs)
            Loger.log(f'{text} ended', type(func).__name__)

        return wrapper

    # returning inner function 
    return inner


