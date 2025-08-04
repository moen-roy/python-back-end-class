
to_loop= True
i=0

while to_loop:
    if i>10:
        to_loop= False
    print("i is",i)
    i= i+1
k= 0

while k<5:
    print("k is", k)
    k=k+1

for i in range(2,8):
    print ("range is working", i)
for i in range(10,2,-2):
    print ("range of 2 is working", i)
for i in range(2,20,5):
    print ("range is working", i)