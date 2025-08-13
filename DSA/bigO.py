import time
# big O is used to know the numbere of loops used in one function
# o(log ) 
        # print (f"For {n}   the sum= {sum}")

start= time.time()
        # print (f"For {n}   the sum= {sum}")

start= time.time()

def find_sum(num):
    sum =0
    for n in range(1,num+1):
        print (f"The sum ={sum}  the num = {n}")
        sum= sum+ n
        # print (f"For {n}   the sum= {sum}")
def find_sum2(num):
    term1= num+1
    term2= term1 *num
    sum = term2/2


start= time.time()
find_sum(100)
end= time.time()
diff=end - start
print (f"Speed= {diff}")