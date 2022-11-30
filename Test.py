import timeit
import time
def long_function():
    print('function start')
    time.sleep(5)
    print('function end')
print(timeit.Timer(long_function).timeit(number=2))