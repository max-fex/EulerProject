from time import time
from datetime import datetime as dt


def time_decorator(func):
    def time_wrapper(n):
        count_start = time()
        func(n)
        count_stop = time()
        execution_time = count_stop - count_start
        print ("Function execution time is " +
               str(execution_time) + " seconds.\n")
    return time_wrapper

def time_decorator_w_start(func):
    def time_wrapper(n):
        count_start = time()
        print("Program started at: %s" % dt.utcfromtimestamp(count_start))
        func(n)
        count_stop = time()
        execution_time = count_stop - count_start
        print ("Function execution time is " +
               str(execution_time) + " seconds.\n")
    return time_wrapper