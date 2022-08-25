import time


def cal_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s running time: %s secs." % (func.__name__, end - start))
        return result

    return wrapper
