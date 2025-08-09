import time

def timer(func):
    def wrapper():
        start=time.time()
        func()
        end= time.time()
        diff=  end- start
        print(f"The totall time taken is {diff} seconds")
    return wrapper

@timer
def slow_func():
    time.sleep(10)
slow_func()