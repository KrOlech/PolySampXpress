import time
from functools import wraps
from Python.BaseClass.Logger.Logger import Loger


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        Loger.log(f"Executed in {execution_time:.6f} seconds", "timeit")
        return result

    return wrapper
