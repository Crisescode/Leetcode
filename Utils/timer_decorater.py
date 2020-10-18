# -*- coding: utf-8 -*-

import timeit
from functools import wraps


# timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        end = timeit.default_timer()
        elapsed = end - start
        print('{0} run time: {1} '.format(func.__qualname__, elapsed))

        return res
    return wrapper
