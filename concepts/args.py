def sum (*args):
    ans= 0
    for n in  args:
        print (ans, "+" ,n,"=")
        ans = ans +n

    print (ans)
sum (10,20,30,40,50)