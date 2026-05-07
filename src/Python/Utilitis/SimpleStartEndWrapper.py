import time

from Python.BaseClass.Logger.Logger import Loger


def simpleStartEndWrapper(text):
    def inner(func):
        # code functionality here

        def wrapper(*args, **kwargs):
            start_time = time.time()
            Loger.log(f'{text} started', type(func).__name__)
            func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            Loger.log(f'{text} ended in {execution_time} s', type(func).__name__)

        return wrapper

    # returning inner function 
    return inner


