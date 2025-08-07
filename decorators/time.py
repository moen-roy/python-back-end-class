import time

def time_fn(fn):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        fn(*args, **kwargs)
        