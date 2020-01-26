from time import time
def timer(limit):
    def decorator(func):
            def inner(arg=0):
                start = time()
                func()
                return time() - start < limit - arg
            return inner
    return decorator