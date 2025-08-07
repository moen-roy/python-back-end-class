import platform
import time

def time_fun (func):
    def wrapper (*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        diff= end_time-start_time
        txt=f"function:{func.__name__} time taken {diff}.sec"
        f_name="log.txt"
        print ("Time taken to run =",diff)
        write_file(f_name ,txt)
    return wrapper

def write_file(f_name,txt):
    with open(f_name,'w')as file:
        file.write(f"{txt} \n")

@time_fun
def counter():
    for n in range(0,1400000):
        pass
counter()
        

print (f"Your OS is {platform.system()} {platform.system()} ")