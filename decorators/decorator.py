# def my_deco(func):
#     def wrapper():
#         print ("Calling hii")
#         func()
#         print("Finished call")
#     return wrapper


# @my_deco
# def hello():
#     print ("Hii world")
# hello()

# @my_deco
# def greet():
#     print("Greetings from above")
# greet()

def mine_deco(logic):
     def wrapper ():        
        for i in range (20,1,-3):            
            logic ()
            print ("your answer is",i)
     return wrapper
@mine_deco
def moon():
    for i in range (1,20,3):
        print ("your answer is",i)
moon()